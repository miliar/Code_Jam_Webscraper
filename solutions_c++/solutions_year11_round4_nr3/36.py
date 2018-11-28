#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>
#include<map>
#include<set>
#include<ctime>
#include<cassert>
using namespace std;
#define y1 fndjifhwdn
#define ws vfsdkofsjd
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pi;
const int N=1000000;
ll n;
ll tk;
ll ans;
int kp;
int d[N+10];
int p[N];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
  	kp=0;
    for (int i=2;i<=N;i++){
    	if (d[i]==0){
    		p[kp++]=i;
    		d[i]=i;
    	}
    	for (int j=0;j<kp && p[j]<=d[i] && i*p[j]<=N;j++) {
    		d[i*p[j]]=p[j];
    	}
    }
	int tt;
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	printf("Case #%d: ",ti+1);
    	cin>>n;
    	ans=0;
    	for (int i=0;i<kp;i++) if (p[i]<=n){
    		tk=p[i];
    		while (tk*p[i]<=n){
    			ans++;
    			tk*=p[i];
    		}
    	}
    	if (n==1){
	    	ans=-1;
	    } 	    	
	    cout<<ans+1;	    
    	printf("\n");
    }
    return 0;
}









