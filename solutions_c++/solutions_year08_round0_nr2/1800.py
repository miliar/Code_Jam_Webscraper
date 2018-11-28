#include <iostream>
#include <string>
#include <set>
using namespace std;

const int maxn=2000;
struct node
{
	int leave,arrive,inde;
};

bool op (node a,node b)
{
	return (a.leave<b.leave);
}

int na,nb,t;
node p[maxn];
multiset<int> tra,trb;

int read_time()
{
	char ch1,ch2,ch3,ch4,ch5;
	cin >> ch1 >> ch2 >> ch3 >> ch4 >> ch5;
	return (((ch1-'0')*10+(ch2-'0'))*60+(ch4-'0')*10+(ch5-'0'));
}

bool good(int a,int b)
{
	tra.clear();
	trb.clear();
	for (int i=1;i<=na+nb;i++)
	{
		if (p[i].inde==0)
		{
			if (a>0)
			{
				a--;
				trb.insert(p[i].arrive+t);
			}
			else if (tra.size()!=0)
			{
				if (*tra.begin()<=p[i].leave)
				{
					trb.insert(p[i].arrive+t);
					tra.erase(tra.begin());
				}
				else return false;
			}
			else return false;
		}
		if (p[i].inde==1)
		{
			if (b>0)
			{
				b--;
				tra.insert(p[i].arrive+t);
			}
			else if (trb.size()!=0)
			{
				if (*trb.begin()<=p[i].leave)
				{
					tra.insert(p[i].arrive+t);
					trb.erase(trb.begin());
				}
				else return false;
			}
			else return false;
		}
	}
	return true;
}

int main()
{
	int test;
	cin >> test;
	for (int w=1;w<=test;w++)
	{
		cin >> t;
		cin >> na >> nb;
		for (int i=1;i<=na;i++)
		{
			p[i].leave=read_time();
			p[i].arrive=read_time();
			p[i].inde=0;
		}
		for (int i=1;i<=nb;i++)
		{
			p[i+na].leave=read_time();
			p[i+na].arrive=read_time();
			p[i+na].inde=1;
		}
		sort(&p[1],&p[na+nb+1],op);
		bool nowgood=false;
		for (int i=0;i<=na+nb && !nowgood;i++)
		{
			for (int j=0;j<=i;j++)
			{
				if (good(j,i-j))
				{
					cout <<"Case #"<<w <<": " <<j << ' ' << i-j << endl;
					nowgood=true;
					break;
				}
			}
		}
	}
	return 0;
}
