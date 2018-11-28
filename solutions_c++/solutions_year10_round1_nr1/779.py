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
int N,K;
bool dentro(int a,int b)
{
	if(a<0||b<0||a>=N||b>=N)
		return false;
	//cout<<a<<" "<<b<<endl;
	return true;
}
void rota(vector <string> &v)
{
	int n=v.size();
	vector <string> res=v;
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
		{
			res[j][n-i-1]=v[i][j];
		}
		v=res;
}	

void bajan(vector <string> &v)
{
	int n=v.size();
	vector <string> res=v;
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++)
			res[i][j]='.';

	for(int j=0;j<n;j++)
	{
		for(int i=n-1;i>=0;i--)
		{
			int ul=i;
			if(v[i][j]=='.')
				continue;
			for(int ii=i;ii<n;ii++)
			{
				if(res[ii][j]=='.')
				{
					ul=ii;		
				}
				else
					break;
			}
			res[ul][j]=v[i][j];
		}
	}
	v=res;
}
void imp(vector <string> v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v.size();j++)
		{
			cout<<v[i][j];
		}
		cout<<endl;
	}
}
bool gana(vector <string> v,char c)
{
	//horizontal
	string kiero="";
	for(int i=0;i<K;i++)
		kiero+=c;

	for(int i=0;i<v.size();i++)
	{
		if(v[i].find(kiero,0)!=-1)
			return true;
	}
	//cout<<"s1"<<endl;
	for(int i=0;i<v.size();i++)
	{
		string cad="";
		for(int j=0;j<v.size();j++)
			cad+=v[j][i];
		if(cad.find(kiero,0)!=-1)
			return true;
	}
	//cout<<"s2"<<endl;
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v.size();j++)
		{
			string cad="";
			for(int ii=0;ii<K;ii++)
			{
				int nx=i+ii;
				int ny=j+ii;
				if(dentro(nx,ny))
				{
					
					cad+=v[nx][ny];
				}
				else
					break;
			}
			if(cad.find(kiero,0)!=-1)
			return true;
		}
	}
//cout<<"s3"<<endl;
		for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v.size();j++)
		{
			string cad="";
			for(int ii=0;ii<K;ii++)
			{
				int nx=i+ii;
				int ny=j-ii;
				if(dentro(nx,ny))
					cad+=v[nx][ny];
			}
			if(cad.find(kiero,0)!=-1)
			return true;
		}
	}
//cout<<"s4"<<endl;
}
int main()
{
	 freopen("A-small-attempt0.in","r",stdin);
	 freopen("Achico","w",stdout);
	int cases;
	cin>>cases;
	for(int ii=0;ii<cases;ii++)
	{
		cin>>N>>K;
		vector <string> v;
		string cad;
		for(int i=0;i<N;i++)
		{
			cin>>cad;
			v.push_back(cad);
		}
		//imp(v);
		//cout<<endl;
		rota(v);
		//imp(v);
		//	cout<<endl;
		bajan(v);
		//imp(v);
		//	cout<<endl;
		bool R=gana(v,'R');
		
		bool B=gana(v,'B');
		cout<<"Case #"<<ii+1<<": ";
		if(R&&B)
		{
			cout<<"Both"<<endl;
		}
		else if(!R&&!B)
		{
			cout<<"Neither"<<endl;
		}
		else if(!R&&B)
		{
			cout<<"Blue"<<endl;
		}
		else if(R&&!B)
			cout<<"Red"<<endl;

	}
	return 0;
}