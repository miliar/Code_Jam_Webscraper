#include <stdio.h>
#include <string.h>

#define MAX_S 110
char engines[MAX_S][110];
int S, Q, hits, ans;
bool hit[MAX_S];

void readS(void)
{
	scanf("%d\n", &S);
	for(int i=0;i<S;i++)
	{
		gets(&engines[i][0]);
		scanf("\n");
	}

	/*for(int i=0;i<S;i++)
	{
		printf("%s\n", engines[i]);
	}*/
}

void clearHit(void)
{
	for(int i=0;i<S;i++)
		hit[i]=0;
}

int findS(char *p)
{
	for(int i=0;i<S;i++)
		if(strcmp(engines[i], p)==0) return i;
	return -1;
}

void readQ(void)
{
	char query[110];

	clearHit();
	ans=hits=0;

	scanf("%d\n", &Q);
	for(int i=0;i<Q;i++)
	{
		gets(query);
		scanf("\n");
		int sid=findS(query);
		if(hit[sid]==0)
		{
			hits++; 
			hit[sid]=1;
		}
		if(hits==S)
		{
			ans++;
			clearHit();
			hits=1;
			hit[sid]=1;
		}
	}

}

int main()
{
  //#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
  //#endif
	freopen ("myfile.txt","w",stdout);
	int cases;
	scanf("%d\n", &cases);

	for(int i=1;i<=cases;i++)
	{
		readS();
		readQ();
		  
		printf("Case #%d: %d\n", i, ans);
		
	}
	fclose (stdout);
	return 0;
}