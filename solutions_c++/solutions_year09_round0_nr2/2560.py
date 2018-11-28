#include <iostream>
#include <vector>
#include <functional>
#include <algorithm>
#include <climits>
#include <cmath>
#include <fstream>
using namespace std;
struct Node
{
	int h;
	char* val;
	Node* next;
};
int main()
{
//#ifndef LOCAL
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");
//#endif
	int T;
	cin>>T;
	for(int ii=1;ii<=T;ii++)
	{
		int H,W;
		cin>>H>>W;
		vector<vector<char> > final(H,vector<char>(W,'\0'));
		vector<vector<int> > basins(H,vector<int>(W));
		vector<vector<bool> > visited(H,vector<bool>(W,false));
		vector<int> heights;
		vector<vector<Node> >mp(H,vector<Node>(W));

		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				cin>>basins[i][j];
				heights.push_back(basins[i][j]);
				mp[i][j].h=basins[i][j];
				mp[i][j].val=&final[i][j];
				mp[i][j].next=NULL;
			}
		}
		sort(heights.begin(),heights.end(),greater<int>());
		for(int i=0;i<heights.size();)
		{
			for(int j=0;j<basins.size();j++)
			{
				for(int k=0;k<basins[j].size();k++)
				{
					if(basins[j][k]!=heights[i] || visited[j][k])continue;
					int x[4]={-1,0,0,1},y[4]={0,-1,1,0};
					int mn=INT_MAX;
					vector<int> cells(4,-1);
					for(int z=0;z<4;z++)
					{
						if(j+x[z]>=0 && j+x[z]<basins.size() && k+y[z]>=0 && k+y[z]<basins[j].size())
						{
							cells[z]=basins[j+x[z]][k+y[z]];
							mn=min(mn,basins[j+x[z]][k+y[z]]);
						}
					}
					if(mn<basins[j][k])
					{
						for(int z=0;z<4;z++)
						{
							if(mn==cells[z])
							{
								mp[j][k].next=&mp[j+x[z]][k+y[z]];
								break;
							}
						}
					}
					visited[j][k]=true;
					goto label;
				}
			}
label:
			i++;
		}
		char c='a';
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				Node* nd=&mp[i][j];
				bool flag=false;
				char ch=c++;
				while(nd!=NULL)
				{
					if(*nd->val!='\0' && *nd->val < ch )
					{
						ch=*nd->val;
						flag=true;
					}
					nd=nd->next;
				}
				if(flag)c--;
				nd=&mp[i][j];
				while(nd!=NULL)
				{
					*nd->val=ch;
					nd=nd->next;
				}
				
			}
		}
		cout<<"Case #"<<ii<<":"<<endl;
		for(int i=0;i<H;i++)
		{
			for(int j=0;j<W;j++)
			{
				cout<<final[i][j];
				if(j+1!=W)cout<<" ";
				else
					cout<<endl;
			}
		}
	}
	return 0;
}