#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
using namespace std;

typedef struct  
{
	__int64 len;
	__int64 num[1010];
}Info;
Info key[1010];

__int64 hash[1010];

bool operator <(const Info &a,const Info &b)
{
	return a.len>b.len;
}

priority_queue<Info> q; 

FILE *fp1,*fp2;

int main()
{
	fp1=fopen("A.in","r");
	fp2=fopen("A.out","w");

	long T;
	fscanf(fp1,"%ld",&T);

	long f=1;
	while (T--)
	{

		memset(key,0,sizeof(key));
		long P,K,L;
		fscanf(fp1,"%ld %ld %ld",&P,&K,&L);

		long i;

		for (i=0;i<L;++i)
		{
			fscanf(fp1,"%I64d",&hash[i]);
		}

		sort(hash,hash+L,greater<__int64>());

		for (i=0;i<K;++i)
		{
			q.push(key[i]);
		}


		Info t;
		bool finish=true;
		for (i=0;i<L;++i)
		{
			t=q.top();
			q.pop();
			if (t.len>P)
			{
				finish=false;
				break;
			}
			else
			{
				t.num[t.len]=hash[i];
				++t.len;
				q.push(t);
			}
		}

		if (!finish)
		{
			while (!q.empty())
			{
				q.pop();
			}
			fprintf(fp2,"Impossible\n");
		}
		else
		{
			__int64 ct=0;
			while (!q.empty())
			{
				Info t=q.top();
				for (i=0;i<t.len;++i)
				{
					ct+=(i+1)*t.num[i];
				}
				q.pop();
			}
			fprintf(fp2,"Case #%ld: %I64d\n",f,ct);
		}
		++f;
	}

	fclose(fp1);
	fclose(fp2);
	return 0;
}