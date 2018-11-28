
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>


using namespace std;

typedef long long LL;
LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }

const int mn=101;
int tt,na,nb;
struct times
{
	int begin,end;
	
}testa[mn],testb[mn];
bool tbf[mn],taf[mn];

class myclass
{
public:
	bool operator () (const times &a,const times &b)
	{
		return a.begin<b.begin;
	}
};
int main()
{
	
	int N;
	cin>>N;
	string s;
	for(int cases=1;cases<=N;cases++)
	{
		cin>>tt;
		cin>>na>>nb;
		getline(cin,s);
		for(int i=0;i<na;i++)
		{
			getline(cin,s);
			int k=s.find(' ');
			string s1=s.substr(0,k);
			s1.erase(s1.find(':'),1);
			int bg=s2i(s1);
			string s2=s.substr(k+1);
			s2.erase(s2.find(':'),1);
			int ed=s2i(s2);
			testa[i].begin=bg;
			testa[i].end=ed;
			
		}
		for(int i=0;i<nb;i++)
		{
			getline(cin,s);
			int k=s.find(' ');
			string s1=s.substr(0,k);
			s1.erase(s1.find(':'),1);
			int bg=s2i(s1);
			string s2=s.substr(k+1);
			s2.erase(s2.find(':'),1);
			int ed=s2i(s2);
			testb[i].begin=bg;
			testb[i].end=ed;
		
		}

		sort(testa,testa+na,myclass());
		sort(testb,testb+nb,myclass());
		memset(tbf,0,sizeof(tbf));
		memset(taf,0,sizeof(taf));
		int na1=0;
		for(int i=0;i<na;i++)
		{
			bool flag=0;
			for(int j=0;j<nb;j++)
			{
				if(testb[j].end+tt<=testa[i].begin && !tbf[j]){tbf[j]=1;flag=1;break;}
			}
			if(!flag) n1++;
		}
		int nb2=0;
		for(int i=0;i<nb;i++)
		{
			bool flag=0;
			for(int j=0;j<na;j++)
			{
				if(testa[j].end+tt<=testb[i].begin && !taf[j]){taf[j]=1;flag=1;break;}
			}
			if(!flag) n2++;
		}



		cout<<"Case #"<<cases<<": "<<na1<<" "<<nb2<<endl;
	}
	return 0;
}