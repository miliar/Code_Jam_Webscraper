
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

#define MAX 128

struct no
{
	map<string, no*> fil;
};

int res;

no* raiz;

void add(no* x, char* path)
{
	if(*path == 0) return;

//	printf("adicionar %s\n", path);

	char buf[MAX];
	char* next = strchr(path,'/');
	strncpy(buf, path, next-path);
	buf[next-path] = 0;

	map<string, no*>::iterator it = x->fil.find(buf);
	if(it == x->fil.end())
	{
//		printf("  cria %s\n", buf);
		res++;
		x->fil[buf] = new no;
		it = x->fil.find(buf);
	}
	
	add(it->second, next+1);
}

int main(void)
{
	int nc, ca;
	int n, m, i;
	char buf[MAX];

	scanf("%d", &nc);
	for(ca=1; ca<=nc; ca++)
	{
		printf("Case #%d: ", ca);

		raiz = new no;

		scanf("%d %d", &n, &m);
		for(i=0; i<n; i++)
		{
			scanf("%s", buf);
			strcat(buf, "/");
			add(raiz, buf+1);
		}

		res = 0;
		for(i=0; i<m; i++)
		{
			scanf("%s", buf);
			strcat(buf, "/");
			add(raiz, buf+1);
		}

		printf("%d\n", res);
	}

	return 0;
}
