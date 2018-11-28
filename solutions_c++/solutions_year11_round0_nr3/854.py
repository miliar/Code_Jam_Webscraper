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
int tt,ti,n,sum,xr,mn;
int a[2000];
int main(){
	#ifdef home
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	scanf("%d",&n);
    	sum=0;
    	mn=1000000000;
    	xr=0;
    	for (int i=0;i<n;i++){
    		scanf("%d",&a[i]);
    		mn=min(mn,a[i]);
    		sum+=a[i];
    		xr^=a[i];
    	}
    	printf("Case #%d: ",ti+1);
    	if (xr!=0){
    		printf("NO\n");
    	} else {
    		printf("%d\n",sum-mn);
    	}

    	
    }
    return 0;
}









