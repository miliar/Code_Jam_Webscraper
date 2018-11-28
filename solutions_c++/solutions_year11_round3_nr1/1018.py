#include<iostream>
#include<vector>
#include<string.h>
#include<stdio.h>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<fstream>
#include<sstream>
#include<algorithm>
#include<numeric>
#include<math.h>
#include<limits.h>
using namespace std;
#define rp(i,a,b) for(int i = (a); i < (b); i++)
#define rrp(i,a,b) for(int i = (b); i >= (a); i--)
#define ri(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define C(x,with) memset(x,with,sizeof(x))
#define S(v) (v).size()
#define ll long long int
#define ii pair<int,int>

void op(int t){
	cout << "Case #" << t << ": ";
}

int main()

{

	int _test;
	cin >> _test;
	rp(_t,1,_test+1){
		op(_t);
		cout << "\n";
		int n,m;
		cin>>n>>m;
		int a[n][m];
		rp(i,0,n)
			rp(j,0,m){
			 	char c;
				cin >> c;
				if(c=='#')
					a[i][j]=1;
				else	
					a[i][j]=0;
			}
		set<ii>v;
		rp(i,0,n-1)
			rp(j,0,m-1){
				if(a[i][j]==1&&a[i][j+1]==1&&a[i+1][j]==1&&a[i+1][j+1]==1){
					a[i][j]=2;a[i][j+1]=2;a[i+1][j]=2;a[i+1][j+1]=2;
					v.insert(make_pair(i,j));
				}	
			}
		bool ok=1;
		rp(i,0,n)
			rp(j,0,m)
				if(a[i][j]==1) ok=0;
		char f[n][m];
		if(!ok)
			cout << "Impossible\n";
		else{
			rp(i,0,n)
				rp(j,0,m)
					if(v.find(ii(i,j))!=v.end()){
						f[i][j]='/';
						f[i][j+1]='\\';
						f[i+1][j]='\\';
						f[i+1][j+1]='/';
					}
				        else if(a[i][j]==0)
						f[i][j]='.';		
					
			rp(i,0,n){
				rp(j,0,m)
					cout<<f[i][j];
				cout << "\n";
			}
		}
		
		
					



	}


	return 0;
}
