#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<cstring>
#include<map>
#include<algorithm>
#include<memory.h>

using namespace std;
#define MAXN 1010
typedef long long int Lint;

int N;
int n[MAXN];
int t[MAXN][MAXN];
int maxcount[MAXN];
int chose[MAXN];

void cal2(int c)
{
    int origin = c;
    if(c == 1){
        return;
    }
    for(int i = 2; i <= c; ++i )
	{
        int cnt = 0;
        while((c % i) == 0 && c >= i)
		{
            c = c / i;
            cnt++;
        }
        if(cnt > t[c][i])
            t[c][i] = cnt;
        if(cnt > maxcount[i])
		{
            maxcount[i] = cnt;
            chose[i] = origin;
        }
        if(c == 1)
			return;
    }
}

void cal(int c)
{
    if(c == 1){
        return;
    }
    for(int i = 2; i <= c; i++){
        int cnt = 0;
        while((c % i) == 0 && c >= i){
            c = c / i;
            cnt++;
        }
        if(cnt > n[i])
            n[i] = cnt;
        if(c == 1)return;
    }
}

bool please(int c)
{
    if(c == 1){
        return true;
    }
    for(int i = 2; i <= c; i++){
        int cnt = 0;
        while((c % i) == 0 && c >= i){
            c = c / i;
            cnt++;
        }
        if(cnt > n[i])
            return false;
        if(c == 1)return true;
    }
    return true;
}


int main()
{
    int ttt;
    int casenum = 1;
    freopen("C-small-attempt1.in", "r", stdin);
    freopen("ccc.out", "w", stdout);
    scanf("%d", &ttt);
    while(ttt--)
    {
        scanf("%d", &N);
        memset(t, 0, sizeof(t));
        memset(maxcount, 0, sizeof(maxcount));
        memset(chose, 0, sizeof(chose));
        for(int i = 1; i <= N; i++){
            cal2(i);
        }

        int big = 0;
        int small = 0;
        bool check = true;
        memset(n, 0, sizeof(n));

        for(int i = 1; i <= N; i++){
            if(maxcount[i] == 0)continue;
            if(please(chose[i]) && !check)continue;
            check = false;

            small++;
            cal(chose[i]);
            //cout<<chose[i]<<endl;
        }

        for(int i = N; i >= 1; i--){
            if(please(i) && !check)continue;
            check = false;
            small++;
            cal(i);
            //cout<<i<<endl;
        }

        check = true;
        memset(n, 0, sizeof(n));
        for(int i = 1; i <= N; i++){
            //if(used[i])continue;
            if(please(i) && !check)continue;
            check = false;
            big++;
            cal(i);
            //cout<<" "<< i<<endl;
        }

        //cout<<small<<" "<<big<<endl;

        printf("Case #%d: %d\n", casenum++, big - small);

    }
    return 0;
}
