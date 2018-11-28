#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<bitset>
#include<cassert>

using namespace std;

typedef long long ll;
typedef pair<int,int> pint;
typedef vector<int> vint;

#define mp make_pair
#define pb push_back
#define REP(i,a,b) for(int i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)



int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int t;
	cin>>t;
	REP(cas,1,t+1){
		char buf[100];
		scanf(" %s",buf);
		int n=strlen(buf);
		int na[100];
		rep(i,n){
			na[i]=buf[i]-'0';
		}
		int j;
		for(j=n-1;j>0;--j){
			if(na[j]>na[j-1])break;
		}
		printf("Case #%d: ",cas);
		if(j){
			int k;
			for(k=n-1;;--k){
				if(na[j-1]<na[k])break;
			}
//			cout<<j<<" "<<k<<endl;
			swap(na[j-1],na[k]);
			for(int l=n-1;n-1+j-l<l;--l){
				swap(na[l],na[n-1+j-l]);
			}
			rep(i,n)printf("%d",na[i]);
			cout<<endl;
		}else{
			na[n]=0;
			sort(na,na+n+1);
			int k;
			for(k=0;!na[k];++k);
			swap(na[0],na[k]);
			rep(i,n+1)printf("%d",na[i]);
			cout<<endl;
		}
	}
	
	
	return 0;
}
