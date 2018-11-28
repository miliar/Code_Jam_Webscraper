#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	for(int ca=0;ca<T;ca++)
	{
		vector <string> total;
		int n;
		fin >> n;
		for(int i=0;i<n;i++)
		{
			string temp;
			fin>>temp;
			total.push_back(temp);
		}
		double wp[110]={0},owp[110]={0},oowp[110]={0};
		int nrgames[100]={0};
		for(int i=0;i<n;i++)
		{
			int won=0,lost=0;
			for(int j=0;j<n;j++)
			{
				if (total[i][j]=='0')
				{
					lost++;
					nrgames[i]++;
				}
				if (total[i][j]=='1')
				{
					won++;
					nrgames[i]++;
				}
			}
			wp[i]=won*1.0/(won+lost);
		}
		for(int i=0;i<n;i++)
		{
			int count=0;
			for(int j=0;j<n;j++)
			{
				if (i!=j)
				{
					if (total[i][j]!='.')
					{
						if (total[j][i]=='1')
						{
							owp[i]+=((wp[j]*nrgames[j])-1)*1.0/(nrgames[j]-1);
						}
						else
						{
							owp[i]+=(wp[j]*nrgames[j])*1.0/(nrgames[j]-1);
						}
						count++;
					}
				}
			}
			owp[i]/=count;
		}
		for(int i=0;i<n;i++)
		{
			int count=0;
			for(int j=0;j<n;j++)
			{
				if (total[i][j]!='.')
				{
					oowp[i]+=owp[j];
					count++;
				}
			}
			oowp[i]/=count;
		}
		fout << "Case #" << ca+1 << ":\n";
		for(int i=0;i<n;i++)
			fout << 0.25*wp[i]+0.5*owp[i]+0.25*oowp[i] << "\n";
	}
	return 0;
}