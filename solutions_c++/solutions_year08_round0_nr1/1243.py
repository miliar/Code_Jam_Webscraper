#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <queue>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <cmath>
using namespace std;

#define SMAX 100
#define QMAX 1000
#define oo 1000000000
int dp[QMAX][SMAX],f[QMAX];
map<string,int> engine;
int main() {
	ifstream cin ("A-large.in");
    ofstream cout ("A-large.out");
	int i,j,k,n,s,q,res;
	int c;
	string str;
	for(cin>>n,c=1;c<=n;c++) {
		engine.clear();
		for(cin>>s,cin.get(),i=0;i<s;i++) {
			getline(cin,str);
			engine[str]=i;
		}
		for(cin>>q,cin.get(),i=0;i<q;i++) {
			getline(cin,str);
			f[i]=engine[str];
		}
		for(i=0;i<q;i++)
			for(j=0;j<s;j++)
				dp[i][j]=oo;
		for(i=0;i<s;i++) {
			if(i!=f[0]) dp[0][i]=0;
		}
		for(i=1;i<q;i++) {
			for(j=0;j<s;j++) {
				if(f[i]==j) continue;
				dp[i][j]=min(dp[i-1][j],dp[i-1][f[i]]+1);
				/*for(k=0;k<s;k++) {
					if(k==j) continue;
					dp[i][j]=min(dp[i][j],dp[i-1][k]+1);
				}*/
			}
		}
		res=oo;
		for(i=0;i<s;i++)
			res=min(res,dp[q-1][i]);
		cout<<"Case #"<<c<<": "<<res<<endl;
	}
}