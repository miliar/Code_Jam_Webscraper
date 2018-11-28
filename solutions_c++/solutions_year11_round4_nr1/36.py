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
int x,s,r,t,n;
int w[10000];
ld l[10000];
int b[10000];
int e[10000];

ld ans,tk;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int tt;
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	printf("Case #%d: ",ti+1);
    	scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
    	w[n]=0;
    	l[n]=x;
    	for (int i=0;i<n;i++){
    		scanf("%d %d %d",&b[i],&e[i],&w[i]);
    		l[i]=e[i]-b[i];
    		l[n]-=l[i];
    	}
    	for (int i=0;i<=n;i++)
    		for (int j=i+1;j<=n;j++) if (w[i]>w[j]){
    			swap(w[i],w[j]);
    			swap(l[i],l[j]);
    		}
    	tk=t;
    	ans=0;
    	//cerr<<"Start"<<endl;
    	for (int i=0;i<=n;i++){
    		//cerr<<l[i]<<" "<<w[i]<<" "<<tk<<" "<<ans<<endl;
    		if ((r+w[i])*tk>=l[i]){
    			ans+=l[i]/(r+w[i]);
    			tk-=l[i]/(r+w[i]);
    		} else {
    			ans+=tk+(l[i]-(r+w[i])*tk)/(s+w[i]);
    			tk=0;
    		}
    	}
    	printf("%.18lf",(double)ans);
    	printf("\n");
    }
    return 0;
}









