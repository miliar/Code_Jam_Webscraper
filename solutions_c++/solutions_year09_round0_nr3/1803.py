#include<iostream>
#include<stdio.h>
#include<string.h>
#include<map>
#include<queue>
#include<algorithm>
using namespace std;
char text[]="welcome to code jam";
int main(){
	
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	 int tt,ii;
	 char str[10005];
	 int tlen=strlen(text);
	 scanf("%d",&tt);
	 getchar();
	 for(ii=1;ii<=tt;ii++)
	 {
		 gets(str);
		 printf("Case #%d: ",ii);
		 int slen=strlen(str);
		 
		 int i,mod=10000;
	     int  a[25];
		memset(a,0,sizeof(a));
		 for(i=slen-1;i>=0;i--)
		 {
            if(str[i]=='w')
			
				a[1]=(a[1]+a[2])%mod;
			
			else if(str[i]=='e')
			{
				a[2]=(a[2]+a[3])%mod;
				a[7]=(a[7]+a[8])%mod;
				a[15]=(a[15]+a[16])%mod;
			}
			else if(str[i]=='l')
				a[3]=(a[3]+a[4])%mod;
			else if(str[i]=='c')
            {
				a[4]=(a[4]+a[5])%mod;
                a[12]=(a[12]+a[13])%mod;
			}
			else if(str[i]=='o')
			{
				a[5]=(a[5]+a[6])%mod;
				a[10]=(a[10]+a[11])%mod;
				a[13]=(a[13]+a[14])%mod;
			}
			else if(str[i]=='m')
			{
				a[6]=(a[6]+a[7])%mod;
				a[19]=(a[19]+1)%mod;
			}
			else if(str[i]==' ')
			{
				a[8]=(a[8]+a[9])%mod;
				a[11]=(a[11]+a[12])%mod;
				a[16]=(a[16]+a[17])%mod;
			}
			else if(str[i]=='t')
			{
				a[9]=(a[9]+a[10])%mod;
			}
			else if(str[i]=='d')
				a[14]=(a[14]+a[15])%mod;
			else if(str[i]=='j')
				a[17]=(a[17]+a[18])%mod;
			else if(str[i]=='a')
				a[18]=(a[18]+a[19])%mod;
		 }
	     
		 if(a[1]>=mod)
             a[1]%=mod;
		 printf("%04d\n",a[1]);
	 }
	 return 0;
}
