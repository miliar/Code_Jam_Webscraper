#include<stdio.h>
#include<string.h>
#include<string>
#include<set>
#include<vector>
#include<algorithm>
using namespace std;

int a,b;


vector<int> all (int x)
{
	vector<int> ret;
	char t[20];
	sprintf(t,"%d%d",x,x);
	int i,m = strlen(t)/2,tt[20];
	for(i=0; t[i] ;i++)
		tt[i] = t[i]-'0';
	set<int> ss;
	for(i=0; i<m ;i++)
	{
		if(!tt[i]) continue;
		int temp=0;
		for(int j=i; j<m+i ;j++)
			temp = temp*10 + t[j]-'0';
		if(ss.find(temp) == ss.end()) ret.push_back(temp);
		ss.insert(temp);
	}
	return ret;
}


int calc (int x)
{
	int ret =0;
	unsigned int j;
	vector<int> t = all(x);
	for(j=0; j< t.size() ;j++)
		if(t[j]<=b && t[j]>x)
			ret++;
	return ret;
}

int solve()
{
	int i,ret=0;
	for(i=a; i<b; i++)
		ret+=calc(i);
	return ret;
}

int main()
{
	int qq,q;
	FILE *in = fopen("t.in","r");
	FILE *out= fopen("ans.txt","w");
	fscanf(in,"%d",&qq);
	for(q=1; q<=qq ;q++)
	{
		fscanf(in,"%d%d",&a,&b);
		fprintf(out,"Case #%d: %d\n",q,solve());
	}
	return 0;
}
