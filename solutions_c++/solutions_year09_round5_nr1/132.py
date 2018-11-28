#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

const int MAXN = 13;
const int MAX_HASH = 1000009;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

/**
 * HashMap
 * author: tudejian@ZSU
 */
template <class K, class V, class HashFcn>
class HashMap
{
public :
    struct HashNode
    {
        pair <int, int> key;
        V value;
        HashNode* next;
    };

    HashNode* hashM, ** bucket;
    HashFcn hashFcn;
    int hashSize, hashN, * vst;

    HashMap(int hashSize_) : hashSize(hashSize_)
    {
        hashM = new HashNode[hashSize];
        bucket = new HashNode * [hashSize];
        vst = new int[hashSize / 32 + 1];
        hashN = 0;
        memset(vst, 0, (hashSize / 32 + 1) * sizeof(int));
    }

    //~HashMap()
    //{
    //    delete[] hashM; delete[] bucket; delete[] vst;
    //}

    void clear()
    {
        hashN = 0;
        memset(vst, 0, (hashSize / 32 + 1) * sizeof(int));
    }

    V& operator [](const K& key)
    {
        pair<int, int> h = hashFcn(key);
        HashNode* p;
        int i = (h.first * 1313131313 + h.second & 0x7fffffff) % hashSize;
        if (!(vst[i >> 5] & (1 << (i & 31))))
            bucket[i] = NULL;
        for (p = bucket[i]; p; p = p->next)
            if (p->key == h)
                return p->value;
        vst[i >> 5] |= 1 << (i & 31);
        p = &hashM[hashN++];
        p->key = h;
        p->next = bucket[i];
        bucket[i] = p;
        return p->value = 0; // or just return p->value;
    }

    int count(const K& key)
    {
        pair<int, int> h = hashFcn(key);
        HashNode* p;
        int i = (h.first * 1313131313 + h.second & 0x7fffffff) % hashSize;
        if (!(vst[i >> 5] & (1 << (i & 31))))
            bucket[i] = NULL;
        for (p = bucket[i]; p; p = p->next)
            if (p->key == h)
                return 1;
        return 0;
    }
};

struct HashPair
{
    pair <int, int> operator ()(const pair <int, int>& key) const
    {
        return key;
    }
};

HashMap< pair <int, int>, int, HashPair> hash(1000000);

int R, C;
int N;
char mat[MAXN][MAXN];

struct Node {
	pair <int, int> pt[5];
	bool operator == (const Node &b) const {
		int i;
		for (i = 0; i < N; ++i)
			if (pt[i] != b.pt[i]) return false;
		return true;
	}
};

Node open[1000009];
int tail;



pair <int, int> hashFcn(const Node &cur) {
	int i, h1 = 0, h2 = 0;
	for (i = 0; i < N; ++i) {
		h1 = h1 * 131 + cur.pt[i].first;
		h2 = h2 * 13131 + cur.pt[i].second;
	}
	return make_pair(h1, h2);
}

int cc;
bool mark[13][13];
bool vst[13][13];
int dist[1000009];

void dfs(int x, int y) {
	++cc;
	vst[x][y] = true;
	int i, r, c;
	for (i = 0; i < 4; ++i) {
		r = x + dx[i];
		c = y + dy[i];
		if (r >= 0 && r < R && c >= 0 && c < C && !vst[r][c] && mark[r][c])
			dfs(r, c);
	}
}

bool check(const Node &cur) {
	memset(vst, 0, sizeof(vst));
	memset(mark, 0, sizeof(mark));
	for (int i = 0; i < N; ++i)
		mark[cur.pt[i].first][cur.pt[i].second] = true;
	cc = 0;
	dfs(cur.pt[0].first, cur.pt[0].second);
	return cc == N;
}





int bfs() {
	int i, j, k;
	int cnt = 0, c1 = 0;
	Node src;
	Node dst;

	for (i = 0; i < R; ++i)
		for (j = 0; j < C; ++j) {
			if (mat[i][j] == 'o' || mat[i][j] == 'w') {
				src.pt[cnt++] = make_pair(i, j);
		//		printf("(%d, %d)", i, j);
			}
			if (mat[i][j] == 'x' || mat[i][j] == 'w') {
				dst.pt[c1++] = make_pair(i, j);
			}
		}
	if (cnt != c1) return -1;
	N = cnt;
	sort(src.pt, src.pt + N);
	sort(dst.pt, dst.pt + N);

	if (src == dst) return 0;

//	printf("N = %d\n", N);
	
	int head, tail;
	head = tail = 0;
	hash.clear();

	open[tail++] = src;
	hash[hashFcn(src)] = true;
	dist[0] = 0;

	bool mark[13][13];
	memset(mark, 0, sizeof(mark));

	while (head < tail) {
		int r, c, r1, c1;
		bool safe;
		Node cur = open[head];
		safe = check(cur);
	//	printf("safe = %d\n", safe);
		for (i = 0; i < N; ++i)
			mark[cur.pt[i].first][cur.pt[i].second] = true;
		for (i = 0; i < N; ++i) {
			for (j = 0; j < 4; ++j) {
				r = cur.pt[i].first + dx[j];
				c = cur.pt[i].second + dy[j];
				r1 = cur.pt[i].first + dx[(j + 2) % 4];
				c1 = cur.pt[i].second + dy[(j + 2) % 4];

				if (r >= 0 && r < R && c >= 0 && c < C &&
					r1 >= 0 && r1 < R && c1 >= 0 && c1 < C && mat[r][c] != '#' && mat[r1][c1] != '#' &&
					!mark[r][c] && !mark[r1][c1]) {
					Node newP = cur;
					newP.pt[i] = make_pair(r, c);
					sort(newP.pt, newP.pt + N);
					if (!hash.count(hashFcn(newP)) && (safe || check(newP))) {
						hash[hashFcn(newP)] = true;
						open[tail] = newP;
						dist[tail++] = dist[head] + 1;
						if (newP == dst) return dist[tail - 1];
					}
				}
			}
		}
		for (i = 0; i < N; ++i)
			mark[cur.pt[i].first][cur.pt[i].second] = false;
		++head;
	}
	return -1;
}

int main() {
	freopen("F:\\A-large.in", "r", stdin);
	freopen("F:\\A-large.out", "w", stdout);
	int T, cas = 0;
	int i, j;
	scanf("%d", &T);

	while (T--) {
		scanf("%d%d", &R, &C);
		for (i = 0; i < R; ++i)
			scanf("%s", mat[i]);
		printf("Case #%d: %d\n", ++cas, bfs());
	}
	return 0;
}

				



				
/*

  6
5 4
....
#x.#
#..#
#o.#
#..#

  */