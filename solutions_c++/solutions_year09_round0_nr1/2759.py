#include<stdio.h>
#include<string.h>
#include<stdlib.h>

typedef struct atree{
    //int n;
    struct atree *next[26];
} _ATREE, * ATREE;

void insert(ATREE *a, char *s)
{
    if(!(*s))
	{
		*a = (ATREE) malloc(sizeof(_ATREE));
        memset(*a, 0, sizeof(_ATREE));
        //(*a)->n = 1;
	}
    else if(*a==NULL)
    {
        *a = (ATREE) malloc(sizeof(_ATREE));
        memset(*a, 0, sizeof(_ATREE));
        //(*a)->n = 1;
        insert(&((*a)->next[*s-'a']), s+1);       
    }
    else
    {
        //(*a)->n++;
        insert(&((*a)->next[*s-'a']), s+1);       
    }
}

int count(ATREE a, char *s)
{
	if(a == NULL) return 0;
    else if(!(*s)) return 1;
    else if(*s != '(')
    {
        return count(a->next[*s-'a'], s+1);
    }
    else
    {
         int c=0;
         char *t = ++s;
		 while(*t != ')') t++;

         while(s<t)
         {
			 c += count (a->next[*s-'a'], t+1);
			 s++;
         }
         return c;
    }
}

void main()
{
	freopen ("input.txt","r", stdin);
	freopen ("output.txt","w", stdout);
	
	ATREE a = NULL;
	int i, L, D, N;
	char s[256];
	scanf("%d %d %d", &L, &D, &N);
	for(i=0; i<D;i++) {scanf("%s", s); insert(&a, s);}
	for(i=1; i<=N; i++)
	{
		scanf("%s", s);
		printf("Case #%d: %d\n", i, count(a, s));
	}
}

