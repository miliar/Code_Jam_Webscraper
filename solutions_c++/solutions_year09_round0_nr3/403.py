#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;

char str[1000];
char p[]="welcome to code jam";
int mat[2][1000];
int main(void)
{
	freopen("C-large.in","r",stdin);
	freopen("CSL.out","w",stdout);
	int cas=0;
	int tn;
	scanf("%d",&tn);
	getchar();
	while(tn--)
	{
	gets(str);
	int s,t;
	memset(mat,0,sizeof(mat));
	int len=strlen(str);
	s=0,t=1;
	for(int i=0;i<len;i++)
		if(str[i]=='w')
		    mat[s][i+1]=1;
    for(int i=1;i<=len;i++)
    	mat[s][i]=(mat[s][i]+mat[s][i-1])%10000;
 /*	for(int i=0;i<len;i++)
 		printf("%d ",mat[s][i]);
	cout<<endl;*/
	for(int i=1;i<19;i++)
	{
	//	cout<<p[i]<<endl;
		for(int j=1;j<=len;j++)
		{
			if(str[j-1]==p[i])
			{
			    mat[t][j]=mat[s][j-1];	
			}
		}
		s=1-s;
		t=1-t;
		for(int j=1;j<=len;j++)
		{
			mat[s][j]=(mat[s][j-1]+mat[s][j])%10000;
		}
		for(int j=0;j<=len;j++)
		{
			mat[t][j]=0;
		//	printf("%d ",mat[s][j]);
		}
		//printf("\n");
	}
	printf("Case #%d: %04d\n",++cas,mat[s][len]);
	}
	return 0;
}
