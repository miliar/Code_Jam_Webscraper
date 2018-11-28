#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
#define MAX 102102
int mat[102][102];
struct unionfind {
    int parent[MAX];
    int rank[MAX];
    
    unionfind() {
		int i;
        for(i = 0; i <MAX;i++) 
			parent[i] = i, rank[i] = 1;
    }
    

    int findpar( int x ) {
        if( parent[x] == x ) return x;
        else return parent[x] = findpar( parent[x] ); 
    }
    
    void Union(int x, int y) {
        int xroot = findpar( x );
        int yroot = findpar( y );
        
        if( xroot == yroot ) return; 
                
        if( rank[ xroot ] < rank[ yroot ] ) 
			parent[ xroot ] = yroot, rank[ yroot ] += rank[ xroot ];
        else parent[ yroot ] = xroot, rank[ xroot ] += rank[ yroot ];
    }
};
int w,h;
bool valid(int a,int b)
{
	if(a<0||a>=h||b<0||b>=w)	return false;
	return true;

}
int convert(int a,int b)
{
	return a*1000+b;
}

char res[101][101];

vector <int> pars[102102];
int main()
{
	int tc,fug = 1;
	cin>>tc;
	while(tc--)
	{
		unionfind mu;
		int i,j,k;
		cin>>h>>w;
		for(i = 0;i<h;i++)
			for(j = 0;j<w;j++)
				cin>>mat[i][j];
			int dx[] = {-1,0,0,1};
			int dy[] = {0,-1,1,0};
		for(i = 0;i<h;i++)
			for(j = 0;j<w;j++)
			{
				int mn = 1000000000,ki,kj;
				for(k = 0;k<4;k++)
				{
					if(valid(i+dx[k],j+dy[k]))
					{
						if(mat[i+dx[k]][j+dy[k]] < mn)
						{
							mn = mat[i+dx[k]][j+dy[k]];
							ki = i+dx[k], kj = j+dy[k];
						}
					}
				}
				if(mn<mat[i][j])
				{
					mu.Union(convert(i,j),convert(ki,kj));
				}				
			}
			CLR(res);
			for(i = 0;i<102102;i++) pars[i].clear();
			
			for(i = 0;i<h;i++)
			{
				for(j = 0;j<w;j++)
				{
					int now = mu.findpar(convert(i,j));
					pars[now].push_back(convert(i,j));
				}
			}
			bool done[102102] = {0};
			char put = 'a';
			for(i = 0;i<h;i++)
			{
				for(j = 0;j<w;j++)
				{
					int now = mu.findpar(convert(i,j));
					if(done[now])	continue;
					done[now] = true;
					for(k = 0;k<pars[now].size();k++)
					{
						int aa = pars[now][k]/1000;
						int bb = pars[now][k]%1000;
						res[aa][bb] = put;
					}
					put++;
				}
			}
			printf("Case #%d:\n",fug);
			fug++;
			for(i = 0;i<h;i++)
			{
				cout<<res[i][0];
				for(j = 1;j<w;j++)
				{
					cout<<" "<<res[i][j];
				}
				cout<<endl;
			}


	}

	return 0;
}