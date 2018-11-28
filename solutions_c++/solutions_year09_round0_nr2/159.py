#include<stdlib.h>
#include<iostream>
#include<sstream>
#include<math.h>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<set>
#include<map>
#include<numeric>
#include<algorithm>
#include<stdio.h>

using namespace std;

#define for0(i,n) for((i)=0;(i)<(n);(i)++)
#define for1(i,n) for((i)=1;(i)<=(n);(i)++)
#define min2(a,b) (a)<(b)?(a):(b)
#define min3(a,b,c) ((a)<(b)?(a):(b))<(c)?((a)<(b)?(a):(b)):(c)
#define min4(a,b,c,d) min3(a,b,c)<d?min3(a,b,c):d
#define max2(a,b) (a)>(b)?(a):(b)
#define max3(a,b,c) ((a)>(b)?(a):(b))>(c)?((a)>(b)?(a):(b)):(c)
#define max4(a,b,c,d) max3(a,b,c)>d?max3(a,b,c):d

#define swap(a,b,t) t=a;a=b;b=t;

#define inf 1000000000
#define iss istringstream

#define vi vector<int>
#define vs vector<string>
#define vd vector<double>
#define ssc sscanf
#define sp sprintf
#define pb push_back
#define sortv(x) sort(x.begin(),x.end())

#define cname c
#define fname f
#define lvars  int l1=0,l2=0,l3=0,l4=0
#define tvars  int t1=0,t2=0,t3=0,t4=0

#define dec(c) (((c)>='0'&&(c)<=9))?((c)-'0'):(((c)>='a'&&(c)<='f')?(c)-'a'+10:(c)-'A'+10)
int m[110][110],h,w,bmap[110][110];
char lmap[110][110];

void traceb(int i,int j,char l)
{
	int x;
	if(i>0 && bmap[i-1][j]==4 && lmap[i-1][j]==0){lmap[i-1][j]=l;traceb(i-1,j,l);}
	if(i<h-1 && bmap[i+1][j]==1 && lmap[i+1][j]==0){lmap[i+1][j]=l;traceb(i+1,j,l);}
	if(j>0 && bmap[i][j-1]==3 && lmap[i][j-1]==0){lmap[i][j-1]=l;traceb(i,j-1,l);}
	if(j<w-1 && bmap[i][j+1]==2 && lmap[i][j+1]==0){lmap[i][j+1]=l;traceb(i,j+1,l);}
}

void trace(int i,int j,char l)
{
	int x;
	x=bmap[i][j];
	lmap[i][j]=l;
	traceb(i,j,l);
	if(x==1)i--;
	if(x==2)j--;
	if(x==3)j++;
	if(x==4)i++;
	if(x!=0)
		trace(i,j,l);
}

int main()
{
	int t,i,j,k,tc=1;
	cin>>t;
	while(t--)
	{
		cin>>h>>w;
		for(i=0;i<h;i++)for(j=0;j<w;j++)
		{
			cin>>m[i][j];
		}
		memset(bmap,0x1f,sizeof(bmap));
		memset(lmap,0,sizeof(lmap));
		for(i=0;i<h;i++)for(j=0;j<w;j++)
		{
			int me = m[i][j],d=0;
			if(i>0 && m[i-1][j]<me){me = m[i-1][j];d=1;}
			if(j>0 && m[i][j-1]<me){me = m[i][j-1];d=2;}
			if(j<w-1 && m[i][j+1]<me){me = m[i][j+1];d=3;}
			if(i<h-1 && m[i+1][j]<me){me = m[i+1][j];d=4;}
			bmap[i][j]=d;
		}

		char l='a';
		for(i=0;i<h;i++)for(j=0;j<w;j++)
		{
			if(lmap[i][j]=='\0')
			{
				trace(i,j,l++);
			}
		}

		cout<<"Case #"<<tc++<<":"<<endl;
		for(i=0;i<h;i++)
		{
			for(j=0;j<w-1;j++)
			{
				cout<<lmap[i][j]<<" ";
			}
			cout<<lmap[i][j]<<endl;
		}

		
	}
	return 0;
}