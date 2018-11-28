#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string>VS;
struct tree_inter_node
{
	int value;
	int changeable;//0 or  1 and
}tree[100];
int answer[100][2];
int Min(int a,int b)
{
	return a<b?a:b;
}
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	int i,Case,num,n,ans,v;
	cin>>Case;
	num=1;
	while (Case--)
	{
		cin>>n>>v;
        ans=0;	
		for(i=1;i<=n;i++)
		{
			answer[i][0]=answer[i][1]=0;
		}
		for(i=1;i<=(n-1)/2;i++)
		{
			cin>>tree[i].value>>tree[i].changeable;
		}
		for(i=(n-1)/2+1;i<=n;i++)
		{
			cin>>tree[i].value;
			answer[i][tree[i].value]=1;
		}		
		for(i=(n-1)/2;i>0;i--)
		{
			if(tree[i].value==0)//or
			{
				int t1,t2;
				if(answer[i*2][1]>0)
					t1=answer[i*2][1];
				if(answer[i*2+1][1]>0)
					t2=answer[i*2+1][1];
				if(t1>0)
				{					 
					answer[i][1]=t1;
					if(t2<t1)
						answer[i][1]=t2;
				}
				else if(t2>0)
					answer[i][1]=t2;
				if(answer[i*2][0]>0&&answer[i*2+1][0]>0)  
				{
					answer[i][0]=answer[i*2][0]+answer[i*2+1][0]-1;
				}
				if(tree[i].changeable==1)
				{
					if(answer[i*2][0]>0)
						t1=answer[i*2][0];
					if(answer[i*2+1][0]>0)
						t2=answer[i*2+1][0];
					if(t1>0)
					{					 
						answer[i][0]=t1+1;
						if(t2<t1)
							answer[i][0]=t2+1;
					}
					else if(t2>0)
						answer[i][0]=t2+1;
				}
			}
			else//and
			{
				int t1,t2;
				if(answer[i*2][0]>0)
					t1=answer[i*2][0];
				if(answer[i*2+1][0]>0)
					t2=answer[i*2+1][0];
				if(t1>0)
				{					 
					answer[i][0]=t1;
					if(t2<t1)
						answer[i][0]=t2;
				}
				else if(t2>0)
					answer[i][0]=t2;
				if(answer[i*2][1]>0&&answer[i*2+1][1]>0)  
				{
					answer[i][1]=answer[i*2][1]+answer[i*2+1][1]-1;
				}
				if(tree[i].changeable==1)
				{
					if(answer[i*2][1]>0)
						t1=answer[i*2][1];
					if(answer[i*2+1][1]>0)
						t2=answer[i*2+1][1];
					if(t1>0)
					{					 
						answer[i][1]=t1+1;
						if(t2<t1)
							answer[i][1]=t2+1;
					}
					else if(t2>0)
						answer[i][1]=t2+1;
				}			      
			}
		}	 
		for(i=1;i<=(n-1)/2;i++)
		{
		  cout<<answer[i][0]<<" "<<answer[i][1]<<endl;
		}
		for(;i<=n;i++)
		{
		  cout<<tree[i].value<<endl;
		}
		if(answer[1][v]==0)
		{
			printf("Case #%d: IMPOSSIBLE\n",num++);	
		}
		else
		{
			printf("Case #%d: %d\n",num++,answer[1][v]-1);		  
		}
	}
	return 0; 
}