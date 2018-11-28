#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;


int main()
{
	ifstream fin("e:\\fl\\in.in");
	ofstream fout("e:\\fl\\out.out");
	int c,x[111],v[111];
	int can[111],val[111];
	fin>>c;
	for (int i=0;i<c;i++)
	{
		int res=0;
		memset(can,0,sizeof(can));
		memset(val,0,sizeof(val));
		int n,k,b,t;
		fin>>n>>k>>b>>t;
		for (int j=0;j<n;j++)
			fin>>x[j];
		for (int j=0;j<n;j++)
			fin>>v[j];
		int w=0;
		for (int j=n-1;j>=0;j--)
		{
			int gap = (b-x[j]);
			if (gap<=t*v[j])
			{
				w++;
				can[j]=1;
			}
		}
		if (w<k)
			fout<<"Case #"<<(i+1)<<": "<<"IMPOSSIBLE"<<endl;
		else
		{
			int q = k;
			for (int j=n-1;j>=0;j--)
			{
				if (can[j])
				{
					for (int h=j+1;h<n;h++)
					{
						if (!can[h])
						{
							res++;
						}
					}
					q--;
					if (!q)
						break;
				}
			}
			fout<<"Case #"<<(i+1)<<": "<<res<<endl;
		}
	}
	return 0;
}