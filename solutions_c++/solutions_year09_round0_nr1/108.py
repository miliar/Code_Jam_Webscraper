#include<iostream>
#include<cstdio>
using namespace std;
int l,d,n;
bool check(char a[500],char dw[19])
{
  int i,p;
  bool flag=true,mf;
  char tmp;
  p=0;
  for(i=0;i<l;i++)
  {
    tmp=dw[i];
    if(a[p]=='(')
    {
      mf=false;
      p++;
      while(a[p]!=')')
      {
	if(a[p]==tmp)
	{
	  mf=true;
	  break;
	}
	p++;
      }
      while(a[p]!=')')
	p++;
      p++;
      if(mf==false)
      {
	flag= false;
	break;
      }
    }
    else
    {
      if(tmp!=a[p])
      {
	flag = false;
	break;
      }
      p++;
    }
  }
  return flag;
}
int main()
{
  int i;
  char dic[5009][19];
  scanf("%d",&l);
  scanf("%d",&d);
  scanf("%d",&n);
  for(i=1;i<=d;i++)
  {
    cin>>dic[i];
  }
  int t,cnt;
  char word[500];
  for(t=1;t<=n;t++)
  {
    printf("Case #%d: ",t);
    cnt=0;
    cin>>word;
    for(i=1;i<=d;i++)
    {
      if(check(word,dic[i]))
	cnt++;
    }
    printf("%d\n",cnt);
    
  }
  return 0;
}