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
string s[200];
int q[2000];
int n,m;
int t[2000][200];
int f(int x,int y){
	if(x==m)return 0;
	int &ret=t[x][y];
	if(ret!=-1)return ret;
	ret=1000;
	//cout<<ret<<endl;
	F(i,1,n+1)if(q[x]!=i){
		//cout<<i<<endl;
		ret=min(ret,(i==y?0:1)+f(x+1,i));
	}
	//cout<<x<<" "<<y<<" "<<ret<<endl;
	return ret;
}
int main(){
	int N,test=1;
	cin>>N;
	while(N--){
		cin>>n;
		getline(cin,s[0]);
		F(i,1,n+1){
			getline(cin,s[i]);
		}
		cin>>m;
		string tru;
		getline(cin,tru);
		F(i,0,m){
			getline(cin,tru);
			F(j,1,n+1)if(tru==s[j]){
				q[i]=j;
			}
		}
		memset(t,-1,sizeof(t));
		cout<<"Case #"<<test++<<": "<<(m==0?0:f(0,0)-1)<<endl;
	}
}
