#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

const string pat="welcome to code jam";
char s[600];

int f[600][30];
int n,m;

int main(){
   freopen("C-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,num;
   while (		scanf("%d\n",&num)==1){
		m=pat.size();
		//printf("%d\n",m);
		foru(test,1,num) {
			gets(s);	
			memset(f,0,sizeof(f));
			printf("Case #%d: ",test);
			n=strlen(s);
			f[0][0]=1;
			foru(i,1,n){
				foru(j,0,m) f[i][j]=f[i-1][j];
				foru(j,1,m) if (pat[j-1]==s[i-1]) {
					f[i][j]+=f[i-1][j-1];
					f[i][j]=f[i][j] % 10000;
				}	
			}
		/*	foru(i,1,n) {
			  foru(j,1,m) printf("%d  ",f[i][j]);
			 	printf("\n"); 
			}*/
			printf("%04d\n",f[n][m]);
		}
	}
   
   return 0;
}
