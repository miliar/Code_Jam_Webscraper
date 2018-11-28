#include<iostream>
#include<vector>
using namespace std;
class node
{
	public:
		int vis;
		vector<int> adj;
		node()
		{
			vis=-1;
		}
	
};
void DFS(int ind,int val,node vertex[])
{
	if(vertex[ind].vis != -1)
		return;
	vertex[ind].vis=val;
	for(int i=0;i<vertex[ind].adj.size();i++)
	{
		DFS(vertex[ind].adj[i],val,vertex);
	}
}

int main()
{
int t;
cin>>t;
int k=1;
	while(k<=t)
	{
		int h,w;
		cin>>h>>w;
		int arr[h+2][w+2];
		for(int i=0;i<h+2;i++)
		{
			arr[i][0]=arr[i][w+1]=20000;
		}
		for(int i=0;i<w+2;i++)
		{
			arr[0][i]=arr[h+1][i]=20000;
		}
		for(int i=1;i<=h;i++)
		{
			for(int j=1;j<=w;j++)
				{
					cin>>arr[i][j];
				}
		}
		
		
		node vertex[h*w];
		for(int i=1;i<=h;i++)
		{

			for(int j=1;j<=w;j++)
				{
				
					if(arr[i-1][j]<arr[i][j] || arr[i+1][j]<arr[i][j] || arr[i][j-1]<arr[i][j] || arr[i][j+1]<arr[i][j] ){
						//NORTH
						int si=i-1;
						int sj=j;
						int min=arr[si][sj];
						
						//west
						
						if(arr[i][j-1]<min)
						{
							min=arr[i][j-1];
							si=i;
							sj=j-1;
												
						}
						//east
						if(arr[i][j+1]<min)
						{
							min=arr[i][j+1];
							si=i;
							sj=j+1;
												
						}
						//south
						if(arr[i+1][j]<min)
						{
							min=arr[i+1][j];
							si=i+1;
							sj=j;
												
						}
						si-=1;
						sj-=1;
						int ci=i-1;
						int cj=j-1;
						int ind1=w*si+sj;
						int ind2=w*ci+cj;
						vertex[ind1].adj.push_back(ind2);
						vertex[ind2].adj.push_back(ind1);
				}				
					
				}
		}
		
		int c=0;
		for(int i=0;i<h*w;i++)
		{
			if(vertex[i].vis == -1)
			{
			DFS(i,c,vertex);
			c++;
			}
		}
		
		
		cout<<"Case #"<<k<<":"<<"\n";
		for(int i=0;i<h;i++)
		{
			for(int j=0;j<w;j++)
			{
				cout<<(char)('a'+vertex[w*i+j].vis)<<" ";
			}
			cout<<"\n";
		}
		k++;	
	}
}
