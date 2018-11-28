#include <cstdio>
#include <cstring>
#include <cassert>

int tests, n, l, len, ind, next_v, q, f;
char buf[1024], t[10000];

char name[10000][20];
bool last[10000];
int left[10000];
int right[10000];
double w[10000];
char fe[100][20];

double get_double()
{
	int k = 0;
	
	while (t[ind] == ' ') ind++;
	
	while (t[ind] != ' ' && t[ind] != ')') buf[k++] = t[ind++];
	
	buf[k] = '\0';
	
	double res;
	sscanf(buf, "%lf", &res);
	
	return res;
}

void get_name(int v)
{
	int k = 0;
	
	while (t[ind] == ' ') ind++;
	
	while (t[ind] != ' ' && t[ind] != ')') name[v][k++] = t[ind++];
	
	name[v][k] = '\0';
}

int czytaj()
{
	int v = next_v++;
	
	while (t[ind] == ' ') ind++;
	
	//printf("* %d %d\n", v, ind);
	assert(t[ind] == '(');
	ind++;
	
	w[v] = get_double();
	//printf("- %d\n", ind);
	
	while (t[ind] == ' ') ind++;
	
	if (t[ind] == ')')
	{
		last[v] = true;
		ind++;
	}
	else
	{
		last[v] = false;
		
		get_name(v);
		left[v] = czytaj();
		right[v] = czytaj();
		
		while (t[ind] == ' ') ind++;
		
		assert(t[ind] == ')');
		ind++;
	}
	
	//printf("done\n");
	return v;
}

bool has_fe_num(int v)
{
	for (int i = 0; i < f; i++)
		if (strcmp(fe[i], name[v]) == 0)
			return true;
	return false;
}

double calc(int v, double prob)
{
	prob *= w[v];
	
	if (last[v])
		return prob;
	else
	{
		if (has_fe_num(v))
			return calc(left[v], prob);
		else
			return calc(right[v], prob);
	}
}

int main()
{
	scanf("%d", &tests);
	for (int tc = 0; tc < tests; tc++)
	{
		printf("Case #%d:\n", tc + 1);
		
		n = 0;
		
		scanf("%d\n", &l);
		for (int i = 0; i < l; i++)
		{
			fgets(buf, 1024, stdin);
			
			len = strlen(buf);
			
			for (int j = 0; j < len; j++)
				t[n++] = buf[j];
			
			t[n - 1] = ' ';
		}
		
		// debug code
		/*for (int i = 0; i < n; i++)
			printf("%c", t[i]);
		printf("\n");*/
		
		ind = 0;
		next_v = 0;
		czytaj();
		
		scanf("%d", &q);
		for (int i = 0; i < q; i++)
		{
			scanf("%s %d", buf, &f);
			for (int j = 0; j < f; j++)
				scanf("%s", fe[j]);
			
			printf("%.7lf\n", calc(0, 1.0));
		}
	}
		
	return 0;
}