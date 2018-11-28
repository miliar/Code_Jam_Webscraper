#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<fstream>
#include<string>
using namespace std;
#define shit 2048

const int CNT=1e7;
int ncoolnum,b[shit];
double data[shit];
int T;
double XieLv(int a,int b)
{
	return ((data[b]-data[a])/(b-a));
}
double Check1(int a,int b) 
{
	int xiao; 
	double cakit,bill;
	for(xiao=a+1;xiao<b;xiao++)
    if((cakit=XieLv(a,xiao))>=XieLv(a,b)) 
	{
      bill=data[a]-cakit*a;
      data[xiao]=cakit*xiao+bill;
      data[b]+=1;     
      return data[b];
    }
	for(xiao=b+1;xiao<=ncoolnum;xiao++)
    if((cakit=XieLv(a,xiao))>XieLv(a,b)) 
	{
      bill=data[a]-cakit*a;
      data[xiao]=cakit*xiao+bill;
      data[b]+=1;
      return data[b];
    }
  return -1;
}
int NumCheck() 
{
	for(int i=1;i<ncoolnum;i++)
	if(Check1(i,b[i])>0)
	return 1;
	return 0;
}
void solve(int fucknumnum)
{
	int i,cnt;
	cnt=0;
    memset(data,0,sizeof(data));
    scanf("%d",&ncoolnum);
    for(i=1;i<ncoolnum;i++)
    scanf("%d",&b[i]);
    while (cnt<CNT&&NumCheck()) 
	cnt++;
    printf("Case #%d: ",fucknumnum);
    if (cnt<CNT) 
	{
      for(i=1;i<=ncoolnum;i++)
      printf("%.0lf ",data[i]<0?-data[i]:data[i]);
      putchar(10);
    } 
	else 
	printf("Impossible\n");
}
int main() 
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
  	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	solve(i);
	return 0;
}