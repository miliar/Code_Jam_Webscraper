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
int tt,ti,n,tp1,tp2,lt1,lt2;
char w[1000];
int d[1000];

int main(){
	#ifdef home
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	scanf("%d",&n);
    	for (int i=0;i<n;i++){
    		scanf(" %c %d",&w[i],&d[i]);
    	}
    	scanf("\n");
    	tp1=1;
    	lt1=0;
    	tp2=1;
    	lt2=0;
    	for (int i=0;i<n;i++){
    		if (w[i]=='O'){
    			lt1=max(lt2,lt1+abs(tp1-d[i]))+1;
    			tp1=d[i];
    		} else {
    			lt2=max(lt1,lt2+abs(tp2-d[i]))+1;
    			tp2=d[i];
    		}
    	}
    	printf("Case #%d: %d\n",ti+1,max(lt1,lt2));
    }
    return 0;
}









