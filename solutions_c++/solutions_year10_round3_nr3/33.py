#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T,M,N;
vector <vector <int> > bo;
vector <string> inp;
vector <pair<int,int> > res;

vector <int> reb(string s)
{
	vector <int> r;
	for (int i=0; i<s.size(); i++)
		if (s[i]=='0')
		{
			r.push_back(0);
			r.push_back(0);
			r.push_back(0);
			r.push_back(0);
		}
		else if (s[i]=='1')
		{
			r.push_back(0);
			r.push_back(0);
			r.push_back(0);
			r.push_back(1);
		}
		else if (s[i]=='2')
		{
			r.push_back(0);
			r.push_back(0);
			r.push_back(1);
			r.push_back(0);
		}
		else if (s[i]=='3')
		{
			r.push_back(0);
			r.push_back(0);
			r.push_back(1);
			r.push_back(1);
		}
		else if (s[i]=='4')
		{
			r.push_back(0);
			r.push_back(1);
			r.push_back(0);
			r.push_back(0);
		}
		else if (s[i]=='5')
		{
			r.push_back(0);
			r.push_back(1);
			r.push_back(0);
			r.push_back(1);
		}
		else if (s[i]=='6')
		{
			r.push_back(0);
			r.push_back(1);
			r.push_back(1);
			r.push_back(0);
		}
		else if (s[i]=='7')
		{
			r.push_back(0);
			r.push_back(1);
			r.push_back(1);
			r.push_back(1);
		}
		else if (s[i]=='8')
		{
			r.push_back(1);
			r.push_back(0);
			r.push_back(0);
			r.push_back(0);
		}
		else if (s[i]=='9')
		{
			r.push_back(1);
			r.push_back(0);
			r.push_back(0);
			r.push_back(1);
		}
		else if (s[i]=='A')
		{
			r.push_back(1);
			r.push_back(0);
			r.push_back(1);
			r.push_back(0);
		}
		else if (s[i]=='B')
		{
			r.push_back(1);
			r.push_back(0);
			r.push_back(1);
			r.push_back(1);
		}
		else if (s[i]=='C')
		{
			r.push_back(1);
			r.push_back(1);
			r.push_back(0);
			r.push_back(0);
		}
		else if (s[i]=='D')
		{
			r.push_back(1);
			r.push_back(1);
			r.push_back(0);
			r.push_back(1);
		}
		else if (s[i]=='E')
		{
			r.push_back(1);
			r.push_back(1);
			r.push_back(1);
			r.push_back(0);
		}
		else if (s[i]=='F')
		{
			r.push_back(1);
			r.push_back(1);
			r.push_back(1);
			r.push_back(1);
		}
	return r;
}

bool good (int i, int j, int k)
{
	if (k==1)
	{
		if (bo[i][j]!=2)
		{
			bo[i][j]=2;
			return true;
		}
		else return false;
	}
	else
	{
		bool re;
		int cu=bo[i][j], up=bo[i][j];
		if (cu==2) return false;
		for (int ii=j+1; ii<j+k; ii++)
			if (bo[i][ii]==2) return false;
			else if (bo[i][ii]!=1-cu) return false;
			else cu=bo[i][ii];

		for (int ii=i+1; ii<i+k; ii++)
		{
			if (bo[ii][j]==2) return false;
			if (bo[ii][j]!=1-up) return false;
			up=bo[ii][j];
			cu=bo[ii][j];
			for (int jj=j+1; jj<j+k; jj++)
				if (bo[ii][jj]==2) return false;
				else if (bo[ii][jj]!=1-cu) return false;
				else cu=bo[ii][jj];	
		}
		for (int ii=i; ii<i+k; ii++)
			for (int jj=j; jj<j+k; jj++)
				bo[ii][jj]=2;
		return true;
	}
}




void solve()
{
	bo.clear();
	vector <int> t;
	res.clear();
	for (int i=0; i<inp.size(); i++)
		bo.push_back(reb(inp[i]));
	int cnt;
	for (int k=min(N,M); k>=1;k--)
	{
		cnt=0;
		for (int i=0; i<=M-k; i++)
			for (int j=0; j<=N-k; j++)
				if (good(i,j,k)) cnt++;
		if (cnt!=0)
			res.push_back(make_pair(k,cnt));
	}
}

void write(int i)
{
	printf("Case #%d: %d\n",i, res.size());
	for (int i=0; i<res.size(); i++)
		printf("%d %d\n", res[i].first, res[i].second);


}
int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	char buf[1000];
	string s;


/*	freopen("C-large.in","w",stdout);
	printf("1\n");
	printf("512 512\n");
	string tmp="";
	for (int i=0; i<128; i++)
		tmp+='0';
	for (int i=0; i<512; i++)
		printf("%s\n",tmp.c_str());


*/
	scanf("%d",&T);
	


	for (int i=0; i<T; i++)
	{
		scanf("%d%d",&M, &N);
		gets(buf);
		inp.clear();
		for (int j=0; j<M; j++)
		{
			gets(buf);
			s=buf;
			inp.push_back(s);
		}		
		solve();
		write(i+1);
	}

	return 0;
}
