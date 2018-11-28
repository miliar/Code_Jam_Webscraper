#include <stdio.h>
#include <string.h>

int n;
int s;
int q;
int count;
char engine[110][110];
char query[1010][110];
int i,j;
bool shown[110];
int pos;
int curEng;
int ans;

int Solve()
{
	for(i = 0; i < q; i++)
	{
		
	}
}

int Check(char *qry)
{
	for(j = 0; j < s; j++)
	{
		if(strcmp(qry, engine[j]) == 0)
		{
			shown[j] = true;
			return j;
		}
	}
}

bool AllShown()
{
	int x;
	for(x = 0; x < s; x++)
	{
		if(!shown[x])
		{
			return false;
		}
	}
	
	return true;
}

void SetShown(int p)
{
	int x;
	for(x = 0; x < s; x++)
	{
		if(x == p)
			continue;
		
		shown[x] = false;
	}
}

int main()
{
	scanf("%d", &n);
	
	FILE *out;
	
	out = fopen("F:\\out.txt", "r+");
	
	for(count = 1; count <= n; count++)
	{
		curEng = -1;
		ans = 0;
		
		scanf("%d", &s);
		
		scanf("%c", &engine[0][0]);
		
		for(i = 0; i < s; i++)
		{
			gets(engine[i]);
			shown[i] = false;
		}
		
		scanf("%d", &q);
		scanf("%c", &query[0][0]);
		
		for(i = 0; i < q; i++)
		{
			gets(query[i]);
		}
		
		for(i = 0; i < q; i++)
		{
			pos = Check(query[i]);
			
			if(AllShown())
			{
				ans++;
				SetShown(pos);
			}
		}
		
		fprintf(out, "Case #%d: %d\n", count, ans);
		//printf("Case #%d: %d\n", count, ans);
	}
	
	return 0;
}