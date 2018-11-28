#include<iostream>
#include<fstream>
#define MAX 1000
using namespace std;
ifstream in("data.in");
ofstream out("data.out");
class a
{
	int l,d,n;
	char my[MAX];
	char his[MAX];
	char dit[MAX][MAX];
	int count;	
public:
	a();
	void search(int, int);
	bool indit(int );
	void process();
};
a::a()
{
	in>>l>>d>>n;
	for(int i = 1;i <= d;i++)
	{
		in>>dit[i];
	}
	
	count = 0;
}
bool a::indit(int L)
{
	for(int i = 1;i <= d;i++)
	{
		int find = 1;
		for(int j = 0;j < L;j++)
		{
			if(dit[i][j] != my[j])
			{
				find = 0;	
				break;
			}
		}
		if(find == 1)
		{
			return true;
		}
	}
	return false;
}
void a::search(int i, int p)
{
	if(i > l - 1)
	{
		if(indit(l))
		{
			count ++;
		}
	}
	else
	{
		if(his[p] == '(')
		{
			int j;
			for(j = p + 1;his[j] != ')';j++)
			{
				;
			}
			for(int k = p + 1;k < j;k++)
			{
				my[i] = his[k];
				if(indit(i))
				search(i + 1, j + 1);
			}
		}
		else
		{
			my[i] = his[i];
			if(indit(i))
			search(i + 1, p + 1);
		}
	}
}
void a::process()
{
	for(int i = 1;i <= n;i++)
	{
		count = 0;
		in>>his;
		search(0, 0);
		 out<<"Case #"<<i<<": "<<count<<endl;
//		 cout<<"Case #"<<i<<": "<<count<<endl;
	}
}
void solve()
{
	class a myobj;
	myobj.process();
}
int main()
{
	solve();
	return 0;
}
