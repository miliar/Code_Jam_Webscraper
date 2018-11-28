#include<cstdio>
#include<set>
#include<string>

using namespace std; 

int ns, nq;
string engine[102];
string query[1002];
set<string> rec;

int startOver(int ind)
{
	rec.clear();
	int cnt=0;
	for(int i=ind; i<nq; ++i)
	{
		if(rec.find(query[i]) == rec.end())
		{
			cnt++;
			rec.insert(query[i]);
			if(cnt==ns)
				return i;
		}
	}
	return nq;
}

int solve()
{
	rec.clear();
	int val=0;
	int ret=0;
	while(val<nq)
	{
		val=startOver(val);
		if(val<nq)
			ret++; 
	}
	return ret;
}

int main()
{
	freopen("A-Large.in", "r", stdin);  
	freopen("large.out", "w", stdout);

	char buf[102];
	int numCase;
	scanf("%d", &numCase);
	for(int c=0; c<numCase; ++c)
	{
		scanf("%d", &ns);
		getchar();
		for(int i=0; i<ns; ++i)
		{
			gets(buf);
			engine[i]=string(buf);
		}
		scanf("%d", &nq);
		getchar();
		for(int i=0; i<nq; ++i)
		{
			gets(buf);
			query[i]=string(buf);
		}
		int ret=solve();
		printf("Case #%d: %d\n", c+1, ret);	
	}
}
