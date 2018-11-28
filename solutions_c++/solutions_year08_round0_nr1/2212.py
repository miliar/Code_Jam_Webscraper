#include<iostream>
#include<vector>
#define MIN(a,b) ((a)<(b)?(a):(b))

using namespace std;

int mem[101][1001];
vector <string> query;
vector <string> engines;
int get(int engine, int pos)
{
	int ret=999999999;
	int i;
	int temppos=pos;
	if(mem[engine][pos]!=-1)
		return mem[engine][pos];
	if(engines[engine]==query[pos])
	{
		mem[engine][pos]=ret;
		return ret;
	}
	for(i=pos;i<query.size();i++)
	{
		if(query[i]!=engines[engine])
			temppos++;
		else
			break;
	}
	if(i==query.size())
	{
		mem[engine][pos]=0;
		return 0;
	}
	for(i=0;i<engines.size();i++)
	{
		if(i!=engine)
			ret=MIN(ret,1+get(i,temppos));
	}
	mem[engine][pos]=ret;
	return ret;
}


int main()
{
	int N;
	cin>>N;
	int count=1;
	while(N--)
	{
		int S,Q;
		cin>>S;
		engines.clear();
		query.clear();
		int i;
		char buff[200];
		int ret=999999999;
		memset(mem,0xff,sizeof(mem));
		cin.getline(buff,101);
		for(i=0;i<S;i++)
		{
			cin.getline(buff,101);
			string temp(buff);
			engines.push_back(temp);
		}
		cin>>Q;
		cin.getline(buff,101);
		for(i=0;i<Q;i++)
		{
			cin.getline(buff,101);
			string temp(buff);
			query.push_back(temp);
		}
		if(Q==0)
		{
			cout<<"Case #"<<count<<": "<<"0"<<endl;
			count++;
			continue;
		}
		for(i=0;i<engines.size();i++)
			ret=MIN(ret,get(i,0));
		cout<<"Case #"<<count<<": "<<ret<<endl;
		count++;
	}
	return 0;
}


