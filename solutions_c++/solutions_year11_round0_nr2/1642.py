#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
using namespace std;

map<char,int> idx;
char Comb[10][10];
bool Dist[10][10];
set<char> isBase;
char ans[100];
int ansLen;
void init()
{
	int i,j;
	for(i=0;i<10;++i)
		for(j=0;j<10;++j)
			Comb[i][j]=0;
	string str="QWERASDF";
	isBase.clear();
	for(i=0;i<str.size();++i)
	{
		idx.insert(make_pair(str[i],i));
		isBase.insert(str[i]);
	}
	memset(Dist,0,sizeof(Dist));
	ansLen=0;

}
bool update()
{
	if(ansLen<2) return false;
	if(isBase.find(ans[ansLen-1])!=isBase.end() &&
		isBase.find(ans[ansLen-2])!=isBase.end() &&
		Comb[idx[ans[ansLen-1]]][idx[ans[ansLen-2]]])
	{
		char c=Comb[idx[ans[ansLen-1]]][idx[ans[ansLen-2]]];
		ansLen-=2;
		ans[ansLen++]=c;
		return true;
	}
	int i;
	for(i=ansLen-2;i>=0;--i)
	{
		if(isBase.find(ans[i])==isBase.end()) continue;
		if(Dist[idx[ans[ansLen-1]]][idx[ans[i]]])
		{
			ansLen=0;
			return true;
		}
	}
	return false;
}
int main()
{
	//freopen("data.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int k,C,D,N;
	cin>>k;
	int i,j;
	for(i=1;i<=k;++i)
	{
		init();
		cout<<"Case #"<<i<<": ";
		cin>>C;
		for(j=0;j<C;++j)
		{
			string str;
			cin>>str;
			Comb[idx[str[0]]][idx[str[1]]]=str[2];
			Comb[idx[str[1]]][idx[str[0]]]=str[2];
		}
		cin>>D;
		for(j=0;j<D;++j)
		{
			string str;
			cin>>str;
			Dist[idx[str[0]]][idx[str[1]]]=1;
			Dist[idx[str[1]]][idx[str[0]]]=1;
		}
		cin>>N;
		string magic;
		cin>>magic;
		for(j=0;j<magic.size();++j)
		{
			ans[ansLen++]=magic[j];
			//while(update());
			update();
		}
		cout<<"[";
		for(j=0;j<ansLen;++j)
		{
			if(j) cout<<", ";
			cout<<ans[j];
		}
		cout<<"]"<<endl;
	}
	return 0;
}