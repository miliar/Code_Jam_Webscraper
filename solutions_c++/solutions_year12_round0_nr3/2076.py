#include<fstream>
#include<iostream>
#include<map>
using namespace std;

int pw[]={1,10,100,1000,10000,100000,1000000};

int get(int n)
{
	int cnt=0;

	while(n>0)
	{
		n/=10;
		++cnt;
	}
	return cnt;
}

int count_it(int n, int low, int up, int sz)
{
	int cnt=0,ad=0,n1=n,put=-1;
	map<int,int> mp;

	while(sz>1)
	{
		--sz;
		++put;
		int cifra=n1%10;
		n1/=10;
		if(cifra!=0)
		{
			ad=cifra*pw[put]+ad;
			int number=ad*pw[sz]+n1;
			if(number>n && number<=up && mp.find(number)==mp.end())
			{
				++cnt;
				mp[number]=1;
			}
		}
	}
	return cnt;
}

int main()
{
	int t,a,b;
	long long cnt=0;
	
	ifstream in("C.in");
	ofstream out("C.out");

	in>>t;
	for(int i=0;i<t;++i)
	{
		in>>a>>b;
		cnt=0;
		int sz=get(a);
		for(int j=a;j<=b;++j)
			cnt+=count_it(j,a,b,sz);
		out<<"Case #"<<i+1<<": "<<cnt<<"\n";
	}
	in.close();
	out.close();
}
