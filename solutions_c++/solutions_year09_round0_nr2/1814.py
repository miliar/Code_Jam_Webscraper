#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime> 
#define MAX 101

using namespace std;
stringstream stream;
int point[MAX][MAX];
char flag[MAX][MAX];
int flowTo[MAX][MAX];
          /*North,West,East,South*/
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};


void prime(int H,int W)
{
	int i=0,j=0,k=0;
	queue<int> que;
	for(i=0;i<H;i++)
		for(j=0;j<W;j++)
		{
			if(flag[i][j]!=0)
			{
				que.push(i);
				que.push(j);
			}
		}
	bool update=true;
	while(!que.empty())
	{
		int x=que.front();
		que.pop();

		int y=que.front();
		que.pop();
		
		for(i=0;i<4;i++)
		{
			int dtx=x+dx[i];
			int dty=y+dy[i];
			if(dtx>=0&&dtx<H&&dty>=0&&dty<W&&flag[dtx][dty]==0)
			{
				if(dx[flowTo[dtx][dty]]==-dx[i]&&dy[flowTo[dtx][dty]]==-dy[i])
				{
					flag[dtx][dty]=flag[x][y];
					que.push(dtx);
					que.push(dty);
				}
				
			}
		}
	}

}

int main()
{
	freopen("large.in","r",stdin);
	freopen("large.out","w",stdout);

	int Case=0;
	int i=0,j=0,k=0;
	int T=0,H=0,W=0;
	string s;


	getline(cin,s);
	stream<<s;
	stream>>T;

	while(Case<T)
	{
		
		for(i=0;i<MAX;i++)
			for(j=0;j<MAX;j++)
			{
				point[i][j]=0;
				flag[i][j]=0;
				flowTo[i][j]=-1;
			}


		getline(cin,s);
		stream.clear();
		stream.str(s);
		stream>>H>>W;
		


		for(i=0;i<H;i++)
		{
			getline(cin,s);
			stream.clear();
			stream.str(s);
			
			for(j=0;j<W;j++)
			{
				stream>>point[i][j];
			}
	
		}

		int baseNum=1;

		for(i=0;i<H;i++)
			for(j=0;j<W;j++)
			{
				int min=point[i][j];
				for(k=0;k<4;k++)
				{
					int tdx=i+dx[k];
					int tdy=j+dy[k];
					

					if(tdx>=0&&tdx<H&&tdy>=0&&tdy<W)
					{
						if(point[tdx][tdy]<min)
						{
							min=point[tdx][tdy];
							flowTo[i][j]=k;
						}
					}
				}
				if(flowTo[i][j]==-1)
				{
					flag[i][j]=baseNum;
					baseNum++;
				}
			}
			
			prime(H,W);
			



			char A[27];
			char now='a';

			for(i=0;i<27;i++)
				A[i]=0;
			
			for(i=0;i<H;i++)
				for(j=0;j<W;j++)
				{
					int temp=flag[i][j];
					if(temp>=1&&temp<=26&&A[temp]==0)
					{	
						A[temp]=now;

						for(int ii=0;ii<H;ii++)
							for(int jj=0;jj<W;jj++)
								if(flag[ii][jj]==temp)flag[ii][jj]=now;

						now++;
					}

				}
			Case++;
			cout<<"Case #"<<Case<<":"<<endl;
			for(i=0;i<H;i++)
			{
				for(j=0;j<W;j++)
				{
					cout<<flag[i][j]<<" ";
				}
				cout<<endl;
			}
	}
	return 0;
}