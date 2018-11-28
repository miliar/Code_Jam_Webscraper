#include<iostream>
#include<cstdio>
#include<cstring>
#define getc getchar_unlocked
using namespace std;

void gstr(char *a)
{
  int p=0;
  a[p]=' ';
  while(a[p]!=' '&&a[p]!='\n');
    a[p]=getc();
  do
  {
    p++;
    a[p]=getc();
  }while(a[p]!='\n');
  a[p]='\0';
}

int main()
{
  int t,tc,i,j,w,l;
  char ans[6];
  scanf("%d",&t);
  char text[609];
  int rec[609][25];
  char word[]={"welcome to code jam"};
  w=19;
  for(tc=1;tc<=t;tc++)
  {
    
    gstr(text);
    l=strlen(text);
    
    for(i=0;i<=l+9;i++)
    {
      for(j=0;j<=w+1;j++)
      {
        rec[l][i]=0;
      }
    }
    
    for(i=l-1;i>=0;i--)
    {
      for(j=0;j<w-1;j++)
      {
	rec[i][j]=rec[i+1][j];
	if(text[i]==word[j])
	{
	  rec[i][j]+=rec[i+1][j+1];
	  rec[i][j]%=10000;
	}
      }
      rec[i][w-1]=rec[i+1][w-1];
      if(text[i]==word[w-1])
      {
	rec[i][w-1]++;
      }
      rec[i][w-1]%=10000;
    }
    ans[4]='\0';
    ans[3]='0' + rec[0][0]%10;
    rec[0][0]/=10;
    ans[2]='0' +rec[0][0]%10;
    rec[0][0]/=10;
    ans[1]='0' + rec[0][0]%10;
    rec[0][0]/=10;
    ans[0]= '0' + rec[0][0]%10;
    printf("Case #%d: %s\n",tc,ans);
  }
  return 0;
}