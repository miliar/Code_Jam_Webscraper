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
int tt,ti,c,d,a,n;
string s;
string mf[1000];
string op[1000];
char st[1000];

int main(){
	#ifdef home
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    #endif
    cin>>tt;
    for (int ti=0;ti<tt;ti++){
    	cin>>c;
    	for (int i=0;i<c;i++)
    		cin>>mf[i];
    	cin>>d;
    	for (int i=0;i<d;i++){
    		cin>>op[i];
    		assert(op[i][0]!=op[i][1]);
    	}
    	cin>>n;
    	cin>>s;
    	a=0;
    	for (int i=0;i<n;i++){
    		st[a++]=s[i];
    		if (a>=2){    			
    			for (int j=0;j<c;j++) 
    				if ((mf[j][0]==st[a-2] && mf[j][1]==st[a-1])||(mf[j][1]==st[a-2] && mf[j][0]==st[a-1])){
    					a-=2;
    					st[a++]=mf[j][2];
    					break;
    				}
    		}
    		if (a>=2){    			
    			for (int j=0;j<d;j++) 
    				for (int p1=0;p1<a;p1++)
    					for (int p2=0;p2<a;p2++) if (p1!=p2){
    						if (st[p1]==op[j][0] && st[p2]==op[j][1]){
    							a=0;    							
    						}
    					}	
    		}
    	}
    	printf("Case #%d: ",ti+1);
    	printf("[");
    	for (int i=0;i<a-1;i++)
    		printf("%c, ",st[i]);
    	if (a>0)
	    	printf("%c",st[a-1]);
    	printf("]\n");
    }
    return 0;
}









