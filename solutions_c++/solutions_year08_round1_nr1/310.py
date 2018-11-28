#include <stdio.h>
#include <math.h> 
#include <iostream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>

using namespace std;

stringstream& GetLineStream(stringstream& aLineStream)
{
		string line; 
        do 
        { 
			getline(cin,line); 
        } 
        while(line==""); 
        aLineStream<<line; 
		return aLineStream;
}

template<typename F, typename S>
void  ReadPair(const string& aLine, F& aFirst, S& aSecond)
{
		int pos=aLine.find(':'); 
		stringstream first(aLine.substr(0,pos));
		first>>aFirst;
		stringstream second(aLine.substr(pos+1));
		second>>aSecond;
}
long long res=0;
void PrintResult(int i)
{
		cout<<"Case #"<<i<<": ";
		cout<<res;
		cout<<"\n";
}
int Len;

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int N;
	cin>>N;

	for(int i=1;i<=N;++i)
	{
		cin>>Len;
		vector<int> a;
		vector<int> b;
		int r;
		for(int j=0;j<Len;++j)
		{
			cin>>r;
			a.push_back(r);
		}
		for(int j=0;j<Len;++j)
		{
			cin>>r;
			b.push_back(r);
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end(),greater<int>());
		res=0;
		for(int j=0;j<Len;++j)
			res+=a[j]*b[j];
		PrintResult(i);
	}
	return 0;
}
