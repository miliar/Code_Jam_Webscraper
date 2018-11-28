#include<iostream>
#include<conio.h>
#include<fstream>
#include<list>
#include<algorithm>
#include<vector>

using namespace std;
int n;
int m;

int main(void)
{
	int i,j;
	int temp;

	fstream fin("a.in",ios::in);
	fstream fout("output.txt",ios::out);

	fin>>n;

	for(int k=0;k<n;k++)
	{
		vector<int> a,b;

		fin>>m;
		for(i=0;i<m;i++)
		{
			fin>>temp;
			a.push_back(temp);
		}

		for(i=0;i<m;i++)
		{
			fin>>temp;
			b.push_back(temp);
		}

		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		int ans1=0,ans2=0,ans;

		for(i=0;i<m;i++)
		{
			ans1=ans1+a[i]*b[i];
			ans2=ans2+a[i]*b[m-i-1];
		}
		if(ans1<ans2)
			ans=ans1;
		else
			ans=ans2;

		fout<<"Case #"<<k+1<<": ";
		fout<<ans;
		fout<<endl;

	}
	return 0;
}

