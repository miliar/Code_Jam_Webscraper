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
//int N,M;
///*
//1
//8 8
//
///az
//
///9at/cgp/pxf
//
///5p
//
///9at/cgp
//
///9at/cgp/efh
//
///yp8e
//
///bkvy
//
///9at
//
///yp8e/xj0s
//
///yp8e/cgp
//
///yp8e/9vr
//
///yp8e/yp8e
//
///yp8e/v
//
///yp8e/5p
//
///yp8e/bkvy
//
///yp8e/bkvy/v
//*/
//vector <string> saca(string cad)
//{
//	for(int i=0;i<cad.size();i++)
//	{
//		if(cad[i]=='/')
//			cad[i]=' ';
//	}
//	vector <string> res;
//	stringstream is(cad);
//	string aux;
//	while(is>>aux)
//	{
//		res.push_back(aux);
//	}
//	return res;
//}
//int main()
//{
//	
//	freopen("solo1.in","r",stdin);
//	 freopen("C:\\Documents and Settings\\jpenam\\Escritorio\\gcj\\Asol.out","w",stdout);
//	
//	int cases;
//	cin>>cases;
//	for(int ii=0;ii<cases;ii++)
//	{
//		cin>>N>>M;
//		vector <string> tengo;
//		
//		map< pair< string, int> , bool> todos;
//		todos.clear();
//		string cad;
//		
//		for(int i=0;i<N;i++)
//		{
//			cin>>cad;
//			vector <string> v=saca(cad);
//			for(int j=0;j<v.size();j++)
//			{
//				if(todos.find(make_pair(v[j],j))!=todos.end())
//				{
//					continue;
//				}
//				else
//				{
//					//sino esta los meto
//					for(int jj=j;jj<v.size();jj++)
//					{
//						todos[make_pair(v[jj],jj)]=true;
//					}
//					break;
//				}
//			}
//		}
//		int res=0;
//		vector <string> despues;
//		despues.clear();
//		for(int i=0;i<M;i++)
//		{
//			cin>>cad;
//			despues.push_back(cad);
//		}
//		//sort(all(despues));
//		for(int i=0;i<M;i++)
//		{
//			cad=despues[i];
//			vector <string> v=saca(cad);
//			for(int j=0;j<v.size();j++)
//			{
//				
//				bool estaa=true;
//				int jj=0;
//				for(int jj=0;jj<=j&&!estaa;jj++)
//				{
//					if(todos.find(make_pair(v[j],j))!=todos.end())
//						continue;
//					else
//					{
//						estaa=false;
//					}
//				}
//				
//				if(!estaa)
//				{
//					//sino esta los meto
//					for(int jj=j;jj<v.size();jj++)
//					{
//						res++;
//						todos[make_pair(v[jj],jj)]=true;
//					}
//					break;
//				}
//			}
//		}
//		
//		
//		cout<<"Case #"<<ii+1<<": ";
//		cout<<res;
//		cout<<endl;
//	}
//
//	return 0;
//}
int cases,N,K,B,T;
int main(){
	
		freopen("B1in.in","r",stdin);
 freopen("C:\\Documents and Settings\\jpenam\\Escritorio\\gcj\\Bsol.out","w",stdout);
	cin>>cases;
	for(int ii = 0; ii <cases; ii++){
		
		cin >> N >> K>> B >> T;
		
		int dentro = 0;
		vector<int> X, Xf;
		vector<int> V;
		int aux;
		for(int i = 0; i < N; i++) 
		{
			cin>>aux;
			X.push_back(aux);
		}
		for(int i = 0; i < N; i++)
		{
			cin>>aux;
			V.push_back(aux);
		}
		
		for(int i = 0; i < N; i++)
			Xf.push_back(X[i] + V[i] * T);
			
		
		vector< int > valor(N);
		for(int i = 0; i < N; i++)
		{
			if(Xf[i] >= B)
			{
				int ind=i;
				//swaps
				for(int j = 0; j < N; j++) 
					if(X[j] >= X[ind] && Xf[j] < B)
						valor[ind]++;
			}
			else valor[i] = INF;
		}
		
		sort(all(valor));
		
		int res = 0;
		bool pode = true;
		for(int i = 0; i < K; i++)
		{
			if(valor[i] >=INF) 
				pode = false;
			else 
				res +=valor[i];
		}
		cout << "Case #"<<ii+1<<": ";

		if(pode)
			cout<<res<<endl;
		else 
			cout <<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
