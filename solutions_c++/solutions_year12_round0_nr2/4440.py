//This code was writen by Alexander Dryapko (sdryapko)
#include<sstream>
#include<iostream>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<map>                             	
#include<set>               
#include<string>
#include<string.h>  
#define gcd(a,b) __gcd((a),(b));
#define sqr(a) ((a)*(a))
#define odd(a) ((a)&1)
#define pw2(x) (1ll<<(x))
#define F first
#define S second
const int maxi=2000000000;              
const int maxq=1000000000;
const double eps=1e-10;       
const double pi=3.1415926535897932;
const double inf=1e+18;
const int mo=1000000007;

using namespace std;
int n,surprise,mark,tt,a;
int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout); 
        scanf("%d",&tt);
        for (int t=1;t<=tt;t++) {
        	scanf("%d%d%d",&n,&surprise,&mark);
                int ans=0;
                int mark1,mark2,mark3;
        	for (int i=1;i<=n;i++) {
        		scanf("%d\n",&a);
        		if (a%3==0) {
        			mark1=a/3;
        			mark2=a/3;
        			mark3=a/3;
        		}
        		if (a%3==1) {
        			mark1=a/3;
        			mark2=a/3;
        			mark3=a/3+1;
        		}
        		if (a%3==2) {
        			mark1=a/3;
        			mark2=a/3+1;
        			mark3=a/3+1;
        	        }

        	        if (mark3>=mark) ans++; else if (surprise&&a>=mark) {
        	        	if (a%3==0&&a/3+1>=mark) ans++,surprise--;
        	        	if (a%3==2&&mark3+1>=mark) ans++,surprise--;
        	        }
        	
        	}
        	printf("Case #%d: %d\n",t,ans);
        }
       	return 0;
}
