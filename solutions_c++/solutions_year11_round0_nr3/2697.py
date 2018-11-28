#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;
int t;
int cas;
int n;
//int value[1010];
long long ans;
vector <int> value;

FILE *fin;
FILE *fout;

void init()
{
	int i;
	int t;
	ans = 0;
	value.clear();
	fscanf(fin,"%d",&n);
	for(i = 1;i <= n;i++)
	{
		fscanf(fin,"%d",&t);
		value.push_back(t);
	}
	
	stable_sort(value.begin(),value.end());
	
}

void work()
{
	int res = 0;
	vector <int>::iterator it;
	
	for(it = value.begin();it != value.end();it ++)
	{
		res ^= *it;
	}
	
	if(res)
		ans = -1;
	else
	{
		ans = 0;
		for(it = value.begin()+1;it != value.end();it++)
		{
			ans += *it;
		}
	}
		

}


int main()
{
	fin = fopen("C-large.in","rb");
	fout = fopen("c.out","wb");
	fscanf(fin,"%d",&t);
	for(cas = 1;cas <= t;cas++)
	{
		init();	
		work();
		if(ans == -1)
		{
			printf("Case #%d: NO\n",cas);
			fprintf(fout,"Case #%d: NO\n",cas);
		}
		else
		{
			printf("Case #%d: %lld\n",cas,ans);
			fprintf(fout,"Case #%d: %lld\n",cas,ans);
		}
	}	
	
	return 0;
}
