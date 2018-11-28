#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("A-large.out");
	
	int n;
	int p,k,l;
	//char src[10000],tar[10000],val[10000];
	fin>>n;
	
	for(int c=1; c<=n; c++)
	{
		fin>>p>>k>>l;
		//cout<<s<<" "<<src<<" "<<tar<<"\n";
		vector<long long> fre;
		long long temp;
		for(int i=0;i<l;i++)
		{
			fin>>temp;
			fre.push_back(temp);
		}
		sort(fre.begin(),fre.end(),greater<int>( ));
		int j = 0;
		int key[k];
		for(int i=0;i<k;i++)
			key[i]=0;
		long long count=0;
		while(j<fre.size())
		{
			key[j%k]++;
			count+=fre[j%l]*key[j%k];
			j++;
			//cout<<count<<endl;
		}
		
		fout<<"Case #"<<c<<": "<<count<<"\n";
	
	}
	
	
	return 0;
}

