#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

long long int compute(long long int n)
{
	if(n<3)
		return 0;
	long long int ans=1;
	ans=(n*(n-1)*(n-2))/6;
	return ans;
}

int main()
{
	long long int a[3][3];
	
	ifstream fin("1.txt");
	ofstream fout("2.txt");
	int cases;
	fin>>cases;
	long long int n,m,s,b,c,d,x,y;
	int p,q;
	for(int i=0;i<cases;i++)
	{
		for(int l=0;l<3;l++)
		{
			for(int o=0;o<3;o++)
			{
				a[l][o]=0;
			}
		}
		fin>>n>>s>>b>>c>>d>>x>>y>>m;
		p=x%3;
		q=y%3;
		a[p][q]++;
		for(int j=1;j<n;j++)
		{
			x=(s*x+b)%m;
			y=(c*y+d)%m;
			//cout<<x<<" "<<y<<endl;
			p=x%3;
			q=y%3;
			a[p][q]++;
		}
		long long int answer=0;
		for(int t=0;t<3;t++)
		{
			for(int r=0;r<3;r++)
			{
			//	cout<<a[t][r]<<" ";
				answer+=compute(a[t][r]);
			}
			//cout<<endl;
		}
		answer+= a[0][0]*a[1][1]*a[2][2];
		answer+= a[1][0]*a[2][1]*a[0][2];
		answer+= a[0][0]*a[2][1]*a[1][2];
		answer+= a[1][0]*a[0][1]*a[2][2];
		answer+= a[2][0]*a[0][1]*a[1][2];
		answer+= a[2][0]*a[1][1]*a[0][2];
		for(int u=0;u<3;u++)
		{
			answer+=a[u][1]*a[u][0]*a[u][2];
			answer+=a[0][u]*a[1][u]*a[2][u];
		}
		fout<<"Case #"<<i+1<<": "<<answer<<endl;
	}
	
	return 0;
}
