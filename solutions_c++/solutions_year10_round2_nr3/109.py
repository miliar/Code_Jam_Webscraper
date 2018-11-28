#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;

int mas[555][555],f[555][555];

int main()
{
	ifstream fin("e:\\fl\\in.in");
	ofstream fout("e:\\fl\\out.out");
	int t;
	fin>>t;
	int p = 100003;
	memset(mas,0,sizeof(mas));
	mas[0][0] = 1;
	for (int i=1;i<=500;i++)
		for (int j=0;j<=i;j++)
		{
			mas[i][j]=mas[i-1][j];
			if (j>0)
				mas[i][j]=(mas[i][j]+mas[i-1][j-1])%p;
		}

	int n=500;
	memset(f,0,sizeof(f));
	for (int j=2;j<=n;j++)
		f[j][1]=1;
	for (int j=2;j<=n;j++)
	{
		for (int h=2;h<j;h++)
		{
			f[j][h]=0;
			for (int d=j-1;d>=1;d--)
			{
				int temp = 1LL*f[h][d]*mas[j-h-1][h-d-1]%p;
				f[j][h]+=temp;
				f[j][h]%=p;
			}
		}
	}

	for (int i=0;i<t;i++)
	{
		fin >> n;
		int res = 0;
		for (int j=1;j<=n-1;j++)
		{
			res+=f[n][j];
			res%=p;
		}
		fout<<"Case #"<<(i+1)<<": "<<res<<endl;
	}
	return 0;
}