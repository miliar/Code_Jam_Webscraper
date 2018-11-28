#include<iostream>
#include<string>
using namespace std;
#define maxl 512
#define len 19
#define mod 10000

int N;
char p[]=" welcome to code jam";
char str[maxl];
int f[maxl][len];
int ans;

int solve()
{ans=0;  f[0][0]=1;
    
  for(int i=0;i<strlen(str);i++)
   for(int j=0;j<=i;j++)
    for(int k=1;k<=len;k++)
     if(p[k]==str[i]){
      f[i][k]+=f[j][k-1];
      f[i][k]=f[i][k]%mod;
      }
   
 for(int i=0;i<strlen(str);i++)
  ans=ans+f[i][len];   

return ans;     
}

int main()
{
 scanf("%d", &N);
   gets(str);
  for(int i=1;i<=N;i++){
   gets(str);
      
    printf("Case #%d: %04d\n",i,solve());
     
      memset(f,0,sizeof(f));
    }
  
return 0;
}   
