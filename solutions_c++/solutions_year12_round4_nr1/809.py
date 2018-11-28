#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 10010;

struct node{
    int d,l,b;
};

node p[MAXN];
int n, d;


bool check(){
	p[1].b = p[1].d;
	for(int i=1;i<=n;++i)
	{
		if(p[i].d + p[i].b >= d){
			return true;
		}
		for(int j = i + 1; j <= n && (p[j].d - p[i].d) <= p[i].b; ++ j)
		{
			p[j].b = max(p[j].b, min(p[j].d - p[i].d, p[j].l));
		}
	}

	return false;
}

int main()
{   int T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t ++)
    {
        scanf("%d",&n);
        for(int i = 1; i <= n;i ++)
        {
            scanf("%d%d",&p[i].d, &p[i].l);
            p[i].b = 0;
        }
        scanf("%d", &d);        
        printf("Case #%d: ",t);
        if(check())
			printf("YES\n");
        else 
			printf("NO\n");
    }
    return 0;
}

