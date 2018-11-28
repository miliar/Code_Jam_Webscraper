#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<memory.h>
#include<algorithm>
using namespace std;
int main()
{
  int ca,i,j,c,d,n,len,total=0,ok;
  int g[30][30];
  FILE *f;
  char s[110],ans[110],t[30][30],s1[110];
  scanf("%d",&ca);
  f=fopen("B_small.out","w");
  while(ca--)
  {
	total++;
	for(i=0;i<30;i++) for(j=0;j<30;j++) t[i][j]='?';
	scanf("%d",&c);
	for(i=1;i<=c;i++)
	{
	  scanf("%s",s);
	  t[s[0]-'A'][s[1]-'A']=t[s[1]-'A'][s[0]-'A']=s[2];
	}
	memset(g,0,sizeof(g));
	scanf("%d",&d);
	for(i=1;i<=d;i++)
	{
	  scanf("%s",s);
	  g[s[0]-'A'][s[1]-'A']=g[s[1]-'A'][s[0]-'A']=1;
	}
	scanf("%d%s",&n,s);
	strcpy(ans,"");
	for(i=0;i<n;i++)
	{
	  len=strlen(ans);
	  ans[len]=s[i];
	  ans[len+1]='\0';
	  ok=1;
	  while(ok)
	  {
		
		ok=0;
	    strcpy(s1,ans);
        len=strlen(s1);
		if(len>1 && t[s1[len-1]-'A'][s1[len-2]-'A']!='?')
		{
		  ans[len-2]=t[s1[len-1]-'A'][s1[len-2]-'A'];
		  ans[len-1]='\0';
		  ok=1;
		  continue;
		}
		for(j=0;j<=len-2;j++)
	    if(g[s1[len-1]-'A'][s1[j]-'A']==1)
		{
		  ans[0]='\0';
		  ok=1;
		  break;
		}
	  }
	}

	//printf("ans=%s\n",ans);system("pause");
	if(strcmp(ans,"")==0) fprintf(f,"Case #%d: []\n",total);
	else
	{
	  fprintf(f,"Case #%d: [%c",total,ans[0]);
	  len=strlen(ans);
	  for(i=1;i<len;i++) fprintf(f,", %c",ans[i]);
	  fprintf(f,"]\n");
	}
  }
  system("pause");
  return 0;
}

