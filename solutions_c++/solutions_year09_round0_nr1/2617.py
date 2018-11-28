#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct flags
{
	void init()
	{
		for(int i=0;i<26;i++)c[i]=0;
	}
	bool c[26];
};

int main()
{
	freopen("Q2009a.in","rt",stdin);
	freopen("Q2009a.out","wt",stdout);
	int L,D,N;
	int i,j,k;
	int total;
	cin>>L>>D>>N;
	vector<string>dict(D);
	vector<flags>query(L);
	string buf;
	string::iterator bufit;
	for(i=0;i<D;i++)cin>>dict[i];
	for(i=0;i<N;i++)
	{
		cin>>buf;
		for(bufit=buf.begin(),j=0;bufit!=buf.end();bufit++)
		{
			query[j].init();
			if(*bufit=='(')
			{
				while(*(++bufit)!=')')
				{
					query[j].c[*bufit-'a']=1;;
				}
			}
			else
			{
				query[j].c[*bufit-'a']=1;;
			}
			j++;
		}
		total=0;
		for(j=0;j<D;j++)
		{
			for(k=0;k<L;k++)
			{
				if(!query[k].c[dict[j][k]-'a'])break;
			}
			if(k==L)total++;
		}
		cout<<"Case #"<<i+1<<": "<<total<<endl;
	}
	return 0;
}
