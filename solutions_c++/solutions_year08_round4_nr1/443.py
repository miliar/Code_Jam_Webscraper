#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

struct in
{
	int g;
	int c;
};
in k[20000];
int m;
int min(int a,int b)
{
	if(a == -1)
		return b;
	if(b == -1)
		return a;
	return a>b?b:a;
}
int get(int now, int v)
{
	if(now>=m/2)
		return k[now].g==v?0:-1;
	int re1,re2;
	int re;
	//not change
	if(v == 1 && k[now].g == 1)
	{
		re1=get( (now+1)*2-1 , 1);
		re2=get( (now+1)*2 , 1);
		if(re1 ==-1||re2==-1)
		re = -1;
		else 
			re = re1 + re2;
	}
	else if(v == 0 && k[now].g == 1)
	{
		re1=get( (now+1)*2-1 , 0);
		re2=get( (now+1)*2 , 0);
		if(re1 ==-1 && re2==-1)
		re = -1;
		else
			re = min(re1 , re2);
	}
	else if(v == 1 && k[now].g == 0)
	{
		re1=get( (now+1)*2-1 , 1);
		re2=get( (now+1)*2 , 1);
		if(re1 ==-1 && re2==-1)
		re = -1;
		else
			re = min(re1 , re2);
	}
	else if(v == 0 && k[now].g == 0)
	{
		re1=get( (now+1)*2-1 , 0);
		re2=get( (now+1)*2 , 0);
		if(re1 ==-1||re2==-1)
		re = -1;
		else
			re = re1 + re2;
	}
	int notre = re;
	if(k[now].c == 1)
	{
		k[now].g = 1 - k[now].g;
		if(v == 1 && k[now].g == 1)
		{
			re1=get( (now+1)*2-1 , 1);
			re2=get( (now+1)*2 , 1);
			if(re1 ==-1||re2==-1)
			re = -1;
			else
				re = re1 + re2 + 1;
		}
		else if(v == 0 && k[now].g == 1)
		{
			re1=get( (now+1)*2-1 , 0);
			re2=get( (now+1)*2 , 0);
			if(re1 ==-1&&re2==-1)
			re = -1;
			else
				re = min(re1 , re2) + 1;
		}
		else if(v == 1 && k[now].g == 0)
		{
			re1=get( (now+1)*2-1 , 1);
			re2=get( (now+1)*2 , 1);
			if(re1 ==-1&&re2==-1)
			re = -1;
			else
				re = min(re1 , re2) + 1;
		}
		else if(v == 0 && k[now].g == 0)
		{
			re1=get( (now+1)*2-1 , 0);
			re2=get( (now+1)*2 , 0);
			if(re1 ==-1||re2==-1)
			re = -1;
			else
				re = re1 + re2 + 1;
		}
		k[now].g = 1 - k[now].g;
	}
	return min(notre,re);
	
	
}

int main()
{
	ifstream fin ("A-large.in");
	ofstream fout ("test.out");

	int i,j;
	
	int n,cases;
	

	fin>>n;
	int t;
	
	for(cases = 1; cases <= n; cases++)
	{
		fin>>m>>t;
		for(i=0;i<(m/1)/2;i++)
			fin>>k[i].g>>k[i].c;

		for(i=m/2;i<m;i++)
			fin>>k[i].g;

		int re = get(0,t);

		if(re == -1)
			fout<<"Case #"<<cases<<": "<< "IMPOSSIBLE"<<endl;			

		else
			fout<<"Case #"<<cases<<": "<< re <<endl;
	}

}
