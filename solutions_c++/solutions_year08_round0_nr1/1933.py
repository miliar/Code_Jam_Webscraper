#include <set>
#include <map>
#include <string>
#include <iostream>
using namespace std;

int N;			//20
int S;			//100
int Q;			//1000
int q[1000];

bool p[1000][1000];

int f[1000];

int solve()
{
	int i,j,k,l;
	int ans=0;

	map<string, int> m;
	std::map<std::string,int>::const_iterator c;

	string s;
 	cin>>S;
 	getline(cin, s); 	
	for (j=0;j<S;j++)
	{
		getline(cin, s);
		//下面是map的使用例子
		m.insert(map<string, int> :: value_type(s,j)) ;
//		c=m.find(s);
//		cout<<c->second<<"  "<<c->first<<endl;           // c->first 和 c->second分别获得了<string, int>中的string和int
	}

	cin>>Q;
	getline(cin, s); 	
	
	if (Q==0)
	{
		return 0;
	}

	for (i=0;i<Q;i++)
	{
		getline(cin, s);
		c=m.find(s);
		q[i]=c->second;
	}

	for (i=0;i<Q;i++)
	for (j=0;j<Q;j++)
	p[i][j]=false;

	set<int> a;
	for (i=0;i<Q;i++)
	{
		a.clear();
		a.insert(q[i]);
		j=i;
		do
		{
			p[i][j]=true;
			a.insert(q[++j]);
		}
		while (a.size()<S);
	}
	
	for (i=1;i<Q;i++) f[i]=Q;


	f[0]=0;
	for (i=1;i<Q;i++)
	{
        if (p[0][i])
        {
			f[i]=0;
        }
		for (j=i;j>0 && p[j][i];j--)
		{
			if (f[j-1]+1<f[i])
			{
				f[i]=f[j-1]+1;
			}
		}
//		cout<<f[i]<<endl;
	}

	return f[Q-1];
}

int main()
{
//	freopen("A.in","r",stdin);
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);


	cin>>N;
	int i,j;
	for (i=0;i<N;i++)
	{
		j=solve();
		cout<<"Case #"<<i+1<<": "<<j<<endl;
	}

	return 0;
}
