#include<iostream>
#include<fstream>
#include<cstring>
#include<cmath>
#include<map>
#include<vector>
#include<algorithm>
#include<iterator>
#include<sstream>
#include<set>
using namespace std;

typedef unsigned long long uint64;
typedef long long int64;

map<int,long double> FLIP;
uint64 FF[1001];

long double flip(int n)
{
	return n;
	/*
	map<int,long double>::iterator it=FLIP.find(n);
	if(it!=FLIP.end())return it->second;

	long double L=0.0;
	long double P[n+1];
	P[n]=1.00/FF[n];
	P[n-1]=0.0;
	long double A;
	A=0;
	for(int i=n-2;i>=0;i--)
	{
		int sign=((n-i)%2==0?1:-1);
		A+=sign*1.00/FF[n-i];
		P[i]=A/FF[i];
//		cout<<i<<':'<<P[i]<<endl;
	}
	for(int i=1;i<=n-2;i++)
		L+=P[i]*flip(n-i);

	L+=1.0;
	L/=(1.0-P[0]);

	FLIP[n]=L;
	cout.precision(8);
	cout<<n<<':'<<L<<endl;
	return L;
	*/
}

int main(int argc, char *argv[])
{
//readin file
	string file;
	if(argc!=2){cerr<<"0,1 or 2!"<<endl;exit(1);}
	switch(atoi(argv[1]))
	{
		case 0: file="test"; break;
		case 1: file="D-small"; break;
		case 2: file="D-large"; break;
		default: cerr<<"choose the correct file, 0(test),1(small),2(large)"<<endl;exit(1); break;
	}
	string ifilename=file+".in"; string ofilename=file+".out";
	ifstream input(ifilename.c_str());ofstream output(ofilename.c_str());

//read in number of events
	int T;
	input>>T;
	int N;

	FF[0]=1;FF[1]=1;
	for(int i=2;i<1001;i++)FF[i]=i*FF[i-1];
	
	FLIP[2]=2.0;
	FLIP[3]=2.5;
//main loop start
	for(int t=0;t<T;t++)
	{
		input>>N;
		int A[N+1];A[0]=0;
		bool V[N+1];V[0]=true;
		for(int i=1;i<=N;i++)
		{
			input>>A[i];
			V[i]=false;
		}
		long double sum=0.0;
		for(int i=1;i<=N;i++)
		{
			if(V[i]!=true)
			{
				V[i]=true;
				if(A[i]==i)continue;
				int count=1;
				int j=i;
				while(A[j]!=i)
				{
					j=A[j];
					V[j]=true;
					count++;
				}
//				cout<<count<<endl;
				sum += count;//flip(count);
			}
		}
		
		cout<<"case : "<<t+1<<endl;
		output.precision(6);
		output<<"Case #"<<t+1<<": "<<showpoint<<sum<<endl;
	}

	input.close();
	output.close();
	return 0;
}
