#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<queue>
#include<fstream>
#define MAXN 10010
int N, L, M;

int n[MAXN];


int main()
{
    int datacase;
    int t = 0;;
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &datacase);
    while( datacase--)
    {
        memset(n, 0, sizeof(n));
        scanf("%d%d%d", &N, &L, &M);
        for(int i = 0;i < N; i++){
            scanf("%d", &n[i]);
        }

        bool isok = false;
        int ans;
        for(int i = L;i <= M; i++)
		{
            bool i_isok = true;
            for(int j = 0;j < N; j++)
			{
				int b, s;
				if( i > n[j] )
					b = i;
				else
					b = n[j];
				if( i < n[j] )
					s = i;
				else
					s = n[j];
                if((b % s) != 0)
				{
                    i_isok = false;
                    break;
                }
            }
            if(i_isok){
                ans = i;
                isok = true;
                break;
            }
        }

        if(isok)
            printf("Case #%d: %d\n", ++t, ans);
        else
            printf("Case #%d: NO\n", ++t);

    }
    return 0;
}
