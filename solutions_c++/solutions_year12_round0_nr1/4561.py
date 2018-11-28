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
char s[1111],s1[1111],s2[1111],ss[1111],ss1[1111],ss2[1111],f[11111],a;
int n;
int main(){                 
        freopen("input.txt","r",stdin);      
        freopen("output.txt","w",stdout);
        for (int i='a';i<='z';i++) {
        	scanf("%c%c%c\n",&a,&a,&a);
               // cout<<a<<endl;
        	f[i]=a;
        }
        cin>>n;
        
        scanf("\n");
        for (int i=0;i<n;i++) {
        	gets(s);
        	int m=strlen(s);
        	for (int j=0;j<m;j++) if (s[j]>='a'&&s[j]<='z') s[j]=f[s[j]];
        	printf("Case #%d: ",i+1);
        	puts(s);
        }	
        return 0;
}
