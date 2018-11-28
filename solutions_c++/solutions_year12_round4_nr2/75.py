#include<iostream>
#include<cstdio>
#include<vector>

using namespace std;

#define MAXN 1010
const int inf = 1000000000;

struct Tree{
	double X, Y;
	vector<int> childs;
} T[MAXN];

int N, W, L;
vector<int> R;
int O[MAXN];
vector<int> Base;
double OX[MAXN], OY[MAXN];

bool tryins(int root, int t)
{
	for (int i = 0; i < T[root].childs.size(); i++ )
		if (tryins(T[root].childs[i], t)) return true;
	double newX, newY;
	if (T[root].childs.size() > 0)
	{
		int lastchild = T[root].childs[T[root].childs.size() - 1];
		newX = T[lastchild].X + R[lastchild] + R[t];
	}
	else 
		newX = max(T[root].X - R[root] + R[t], 0.0);
	newY = T[root].Y + R[root] + R[t];
	if (newY + R[t] > L) return false;
	if (newX + R[t] > T[root].X + R[root]) return false;
	T[t].X = newX; T[t].Y = newY;
	T[t].childs.clear();
	T[root].childs.push_back(t);
	return true;
}

void insert(int t)
{
	for (int i = 0; i < Base.size(); i++ )
		if (tryins(Base[i], t)) return;
	if (Base.size() > 0)
		T[t].X = T[Base[Base.size() - 1]].X + R[Base[Base.size() - 1]] + R[t];
	else
		T[t].X = 0;
	T[t].Y = 0;
	T[t].childs.clear();		
	Base.push_back(t);
}

void solve(int casen)
{
	scanf( "%d", &N );
	scanf( "%d %d", &W, &L );
	R.clear();
	for (int i = 0; i < N; i++ )
	{
		int t;
		scanf( "%d", &t );
		R.push_back(t * N + i);
	}
	sort(R.begin(), R.end());
	Base.clear();
	for (int i = 0; i < N; i++ )
	{
		O[i] = R[i] % N;
		R[i] /= N;
	}
	for (int i = R.size() - 1; i >= 0; i-- )
		insert(i);
	for (int i = 0; i < N; i++ ){
		OX[O[i]] = T[i].X;
		OY[O[i]] = T[i].Y;
	}
	printf( "Case #%d: ", casen );
	for (int i = 0; i < N; i++ )
		printf( "%.2lf %.2lf%c", OX[i], OY[i], (i == N - 1 ? '\n' : ' ') ); 
}

int main()
{
	freopen( "in.txt", "r", stdin );
	freopen( "out.txt", "w", stdout );
	int test_cases;
	scanf( "%d", &test_cases );
	for (int i = 1; i <= test_cases; i++ )
		solve(i);
}

 