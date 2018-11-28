
#include <stdio.h>
#include <time.h>

#include <vector>
#include <list>
#include <set>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <iomanip>
#include <sstream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <stack>
#include <numeric>
#include <complex>

using namespace std;


typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;
#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a, n) memset(a, n, sizeof(a))
#define PB(n) push_back(n)
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()

#define NUM 1000000

int T, N, M;
string words[1000000];
string seqs[105];
typedef pair<int, int> PII;
struct node;
typedef map<int, node*> MIN;
struct node {
	int leaf;
	MIN child;	
};
node all_nodes[1000000];
int node_cnt = 0;

void put(node *root, int w, int n, int m, int w_msk) {
	char c = seqs[m][n];
	string &wd = words[w];
	int msk = 0;
	FORI(i, SZ(wd))
		if(wd[i] == c)
			msk |= 1<<i;
	if(!root->child.count(msk)) {
		node *nxt = &all_nodes[node_cnt++];
		nxt->child.clear();
		nxt->leaf = -1;
		root->child[msk] = nxt;
	}
	w_msk = w_msk |= msk;
	if(w_msk == (1<<SZ(wd))-1) {
		root->child[msk]->leaf = w;
		return;
	}
	put(root->child[msk], w, n+1, m, w_msk);
}

PII count(node *root) {
	if(SZ(root->child) == 0) {
		return PII(root->leaf, -1);
	}
	if(SZ(root->child) == 1) {
		pair<int, node*> chd = *root->child.begin();
		PII res = count(chd.second);
		return res;
	}
	PII best(-1, -1);
	FORE(it, root->child, MIN) {
		pair<int, node*> chd = *it;
		PII res = count(chd.second);
		int ad = (chd.first == 0)?1:0;
		if(res.second == -1)
			res.second = 0;
		res.second += ad;
		if(best.first == -1)
			best = res;
		else if(best.second < res.second)
			best = res;
		else if(best.second == res.second && best.first > res.first)
			best = res;
	}
	return best;	
}


int main(int argc, char* argv[])
{
#define TASK_NAME(file) "B"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2011\\Round1A\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt1.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt1.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> T;
	FORI(ncase, T) {
		in >> N >> M;
		FORI(i, N)
			in >> words[i];
		FORI(i, M)
			in >> seqs[i];

		out << "Case #" << (ncase+1) << ": ";
		FORI(m, M) {
			PII res (-1, -1);
			FORIS(l, 1, 11) {
				node_cnt = 0;
				node *root = &all_nodes[node_cnt++];
				root->child.clear();
				root->leaf = -1;
				FORI(i, N) {
					if(SZ(words[i]) == l) {
						put(root, i, 0, m, 0);
					}
				}
				if(root->child.empty())
					continue;
				PII r = count(root);
				if(r.second != -1) {
					if(r.second > res.second)
						res = r;
					else if(r.second == res.second && r.first < res.first)
						res = r;
				}
			}
			if(res.first == -1)
				res.first = 0;
			out << words[res.first];
			if(m < M-1)
				out << " ";
		}
		out << endl;
	}
	return 0;
}

