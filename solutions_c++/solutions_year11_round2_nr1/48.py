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
int tt,n;
ld f1,f2,f3,f4;
ld wp[1000];
ld op[1000];
ld oop[1000];
char a[1000][1000];
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&tt);
    for (int ti=0;ti<tt;ti++){
    	printf("Case #%d:\n",ti+1);
    	scanf("%d",&n);
    	for (int i=0;i<n;i++)
    		scanf("%s",a[i]);
    	for (int i=0;i<n;i++){
    		f1=0;
    		f2=0;
    		for (int j=0;j<n;j++) if (a[i][j]!='.'){
    			f2++;
    			if (a[i][j]=='1')
    				f1++;
    		}
    		wp[i]=f1*1.0/f2;
    	}
    	for (int i=0;i<n;i++){
    		f1=0;
    		f2=0;
    		for (int j=0;j<n;j++) if (a[i][j]!='.'){
    			f2++;
    			f3=0;
    			f4=0;
    			for (int k=0;k<n;k++) if (k!=i && a[j][k]!='.'){
    				f3++;
    				if (a[j][k]=='1'){
    					f4++;
    				}
    			}
    			f1+=f4*1.0/f3;
    		}
    		op[i]=f1*1.0/f2;
    	}
    	for (int i=0;i<n;i++){
    		f1=0;
    		f2=0;
    		for (int j=0;j<n;j++) if (a[i][j]!='.'){
    			f2++;
    			f1+=op[j];
    		}
    		oop[i]=f1*1.0/f2;
    	}
    	for (int i=0;i<n;i++)
    		printf("%.18lf\n",(double)(0.25*wp[i]+0.5*op[i]+0.25*oop[i]));
    }
    return 0;
}









