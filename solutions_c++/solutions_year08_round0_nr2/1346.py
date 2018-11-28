#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int timeadd(int m,int temp)
{
 	int ans;
	int min=temp%100 + m;
	ans=(temp/100)*100 + min%60 + (min/60)*100;
	return ans;
}

int main()
{
 	ifstream fin("1.txt");
	ofstream fout("4.txt");
 	int n;
	fin>>n;
	for(int i=0;i<n;i++)
	{
	 	vector<int> A1,A2,B1,B2;
	 	int m;
		fin>>m;
		int a,b;
		fin>>a>>b;
		string inp,inp2;
		for(int j=0;j<a;j++)
		{
		 	fin>>inp>>inp2;
			//inp.find(":",0)
			inp.erase(2,1);
			inp2.erase(2,1);
			int temp=atoi(inp.c_str());
			A1.push_back(temp);
			temp=atoi(inp2.c_str());
			//fout<<temp<<endl;
			temp=timeadd(m,temp);
			A2.push_back(temp);
		}
		sort(A1.begin(),A1.end());
		sort(A2.begin(),A2.end());
		for(int j=0;j<b;j++)
		{
		 	fin>>inp>>inp2;
			//inp.find(":",0)
			inp.erase(2,1);
			inp2.erase(2,1);
			int temp=atoi(inp.c_str());
			B1.push_back(temp);
			temp=atoi(inp2.c_str());
			temp=timeadd(m,temp);
			B2.push_back(temp);
		}
		sort(B1.begin(),B1.end());
		sort(B2.begin(),B2.end());
	/*	for(int p=0;p<A1.size();p++)
		{
		 	fout<<A1[p]<<" "<<A2[p]<<endl;
		}
		for(int p=0;p<B1.size();p++)
		{
		 	fout<<B1[p]<<" "<<B2[p]<<endl;
		}*/
		int counta=0;
		int countb=0;
		int iterb=0;
		int itera=0;
		for(int j=0;j<A1.size();j++)
		{
		 	if(iterb<B2.size() && B2[iterb]<=A1[j])
			{
			 	iterb++;
			}
			else
			{
			 	counta++;
			}			
		}
		for(int j=0;j<B1.size();j++)
		{
		 	if(itera<A2.size() && A2[itera]<=B1[j])
			{
			 	itera++;
			}
			else
			{
			 	countb++;
			}			
		}
	 	fout<<"Case #"<<i+1<<": "<<counta<<" "<<countb<<endl;
		A1.clear();
		A2.clear();
		B1.clear();
		B2.clear();
	}
	return 0;
}
