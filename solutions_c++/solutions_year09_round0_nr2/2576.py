#include<vector>
#include<list>
#include<map>
#include<set>
#include<deque>
#include<queue>
#include<stack>
#include<algorithm>
#include<functional>
#include<utility>
#include<sstream>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdio>
#include<ctime>
#include<string>
using namespace std;
struct node{
	int at;
	int b;
	int p;
	int i;
	int j;
};
vector<node>rs[10005];
int s[][2]={-1,0,0,-1,0,1,1,0};
 int m,n;
bool isok(int i,int j)
{
	return i<m&&i>=0&&j<n&&j>=0;
}
int main() 
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
    int t;
	cin>>t;
    int i,j,kth=1;
	while(t--)
	{ 
      int k=0;
	  node a[101][101];
	  char re[101][101];
	  cin>>m>>n;
	  for(i=0;i<m;i++)
	    for(j=0;j<n;j++)
		{
			cin>>a[i][j].at;
			a[i][j].b=k++;
			a[i][j].p=-1;
			a[i][j].i=i;
			a[i][j].j=j;
	     }
		for(i=0;i<k;i++)
			rs[i].clear();
		for(i=0;i<m;i++)
			 for(j=0;j<n;j++)
				 rs[a[i][j].b].push_back(a[i][j]);

       for(i=0;i<m;i++)
		   for(j=0;j<n;j++)
		   {
			  int mmin=10000000,b;
              for(k=0;k<4;k++)
			  {
				  int ii,jj;
				  ii=i+s[k][0];
				  jj=j+s[k][1];
				  if(isok(ii,jj)&&a[ii][jj].at<mmin&&a[ii][jj].at<a[i][j].at) 
				  {
					  mmin=a[ii][jj].at;
					  b=a[ii][jj].b;
				  }
			  }
              if(mmin!=10000000)
			  {
				  int nb=a[i][j].b;
				  for(k=0;k<rs[b].size();k++)
				  {
					  a[rs[b][k].i][rs[b][k].j].b=nb;
					  rs[nb].push_back(rs[b][k]);
				  }
				  rs[b].clear();
			   }
		   }
			 
	     int f=0;
		 for(i=0;i<m;i++)
             for(j=0;j<n;j++)
			 {
				 if(a[i][j].p==-1)
				 {
				     int w=a[i][j].b;
			    	 for(k=0;k<rs[w].size();k++)
				     {
					    re[rs[w][k].i][rs[w][k].j]=f+'a';
						a[rs[w][k].i][rs[w][k].j].p=1;
					 }  
					 f++;
				 }
			 }

      printf("Case #%d:\n",kth++);
	  for(i=0;i<m;i++)
		  for(j=0;j<n;j++)
		  {
			  if(j==n-1)
			      printf("%c\n",re[i][j]);
			  else
                  printf("%c ",re[i][j]);
		  }
	} 
	return 0;
}

