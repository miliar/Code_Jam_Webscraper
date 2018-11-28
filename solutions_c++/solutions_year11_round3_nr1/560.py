#include<iostream>
#include<string>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
using namespace std;

const int maxn = 110;

string g[maxn];


int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;

	
	string str;
	int nca;
	int R,C,N;

	cin>>nca;
	for(int cid=1;cid<=nca;cid++){
		
		
		int v;
		double p;
		N=0;

		bool ok = true ;
		cin>>R>>C;
		for(i=0;i<R;i++){
			cin>>g[i];
		}

		for(i=0;i<R;i++)
		{
			for(j=0;j<C;j++){
				if( g[i][j] == '#' )
				{
					if( i+1 < R && j+1 < C )
					{
						if( g[i][j] == '#' && g[i+1][j] =='#' && g[i][j+1] == '#' && g[i+1][j+1] == '#' )
						{
							g[i][j] = g[i+1][j+1] = '/';
							g[i][j+1] = g[ i+1][j] = '\\';
							
						}
					}
				}
			}
		}

		for(i=0;i<R;i++)for(j=0;j<C;j++)if( g[i][j] =='#' )ok = false;

		printf("Case #%d:\n",cid);
		if( ok ){
			for(i=0;i<R;i++)cout<<g[i]<<endl;
		}
		else {
			cout<<"Impossible"<<endl;
		}
		
	}

		
}

/*
4
4
.11.
0.00
01.1
.10.


*/