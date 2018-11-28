#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<map>
#include<string>
#include<algorithm>
#include<queue>
#include<iostream>
using namespace std;

struct T
{
  string a;
  int depth;
};

const int debug[]={341,312,261,191,119,58,22,8,3,1};
map <string,int> P;
T tmp;
string a,Tmp;
int cnt,N;
int r,c,d,t;
int Cnt;
int father[1000001];
bool b[201];
queue <T> Q;
int Num=0;

void bfs(int x)
{
  b[x]=true;
  Num++;
  if(!b[x+1]&&(a[x+1]=='w'||a[x+1]=='o')&&((x+1)%c))
    bfs(x+1);
  if(!b[x-1]&&(a[x-1]=='w'||a[x-1]=='o')&&(x%c))
    bfs(x-1);
  if(!b[x-c]&&(a[x-c]=='w'||a[x-c]=='o')&&(x/c))
    bfs(x-c);
  if(!b[x+c]&&(a[x+c]=='w'||a[x+c]=='o')&&(x<(r-1)*c))
    bfs(x+c);
}

bool check(int x)
{
  if(a[x]=='x'||a[x]=='.')
    return true;
  else
    return false;
}

void move(int x,int p)
{
  if(p==1)
  {
    if(a[x-c]=='x')
      a[x-c]='w';
    else
      a[x-c]='o';
    if(a[x]=='w')
      a[x]='x';
    else
      a[x]='.';
  }
  if(p==2)
  {
    if(a[x+1]=='x')
      a[x+1]='w';
    else
      a[x+1]='o';
    if(a[x]=='w')
      a[x]='x';
    else
      a[x]='.';
  }
  if(p==3)
  {
    if(a[x+c]=='x')
      a[x+c]='w';
    else
      a[x+c]='o';
    if(a[x]=='w')
      a[x]='x';
    else
      a[x]='.';
  }
  if(p==4)
  {
    if(a[x-1]=='x')
      a[x-1]='w';
    else
      a[x-1]='o';
    if(a[x]=='w')
      a[x]='x';
    else
      a[x]='.';
  }
}

void Push(int x,int flag)
{
  Cnt=P[a];
  if(x>=c&&x<(r-1)*c)
    if(check(x-c)&&check(x+c))
    { 
      move(x,1);
      Num=N;
      if(flag)
      {
        Num=0;
	memset(b,0,sizeof(b));
        bfs(x-c);
      }
      if(!P[a]&&Num>=N)
      {
	P[a]=++cnt;
	father[cnt]=Cnt;
	tmp.a=a;
	tmp.depth=d+1;
        Q.push(tmp);
      }
      move(x-c,3);
      move(x,3);
      Num=N;
      if(flag)
      {
	Num=0;
	memset(b,0,sizeof(b));
	bfs(x+c);
      }
      if(!P[a]&&Num>=N)
      {
	P[a]=++cnt;
	father[cnt]=Cnt;
	tmp.a=a;
	tmp.depth=d+1;
        Q.push(tmp);
      }
      move(x+c,1);
    }
  if((x%c)&&((x+1)%c))
    if(check(x-1)&&check(x+1))
    {
      move(x,2);
      Num=N;
      if(flag)
      {
	Num=0;
	memset(b,0,sizeof(b));
	bfs(x+1);
      }
      if(!P[a]&&Num>=N)
      {
	P[a]=++cnt;
	father[cnt]=Cnt;
	tmp.a=a;
	tmp.depth=d+1;
        Q.push(tmp);
      }
      move(x+1,4);
      move(x,4);
      Num=N;
      if(flag)
      {
	Num=0;
	memset(b,0,sizeof(b));
	bfs(x-1);
      }
      if(!P[a]&&Num>=N)
      {
	P[a]=++cnt;
	father[cnt]=Cnt;
	tmp.a=a;
	tmp.depth=d+1;
        Q.push(tmp);
      }
      move(x-1,2);
    }
  return;
}

int main()
{
  freopen("Gcj_A.in","r",stdin);
  freopen("Gcj_A.out","w",stdout);
  scanf("%d",&t);
  for(int num=1;num<=t;num++)
  {
    a="";
    while(!Q.empty())
      Q.pop();
    bool flag=false;
    cnt=0;
    string end="";
    printf("Case #%d: ",num);
    P.clear();
    scanf("%d%d",&r,&c);
    for(int i=0;i<r;i++)
    {
      cin>>Tmp;
      a+=Tmp;
    }
    P[a]=++cnt;
    tmp.a=a;
    tmp.depth=0;
    Q.push(tmp);
    end=a;
    N=0;
    for(int i=0;i<r*c;i++)
      if(a[i]=='o'||a[i]=='w')
	N++;
    for(int i=0;i<r*c;i++)
    {
      if(a[i]=='x')
	end[i]='w';
      else
	if(a[i]=='o')
	  end[i]='.';
    }
    while(!Q.empty())
    {
      a=Q.front().a;
      d=Q.front().depth;
/*      for(int i=0;i<r*c;i++)
      {
	cout<<a[i];
	if((i+1)%c==0)
	  cout<<endl;
      }
      cout<<P[a]<<endl;*/
      if(a==end)
      {
	printf("%d\n",d);
	flag=true;
      }
      if(flag)
	break;
      Q.pop();
      Num=0;
      for(int i=0;i<r*c;i++)
	if(a[i]=='w'||a[i]=='o')
	{
	  memset(b,0,sizeof(b));
	  bfs(i);
	  break;
	}
      int Flag;
      if(Num<N)
	Flag=1;
      else
	Flag=0;
      for(int i=0;i<r*c;i++)
      {
        if(a[i]=='w'||a[i]=='o') 
	  Push(i,Flag);
      }
    }
    if(!flag)
      puts("-1");
  }
  return 0;
}


