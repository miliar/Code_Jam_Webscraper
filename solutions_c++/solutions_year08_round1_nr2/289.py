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

short * Result;
short * Satisfied;
bool Impossible;
int Cust;
int Kind;

void PrintResult(int i)
{
		cout<<"Case #"<<i<<": ";
		if(Impossible)
			cout<<"IMPOSSIBLE";
		else
			for(int j=0;j<Kind;j++)
				cout<<Result[j]<<" ";
		cout<<"\n";
}

struct Customer
{
	set<int> likes;
	int malted;
};

vector<Customer> Customers;
typedef set<int>::iterator SII;

void ReadCust()
{
	Customer c;
	c.malted=-1;
	int t;
	cin>>t;
	for(int i=0;i<t;++i)
	{
		int x,y;
		cin>>x>>y;
		--x;//0based
		if(y)
			c.malted=x;
		else
			c.likes.insert(x);
	}
	Customers.push_back(c);
}

bool CheckAllSat()
{
	int sumSat=0;
	memset(Satisfied,0,sizeof(short)*Cust);
	for(int i=0;i<Kind;++i)
	{
		for(int j=0;j<Cust;++j)
		{
			Customer& c=Customers[j];
			if(!Satisfied[j])
			{
				if(   (Result[i]&&(c.malted==i))||
				((!Result[i])&&(c.likes.find(i)!=c.likes.end()))   )
				{
					Satisfied[j]=1;
					++sumSat;
					if(sumSat==Cust)
						return true;
				}
			}
		}
	}
	return false;
}

void Solve()
{
	Impossible=true;
	while(!CheckAllSat())
	{
		for(int i=0;i<Cust;++i)
		{
			if(!Satisfied[i])
			{
				Customer& c=Customers[i];
				if(c.malted<0)
					return;
				else
				{
					Result[c.malted]=1;//this must be set;
				}
			}
		}
	}
	Impossible=false;
}

int main(int argc, char* argv[])
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int N;
	cin>>N;

	for(int i=1;i<=N;++i)
	{
		Customers.clear();
		cin>>Kind>>Cust;
		Result=new short[Kind];
		Satisfied=new short[Cust];
		memset(Result,0,sizeof(short)*Kind);
		memset(Satisfied,0,sizeof(short)*Cust);
		for(int j=0;j<Cust;++j)
		{
			ReadCust();
		}
		Solve();
		PrintResult(i);
		delete Result;
		delete Satisfied;
		Result=0;
		Satisfied=0;
	}
	return 0;
}
