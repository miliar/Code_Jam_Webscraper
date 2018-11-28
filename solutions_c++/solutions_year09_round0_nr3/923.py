#include <cstdio>
#include <cstring>
using namespace std;
const char gcj[]="welcome to code jam";

int f[1000][30];
int n,len;
char bl[10],s[1000];

int main() {
    scanf("%d",&n);
    gets(bl);
    for (int kk=1;kk<=n;kk++) {
        gets(s);
        len=strlen(s);
    	for (int i=0;i<len;i++)
    		if (s[i]=='w') f[i][0]=1; else f[i][0]=0;
		for (int j=1;j<=18;j++) {
		    for (int i=0;i<len;i++) {
		        f[i][j]=0;
		        if (s[i]==gcj[j]) {
		            for (int p=0;p<i;p++) {
		                if (s[p]==gcj[j-1]) f[i][j]=(f[i][j]+f[p][j-1])%10000;
		            }    
		        }    
		    }    
		}    
		int ans=0;
		for (int i=0;i<len;i++) ans=(ans+f[i][18])%10000;
		printf("Case #%d: %04d\n",kk,ans);
    }    
}    
