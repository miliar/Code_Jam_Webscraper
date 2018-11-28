#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <queue>
#include <numeric>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define F(i,a,b) for(int i=(a);i<(b);++i)
#define Fe(it,v)for(__typeof__((v).begin()) it=(v).begin();it!=(v).end();++it)
#define all(x) (x).begin(),(x).end()
using namespace std;
int main(){
	int test=1;
	int N;
	cin>>N;
	int B[200][20];
	while(N--){
		
		int n;
		int m;
		cin>>n;
		cin>>m;
		#define pii pair<int,int> 
			//vector<pii> B[200];
		memset(B,-1,sizeof(B));
		F(i,0,m){
			int t;
			cin>>t;
			F(j,0,t){
				int x,y;
				cin>>x>>y;
				//B[i].push_back(pii(x,y));
				B[i][x-1]=y;
			}
		}	
		int ret=n+1,mask;
		F(i,0,1<<n){
			int ct=0;
			F(j,0,n)if((i>>j)&1){
				++ct;
			}
			
			bool sat[200]={};
			F(j,0,n){
				int t=(i>>j)&1;
				F(k,0,m){
					if(B[k][j]==t)sat[k]=1;
				}
			}
			int st=0;
			F(j,0,m)if(sat[j])++st;
			//cout<<i<<" "<<st<<endl;
			if(st==m&&ret>ct){
				ret=ct;
				mask=i;
			}
		}
		if(ret<=n){
			cout<<"Case #"<<test++<<":";
			F(i,0,n){
				int t=(mask>>i)&1;
				cout<<" "<<t;
			}	
			cout<<endl;
		}
		else{
			cout<<"Case #"<<test++<<": IMPOSSIBLE"<<endl;
		}
	}
}
