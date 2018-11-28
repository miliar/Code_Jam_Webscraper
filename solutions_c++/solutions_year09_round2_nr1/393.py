#include <stdio.h>
#include <string.h>

#define NUM_NODE	9000

int numchar, node;
char inp[10000];
char _char[100][20];

double value[NUM_NODE];
char savechar[NUM_NODE][20];
int child[NUM_NODE][2];

void tree_construction(int ind, int str)
{
	int i, len, t;
	double unit;
	
	len = strlen(inp);
	i = str;
	while(inp[i] == ' ' || inp[i] == '\n' || inp[i] == '\r') i++;
	if(inp[i] == '(')
	{
		i++;
		while(inp[i] == ' ' || inp[i] == '\n' || inp[i] == '\r') i++;
		if(inp[i] == '1')
		{
			value[ind] = 1;
			i += 2;
			while('0' <= inp[i] && inp[i] <= '9') i++;
		}
		else
		{
			i += 2;
			unit = 0.1;
			value[ind] = 0;
			while('0' <= inp[i] && inp[i] <= '9')
			{
				value[ind] += (inp[i]-'0') * unit;
				unit *= 0.1;
				i++;
			}
		}
		while(inp[i] == ' ' || inp[i] == '\n') i++;
		if(inp[i] == ')') child[ind][0] = -1;
		else
		{
			t = 0;
			while('a' <= inp[i] && inp[i] <= 'z')
			{
				savechar[ind][t] = inp[i];
				t++;
				i++;
			}
			savechar[ind][t] = '\0';
			child[ind][0] = node++;
			while(inp[i] == ' ' || inp[i] == '\n' || inp[i] == '\r') i++;
			tree_construction(node-1, i);

			t = 1;
			i++;
			while(t > 0)
			{
				if(inp[i] == '(') t++;
				if(inp[i] == ')') t--;
				i++;
			}
			child[ind][1] = node++;
			tree_construction(node-1, i);

		}
	}
}

void process()
{
	int point = 0, i;
	double ans = 1.0;

	while(1)
	{
		ans *= value[point];
		if(child[point][0] < 0)
		{
			printf("%.7f\n", ans);
			break;
		}
		else
		{
			for(i = 0; i < numchar; i++)
				if(!strcmp(_char[i], savechar[point])) break;
			if(i < numchar) point = child[point][0];
			else point = child[point][1];
		}
	}
}

int main()
{
	int z, t, l, i, j, cnt;
	char temp[90];

	t = 1;
	scanf("%d", &z);
	while(z > 0)
	{
		scanf("%d", &l);
		gets(temp);
		cnt = 0;
		for(i = 0; i < l; i++)
		{
			gets(temp);
			strcpy(&inp[cnt], temp);
			cnt += strlen(temp);
		}
		node = 1;
		tree_construction(0, 0);

		printf("Case #%d:\n", t++);
		scanf("%d", &l);
		for(i = 0; i < l; i++)
		{
			scanf("%s %d", temp, &numchar);
			for(j = 0; j < numchar; j++)
				scanf("%s", _char[j]);
			process();
		}
		z--;
	}

	return 0;
}