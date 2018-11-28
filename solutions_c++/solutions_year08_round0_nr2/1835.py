
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



const int maxn=105;
int turntimes,na,nb;
struct times
{
	int begin,end;
	//bool flag;
}testa[maxn],testb[maxn];
bool tbf[maxn],taf[maxn];

class mycrit
{
public:
	bool operator () (const times &a,const times &b)
	{
		return a.begin<b.begin;
	}
};
int main()
{
	//freopen("test.txt","r",stdin);
	freopen("B-small2.in","r",stdin);
	freopen("B-small2.out","w",stdout);
	/*freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);*/
	int N;
	cin>>N;
	string s;
	for(int cases=1;cases<=N;cases++)
	{
		cin>>turntimes;
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

		sort(testa,testa+na,mycrit());
		sort(testb,testb+nb,mycrit());
		memset(tbf,0,sizeof(tbf));
		memset(taf,0,sizeof(taf));
		int n1=0;
		for(int i=0;i<na;i++)
		{
			bool flag=0;
			for(int j=0;j<nb;j++)
			{
				if(testb[j].end+turntimes<=testa[i].begin && !tbf[j]){tbf[j]=1;flag=1;break;}
			}
			if(!flag) n1++;
		}
		int n2=0;
		for(int i=0;i<nb;i++)
		{
			bool flag=0;
			for(int j=0;j<na;j++)
			{
				if(testa[j].end+turntimes<=testb[i].begin && !taf[j]){taf[j]=1;flag=1;break;}
			}
			if(!flag) n2++;
		}



		cout<<"Case #"<<cases<<": "<<n1<<" "<<n2<<endl;
	}
	return 0;
}