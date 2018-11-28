#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cmath>
#include<list>
#include<queue>
#include<cctype>
#include<stack>
#include<map>
#include<set>
#define black 0
#define gray 1
#define white 2
#define inf 2147483647
using namespace std;
void bfs_label(vector<vector<int> > & v,int s,vector <int> & d, vector<int> & prev,vector <int> & colour,char l,vector <char> & label)
{
        //vector<int> colour(v.size(),white);
        //prev.assign(prev.size(),-1);
        //d.assign(d.size(),inf);
        colour[s]=gray;
        d[s]=0;
        queue<int> q;
        q.push(s);
        while(!q.empty())
        {
                int u=q.front();
                q.pop();
                for(vector<int>::iterator it=v[u].begin();it!=v[u].end();it++)
                {
                        if(colour[*it]==white)
                        {
                                colour[*it]=gray;
                                d[*it]=d[u]+1;
                                prev[*it]=u;
                                q.push(*it);
                        }
                }
                colour[u]=black;
		label[u]=l;
	}
}



int main()
{
	int t;
	cin>>t;
	int arr[100][100];
	char ans[100][100];
	for(int count=1;count<=t;count++)
	{
		int m,n;
		cin>>m>>n;
		for(int i=0;i<m;i++)
			for(int j=0;j<n;j++)
				cin>>arr[i][j];
		vector<vector<int> > graph(m*n);
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n;j++)
			{
				vector<pair<int,int> > s;
				if(i>0 && arr[i-1][j]<arr[i][j])
					s.push_back(make_pair(arr[i-1][j],-n));
				if(j>0 && arr[i][j-1]<arr[i][j])
					s.push_back(make_pair(arr[i][j-1],-1));
				if(j<n-1 && arr[i][j+1] <arr[i][j])
					s.push_back(make_pair(arr[i][j+1],1));
				if(i<m-1 && arr[i+1][j]<arr[i][j])
					s.push_back(make_pair(arr[i+1][j],n));
				if(s.size()>0)
				{
					sort(s.begin(),s.end());
					/*if(i==1 &&  j==1)
					{
						for(int i=0;i<s.size();i++)
						{
							cout<<s[i].first<<" "<<s[i].second<<endl;
						}
					}*/
					graph[i*n+j].push_back(i*n+j+s[0].second);
					graph[i*n+j+s[0].second].push_back(i*n+j);
				}
				
			}

		}
		/*for(int i=0;i<graph.size();i++)
		{
			for(int j=0;j<graph[i].size();j++)
			{
				cout<<graph[i][j]<<" ";
			}
			cout<<endl;
		}*/
		vector<int> d(graph.size(),inf),colour(graph.size(),white),prev(graph.size(),-1);
		vector<char> label(graph.size());
		char l='a';
		for(int i=0;i<graph.size();i++)
		{
			if(colour[i]==white)
			{
				bfs_label(graph,i,d,prev,colour,l,label);
				l++;
			}
		}
		for(int i=0;i<label.size();i++)
		{
			ans[i/n][i%n]=label[i];	
		}
		cout<<"Case #"<<count<<":"<<endl;
		for(int i=0;i<m;i++)
		{
			for(int j=0;j<n-1;j++)
				cout<<ans[i][j]<<" ";
			cout<<ans[i][n-1]<<endl;
		}
			
	}
	return 0;
}
