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
int tt,ti,n,cnt;
int a[2000];
int main(){
	#ifdef home
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	scanf("%d",&n);    	
    	cnt=0;
    	for (int i=0;i<n;i++){
    		scanf("%d",&a[i]);    		
    		if (a[i]==i+1) cnt++;
    	}
    	printf("Case #%d: %.18lf\n",ti+1,1.0*(n-cnt));        	
    }
    return 0;
}









