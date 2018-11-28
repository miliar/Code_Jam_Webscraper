#include<iostream>
#include<fstream>
#include<map>
#include<string>

using namespace std;

int main()
{
 	ifstream fin("1.txt");
	ofstream fout("2.txt");
	int n;
	fin>>n;
	for(int i=0;i<n;i++)
	{
	 	int count=0;
	 	map<string,int> M;
		map<string,int>::iterator iter;
	 	int m;
		fin>>m;
		string inp;
		for(int j=0;j<m;j++)
		{
		 	getline(fin,inp);
			if(inp=="")
				getline(fin,inp);
			//fout<<inp<<endl;
		 	M[inp]=0;
		}
		int p;
		fin>>p;
		int sum=0;
		//cout<<n<<" "<<m<<" "<<p;
		for(int j=0;j<p;j++)
		{
		 	getline(fin,inp);
			if(inp=="")
					   getline(fin,inp);
			//fout<<inp<<endl;
		 	if(M[inp]==0)
			{
			 	//fout<<j<<" "<<M[inp]<<endl;
			 	M[inp]=1;
				sum++;
				if(sum==m)
				{
					sum=1;
					for(iter=M.begin();iter!=M.end();iter++)
					{
					 	iter->second=0;
					}
					M[inp]=1;
					count++;
				}
			}
		}
		fout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
