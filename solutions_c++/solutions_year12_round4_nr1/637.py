#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int SIZE = 10009;
int ls[SIZE];
int ds[SIZE];
int N;
int D;
int table[SIZE];

int main()
{    
    int T;
    scanf("%d", &T);
    for(int testnum = 1; testnum <= T; testnum++)
    {
	printf("Case #%d: ", testnum);


        memset(table, -1, sizeof(table));
	scanf("%d", &N);
	for(int i = 1; i <= N; i++)
	    scanf("%d%d", ds + i, ls + i);

	
	scanf("%d", &D);

	bool ans = false;
	table[1] = 0;
	for(int i = 1; i <= N; i++)
	    if(table[i] >= 0)
   	    {  
	        for(int j = i + 1; j <= N; j++)
		    if(ds[j] > ds[i] + min(ds[i] - ds[table[i]], ls[i]))
			break;
		    else
			if(table[j] == -1)
			    table[j] = i;	    
		if(ds[i] + min(ls[i], ds[i] - ds[table[i]]) >= D)
		    ans = true;
	    }
	puts(ans? "YES": "NO");

    }

    return 0;
}
