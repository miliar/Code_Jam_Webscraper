#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

struct point
{
	long long int x;int y;
}pt;

int main()
{
	int N;
	cin>>N;
	vector<point> trees;
	
	for(int i=1;i<=N;i++)
	{
		long long int n,A,B,C,D,x0,y0,M,X,Y;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;

		trees.clear();
		X = x0; Y = y0;
		pt.x = X; pt.y = Y;
		trees.push_back(pt);
		for(int j = 1; j<=n-1;j++)
		{
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
			pt.x = X; pt.y = Y;
			trees.push_back(pt);
  		}

		long long int ii,jj,kk,count=0;
		for(ii=0;ii<trees.size()-2;ii++)
			for(jj=ii+1;jj<trees.size()-1;jj++)
				for(kk=jj+1;kk<trees.size();kk++)
					if((trees[ii].x+trees[jj].x+trees[kk].x)%3==0 && (trees[ii].y+trees[jj].y+trees[kk].y)%3==0)
						count++;
				
		cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
