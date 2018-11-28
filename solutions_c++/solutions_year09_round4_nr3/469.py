#include "stdafx.h"
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <algorithm>
#include <iostream>
#define PI 3.14159265358979323846264338327950288
#define _clr(a,b) memset(a,b,sizeof(a))
template<class T> T _abs(T a)
{ if(a<0) return -a;return a;}
template<class T> void get_min(T& a,T b)
{ if(a>b) a=b;}
template<class T> void get_max(T& a,T b)
{ if(a<b) a=b;}
using namespace std;
int point[30][30];
int k,n;
bool map[30][30];
int color[30]; 
int ans;
bool check(int position,int color_index)   
{   
    for(int i=0;i<n;i++)   
    {   
        if(map[position][i]&&color[i]==color_index) return false;   
    }   
    return true;   
}
bool check2(int m,int n)
{
	int pp=point[m][0]-point[n][0];
	if(pp>0) pp=1;
	else if(pp<0) pp=-1;
	for(int i=1;i<k;i++)
	{
		if((point[m][i]-point[n][i])*pp<=0) return false;
	}
	return true;
}
void DFS(int index,int used_color_num)   
{   
    if(used_color_num>=ans) return;   
    if(index==n)    
    {   
        ans=used_color_num;   
        return;   
    }   
    for(int i=1;i<=used_color_num;i++)   
    {   
        if(check(index,i))   
        {   
            color[index]=i;   
            DFS(index+1,used_color_num);   
            color[index]=0;   
        }   
    }   
    used_color_num++;   
    color[index]=used_color_num;   
    DFS(index+1,used_color_num);   
    color[index]=0;   
} 
int main()
{
	freopen("e:\\1.in","r",stdin);
	freopen("e:\\1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<k;j++)
			{
				scanf("%d",&point[i][j]);
			}
		}
		_clr(map,0);
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if(!check2(i,j))
				{
					map[i][j]=map[j][i]=true;
				}
			}
		}
		ans=50;
		_clr(color,0);
		DFS(0,0); 
		printf("%d\n",ans);
	}
	return 0;
}
