#include<vector>
#include<cmath>
#include<map>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<string>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<set>
#include<stack>
#include<bitset>
#include<functional>
#include<cstdlib>
#include<ctime>
#include<queue>
#include<deque>
using namespace std;
#define pb push_back
typedef long long lint;
#define mp make_pair
#define fi first
#define se second
typedef pair<int,int> pint;
vector <string> tmp;
bool ta(vector <string> a,int b){
	int i,j,n=a.size();
	for(i=0;i<b;i++){
		if(b*2-i>=n) continue;
		for(j=0;j<n;j++){
//			cout<<a[i][j]<<a[b*2-i][j]<<endl;
			if(a[i][j]!='a' && a[b*2-i][j]!='a' && a[i][j]!=a[b*2-i][j]) return false;
		}
	}
	return true;
}
bool yo(vector <string> a,int b){
	int i,j,n=a.size();
	for(i=0;i<b;i++){
		if(b*2-i>=n) continue;
		for(j=0;j<n;j++){
//			cout<<a[j][i]<<a[j][b*2-i]<<endl;
			if(a[j][i]!='a' && a[j][b*2-i]!='a' && a[j][i]!=a[j][b*2-i]) return false;
		}
	}
	return true;
}
int main()
{
	int i,j,k,t,n,a;string tm="";vector <int> out;
	for(i=0;i<110;i++) tm+='a';for(i=0;i<110;i++) tmp.pb(tm);
	cin>>t;
	for(i=0;i<t;i++){
//		memset(pi,0,sizeof(pi));
//		vector <string> ma=tmp;
		cin>>n;
		vector <string> ma;
		for(j=0;j<2*n-1;j++) ma.pb(tm.substr(0,2*n-1));
		for(j=1;j<2*n;j++){
//			if(j<n) for(k=0;k<j;k++) scanf("%d",&pi[j-1][k]);
//			else for(k=0;k<2*n-j;k++) scanf("%d",&pi[j-1][k]);
			if(j<n){
				for(k=0;k<j;k++){
					scanf("%d",&a);ma[j-1][n-j+2*k]=(a+'0');
				}
			}
			else{
				for(k=0;k<2*n-j;k++){
					scanf("%d",&a);ma[j-1][j-n+2*k]=(a+'0');
				}
			}
		}
//		for(j=0;j<n*2-1;j++) cout<<ma[j].substr(0,n*2-1)<<endl;
		int x=0,y=0;
		for(j=0;j<=n-1;j++){
			if(ta(ma,n-1+j)){x=j;break;}
			if(ta(ma,n-1-j)){x=j;break;}
		}
		for(j=0;j<=n-1;j++){
			if(yo(ma,n-1+j)){y=j;break;}
			if(yo(ma,n-1-j)){y=j;break;}
		}
//		cout<<x<<' '<<y<<endl;

//		yo(ma,1);
		out.pb((n+x+y)*(n+x+y)-n*n);
	}
	for(i=0;i<t;i++) cout<<"Case #"<<i+1<<": "<<out[i]<<endl;
	return 0;
}
