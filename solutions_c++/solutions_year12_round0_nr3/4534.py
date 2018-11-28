#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<vector>
#include<set>

using namespace std;

const int LIMIT = 1000;

int pot10[16]= {0,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000};

vector<set<int> > v;

int longitud(int n)
{
	int t=0;
	while(n!=0)
	{
		n/=10;
		t++;
	}
	return t;
} 

void precalc()
{
	v= vector<set<int> >(LIMIT+10);
	int t;
	for(int i = 1; i < LIMIT; ++i)
	{
		t = longitud(i);
		for(int j = 1; j < t; ++j)
		{
			int pp1 = pot10[j];
			int pp2 = pot10[t-j];
			int newNum = (i%pp1)*pp2 + i/pp1;
			if ( t == longitud(newNum) )
			{
				v[i].insert( newNum );
			}
		}
	}
}

int get(int A, int B)
{
	int cont = 0;
	for ( int i = A; i < B; ++i)
	{
		set<int>::iterator it;
		for( it = v[i].begin(); it != v[i].end(); ++it)
		{
			if( (*it) > i && (*it)<=B)
			{
				cont++;
			}
		}
	}
	return cont;
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	 
	int n; cin>>n;
	int n1, n2;
	precalc();
	
	for(int caso=1;caso<=n;++caso)
	{
		cin>>n1>>n2;
		if(caso > 1)cout<<endl;
		cout<<"Case #"<<caso<<": ";
		cout<<get(n1, n2);
	}
}