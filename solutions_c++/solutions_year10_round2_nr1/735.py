#line 3 "main.cpp"
#include  "iostream" 
#include  "vector"
#include  "string"
#include  "string.h"
#include  "algorithm" 
#include  "sstream"
#include  "set"
#include  "map"
#include  "queue"
#include  "deque"
#include  "stack"
#include "list"
#include  "bitset"
#include  "cstdio"
#include  "assert.h"
#include  "cmath"
#include  "cstdlib"
#include  "ctime"
#include  "cfloat"
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define INF 1<<28
int N,M;

map< string,bool > esta;
int res=0;

void saca(string cad)
{
	for(int i=0;i<cad.size();i++)
	{
		if(cad[i]=='/')
			cad[i]=' ';
	}
	
	stringstream is(cad);
	string aux;
	string te="/";
	while(is>>aux)
	{
		
		te+=aux;
		if(esta[te])
			continue;
		else
		{
		esta[te]=true;
		}
	}
	return;
}
void saca2(string cad)
{
for(int i=0;i<cad.size();i++)
	{
		if(cad[i]=='/')
			cad[i]=' ';
	}
	
	stringstream is(cad);
	string aux;
	string te="/";

	while(is>>aux)
	{
		
		te+=aux;
		if(esta[te])
		{
			continue;
		}
		else
		{
			res++;
			esta[te]=true;
		}
	}
	return;
	
}
int main()
{
	
	freopen("A2.in","r",stdin);
	 freopen("C:\\Documents and Settings\\jpenam\\Escritorio\\gcj\\AAsol2.out","w",stdout);
	
	int cases;
	cin>>cases;
	for(int ii=0;ii<cases;ii++)
	{
		cin>>N>>M;
		string cad;
		esta.clear();
		for(int i=0;i<N;i++)
		{
			cin>>cad;
			saca(cad);
		}

		res=0;
		for(int i=0;i<M;i++)
		{
			cin>>cad;
			saca2(cad);
			
		}
		
		
		cout<<"Case #"<<ii+1<<": ";
		cout<<res;
		cout<<endl;
	}

	return 0;
}
//}
//int cases,N,K,B,T;
//int main(){
//	
//		freopen("Blargo.in","r",stdin);
// freopen("C:\\Documents and Settings\\jpenam\\Escritorio\\gcj\\B2sol.out","w",stdout);
//	cin>>cases;
//	for(int ii = 0; ii <cases; ii++){
//		
//		cin >> N >> K>> B >> T;
//		
//		int dentro = 0;
//		vector<int> X, Xf;
//		vector<int> V;
//		int aux;
//		for(int i = 0; i < N; i++) 
//		{
//			cin>>aux;
//			X.push_back(aux);
//		}
//		for(int i = 0; i < N; i++)
//		{
//			cin>>aux;
//			V.push_back(aux);
//		}
//		
//		for(int i = 0; i < N; i++)
//			Xf.push_back(X[i] + V[i] * T);
//			
//		
//		vector< int > valor(N);
//		for(int i = 0; i < N; i++)
//		{
//			if(Xf[i] >= B)
//			{
//				int ind=i;
//				//swaps
//				for(int j = 0; j < N; j++) 
//					if(X[j] >= X[ind] && Xf[j] < B)
//						valor[ind]++;
//			}
//			else valor[i] = INF;
//		}
//		
//		sort(all(valor));
//		
//		int res = 0;
//		bool pode = true;
//		for(int i = 0; i < K; i++)
//		{
//			if(valor[i] >=INF) 
//				pode = false;
//			else 
//				res +=valor[i];
//		}
//		cout << "Case #"<<ii+1<<": ";
//
//		if(pode)
//			cout<<res<<endl;
//		else 
//			cout <<"IMPOSSIBLE"<<endl;
//	}
//	return 0;
//}
