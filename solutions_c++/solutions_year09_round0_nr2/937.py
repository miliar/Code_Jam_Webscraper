#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<set>
#define vi vector<int>
#define vs vector<string>

#define REP(i,n) for(int i=0;i<(int) n;i++)
#define LL long long
#define INF (2<<29)

using namespace std; 

/**  union rank */
int p[100000],rank[100000];
char G[100000];// max_size 
void make_set(int n){
    for(int i=0;i<n;i++){
        p[i]=i;
        rank[i]=0;
        G[i] = 'A';
    }
}
int find_set(int x){
    if(x!=p[x])
       p[x]=find_set(p[x]);
    return p[x];
}
void link(int x,int y){
    if(rank[x]>rank[y]){
        p[y]=x;
    }
    else{
        p[x]=y;
        if(rank[x]==rank[y])
           rank[y]++;
    }
}                    
void unite(int x,int y){
    link(find_set(x),find_set(y));
}      
/***/    

int N, M;
int A[100][100];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

inline int f(int x, int y)
{
	return x * M + y;
}

int main()
{
	
	int kases;
	cin >> kases;
	
	for(int kase = 1; kase <= kases; ++kase)
	{
		
		cin >> N >> M;
		
		make_set( N * M);
		
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				cin >> A[i][j];
			}
		}
		
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				int X, Y;
				X = Y = -1;
				int mini = 10000000;
				for(int k = 0; k < 4; ++k)
				{
					int x = dx[k] + i;
					int y = dy[k] + j;
					if(x < 0 || y < 0 || x >= N || y >= M)
					{
						continue;
					}
					if(A[x][y] < A[i][j] && A[x][y] < mini)
					{
						mini = A[x][y];
						X = x;
						Y = y;
					}
				}
					
				if(X != -1)
				{
					unite(f(X, Y), f(i,j));
				}
				
			}
		}
		 
		cout << "Case #" << kase << ":" << endl;
		char color = 'a';
		for(int i = 0; i < N; ++i)
		{
			for(int j = 0; j < M; ++j)
			{
				if(j)
					cout << " ";
				int setId = find_set(f(i,j));
				if(G[setId] == 'A')
				{
					G[setId] = color;
					color++;
				}
				cout << G[setId];	
			}
			cout << endl;
		}
		
	}
	
	return 0;
}
