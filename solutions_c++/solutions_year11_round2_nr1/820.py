#include<stdio.h>
#include<stdlib.h>
#include<string.h>
double wp[110],owp[110],oowp[110],pri[110];
int win[110],lose[110];
char s[110][110];
int n;
void calwp()
{
  int i,j;
  memset(lose,0,sizeof(lose));
  memset(win,0,sizeof(win));
  for(i=1;i<=n;i++)
  {
	for(j=0;j<n;j++)
	if(s[i][j]=='0') lose[i]++;
	else if(s[i][j]=='1') win[i]++;
    
	wp[i]=(double)(win[i])/(lose[i]+win[i]);
  }
}

void calowp()
{
   int i,j,cnt=0;
   double sum;
   for(i=1;i<=n;i++)
   {
	 cnt=0;sum=0.0;
	 for(j=1;j<=n;j++)
	 if(i!=j && s[j][i-1]!='.')
	 {
	   if(s[j][i-1]=='1') sum+=(double)(win[j]-1)/(win[j]+lose[j]-1);
	   else sum+=(double)(win[j])/(win[j]+lose[j]-1);
	   cnt++;
	 }
	 owp[i]=sum/cnt;
   }
}

void caloowp()
{
   int i,j,cnt;
   double sum;
   for(i=1;i<=n;i++)
   {
	  sum=0.0;cnt=0;
	  for(j=1;j<=n;j++)
	    if(i!=j && s[j][i-1]!='.')
		{
	     sum+=owp[j];
		 cnt++;
		}
	  oowp[i]=sum/cnt;
   }
}
void calpri()
{
  int i;
  for(i=1;i<=n;i++)
  pri[i]=0.25*wp[i]+0.5*owp[i]+0.25*oowp[i];
}
int main()
{
	int ca,i,j,test=0;
	FILE *f;
	f=fopen("A.out","w");

	scanf("%d",&ca);
	while(ca--)
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++)
	    scanf("%s",s[i]);

		calwp();
		calowp();
		caloowp();
		calpri();
		fprintf(f,"Case #%d:\n",++test);
		for(i=1;i<=n;i++)
		fprintf(f,"%.7lf\n",pri[i]);
	}
	system("pause");
	return 0;
}
