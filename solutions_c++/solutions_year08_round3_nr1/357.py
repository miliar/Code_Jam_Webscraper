#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	
	long long N,P,K,L;
	long long X,Y;
	long long ctr=0;
	long long cas,val;
	vector<long long>arr;
	
	fin>>N;
	for(int cas=1; cas<=N; cas++)
	{
		arr.clear();
		
		fin>>P>>K>>L;
		for(int i=1; i<=L; i++)
		{
			fin>>val;
			arr.push_back(val);
		}
		
		if(P*K<L)
		{
			fout<<"Case #"<<cas<<": "<<"Impossible"<<"\n";
			continue;
		}
		
		sort(arr.begin(),arr.end(),greater<int>( ) );
		
		long long temp=1,ctr=0;
		
		for(int i=0; i<L; i++)
		{
			val=arr[i];
			ctr+=(val*temp);
			if((i+1)%K==0)
				temp++;
		}
		
		fout<<"Case #"<<cas<<": "<<ctr<<"\n";
	}
	return 0;
	
}
	
	
	

