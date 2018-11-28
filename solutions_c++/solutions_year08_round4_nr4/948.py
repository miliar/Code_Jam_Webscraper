#include <cstdio>
#include <cmath>
#include <map>
#include <deque>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
#define FOR(i,a,b) for (int i(a); i <= b; ++i)

void Next(int N,vector<int>&X,bool&y)
{
	int j,i=N-1;
	while ((i>0)&&(X[i-1]>X[i])) --i;
	if (i>0)
	{
		j=i+1;
		while ((j<N)&&(X[j]>X[i-1])) ++j;
		swap(X[i-1],X[j-1]);
		for (j=i+1;j<=((N+i)/2);++j) swap(X[j-1],X[N-j+i]);
		y=true;
	}else
		y=false;
}

int permrle(int k, int C,const std::string&s,const vector<int>&X)
{
	std::string a=s;
	for (int i=0;i<C;++i)
	{
		for (int j=0;j<X.size();++j)
		{
			a[X[j]+k*i]=s[j+k*i];
		}
	}

	int n=0;
	char c=0;
	for (int i=0;i<a.length();++i)
	{
		if (c!=a[i]){++n;c=a[i];}
	}
	return n;
}

int Compress(int k, const std::string&s)
{
	bool y;
	vector<int> X;
	for (int i=0;i<k;++i) X.push_back(i);
	int t,M=s.length();
	int C=s.length()/k;

	do 
	{
		t=permrle(k,C,s,X);
		if (t<M) M=t;
		Next(k,X,y);
	} while (y);

	return M;
}

void main()
{
	int nCases,k;
	char buf[80000];
	scanf("%d", &nCases);
	FOR(nCase,1,nCases)
	{
		scanf("%d\n",&k);
		gets(buf);
		printf("Case #%d: %d\n",nCase,Compress(k,buf));
	}
}
