#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> T;
	/*double dyn[1010];
	dyn[0]=0;
	dyn[1]=0;
	dyn[2]=2;
	double help[11][11]={0};
	int fact[11]={0};
	fact[0]=1;
	for(int i=1;i<11;i++)
		fact[i]=fact[i-1]*i;
	for(int i=0;i<11;i++)
	{
		vector <int> tha;
		for(int j=0;j<i;j++)
			tha.push_back(j+1);
		for(int j=0;j<fact[i];j++)
		{
			int c=0;
			for(int k=0;k<i;k++)
				if (tha[k]==k+1)
					c++;
			help[c][i]+=1.0/fact[i];
			next_permutation(tha.begin(),tha.end());
		}
	}
	for(int i=3;i<11;i++)
	{
		double temp=0;
		for(int j=1;j<=i;j++)
		{
			temp+=help[j][i]*1.0*(dyn[i-j]+1);
		}
		temp+=help[0][i];
		temp/=(1.0-help[0][i]);
		dyn[i]=temp;
	}*/
	for(int ca=0;ca<T;ca++)
	{
		int n;
		fin >> n;
		int count=0;
		for(int i=0;i<n;i++)
		{
			int temp;
			fin >> temp;
			if (temp==i+1)
				count++;
		}
		fout << "Case #" << ca+1 << ": " << n-count << "\n";
	}
	return 0;

}