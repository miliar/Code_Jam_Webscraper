#include<cstdio>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

#define pci pair<char, int>
pci* mas;
int* tms;
	vector<string> vyvod;
	vector<string> oppos;
	string lin;
	string out;

char canCon(char c)
{
	for(int i=0; i<vyvod.size(); ++i)
		if(out[out.size()-1]==vyvod[i][0] && c==vyvod[i][1] || out[out.size()-1]==vyvod[i][1] && c==vyvod[i][0])
			return vyvod[i][2];
	return 0;
}

bool isOpp()
{
	for(int i=0; i<(int)out.size()-1; ++i)
	{
		for(int j=0; j<oppos.size(); ++j)
			if(out[out.size()-1]==oppos[j][0] && out[i]==oppos[j][1] || out[out.size()-1]==oppos[j][1] && out[i]==oppos[j][0])
				return true;
	}
	return false;
}

void test(int num)
{
	vyvod.clear();
	oppos.clear();
	lin.clear();
	out.clear();
	int c;
	cin>>c;
	for(int i=0; i<c; ++i)
	{
		string tmp;
		cin>>tmp;
		vyvod.push_back(tmp);
	}
	int d;
	cin>>d;
	for(int i=0; i<d; ++i)
	{
		string tmp;
		cin>>tmp;
		oppos.push_back(tmp);
	}
	int n;
	cin>>n;
	cin>>lin;
	char rs;
	for(int i=0; i<n; ++i)
	{
		if(out.empty())
		{
			out.push_back(lin[i]);
			continue;
		}
		if(isOpp())
		{
			out.clear();
			out.push_back(lin[i]);
			continue;
		}
		if(rs=canCon(lin[i]))
		{
			out[out.size()-1]=rs;
			continue;
		}
		out.push_back(lin[i]);
	}
	if(isOpp())
	{
		out.clear();
	}
	printf("Case #%d: ",num);
	if(out.empty())
	{
		printf("[]\n");
		return;
	}
	printf("[%c",out[0]);
	for(int i=1; i<out.size(); ++i)
		printf(", %c",out[i]);
	printf("]\n");
}

int main()
{
	mas=new pci[1000];
	tms=new int[1000];
	int t;
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&t);
	for(int i=0; i<t; ++i)
		test(i+1);
	return 0;
}