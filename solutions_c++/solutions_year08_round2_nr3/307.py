#include <fstream>
#include <iostream>
using namespace std;

int v[1000001];
int link[1000001];

int main()
{
	int n, k, m, p, head, tail;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	fin >> n;
	for(int i=0;i<n;i++)
	{
		fin >> k;
		v[1]=1;
		for(int j=1;j<=k;j++)
			if(j!=k) link[j]=j+1;
			else link[j]=0;
		head=2;
		tail=k;
		for(int j=2;j<=k-1;j++)
		{
			link[tail]=head;
			for(int z=0;z<j-1;z++)
			{
				tail=head;
				head=link[head];
			}
			v[head]=j;
			head=link[head];
			link[tail]=0;
		}
		v[tail]=k;
		/*for(int j=1;j<=k;j++)
			cout << " " << v[j];
		cout << endl;*/
		fout << "Case #" << i+1 << ":";
		fin >> m;
		for(int j=0;j<m;j++)
		{
			fin >> p;
			fout << " " << v[p];
		}
		fout << endl;
	}
	return(0);
}