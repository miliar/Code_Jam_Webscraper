#include<stdio.h>
#include <algorithm>
#include <cstring>
#include <queue>
#include <vector>
#include <iostream>
#include <map>
#include <stdlib.h>
using namespace std;
#define eps 1e-8
#define inf 0x7f7f7f7f
#define LL long long
#define MOD 1000000007
#define MAXN 20
#define MAXK 110
#include <string>
#include <queue>
#include <ctime>
int m, n;

char data[5][5];

int main()
{
   // freopen("input.txt", "r", stdin);
   // freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    int cas = 0;
    while(t--)
    {
        for(int i = 0; i < 4; ++i)
        {
            //for(int j = 0; j < 4; ++j)
            //{
                scanf("%s", data[i]);

        }
        int cntt = 0;
        int cntx = 0;
        int cnto = 0;
        int cntd = 0;
        int flg = 0;
        for(int i = 0; i < 4; ++i)
        {
            cntt = 0;
            cntx = 0;
            cnto = 0;
            for(int j = 0; j < 4; ++j)
            {
                if(data[i][j] == 'X') ++cntx;
                if(data[i][j] == 'T') ++cntt;
                if(data[i][j] == 'O') ++cnto;
            }
            cntd += 4 - cntx - cntt - cnto;
            if(cntx == 4 || cntx == 3 && cntt == 1)
            {
                flg = 1;
                break;
            }
            if(cnto == 4 || cnto == 3 && cntt == 1)
            {
                flg = 2;
                break;
            }
        }
        if(flg == 0 && cntd != 0) for(int j = 0; j < 4; ++j)
        {
            cntt = 0;
            cntx = 0;
            cnto = 0;
            for(int i = 0; i < 4; ++i)
            {
                if(data[i][j] == 'X') ++cntx;
                if(data[i][j] == 'T') ++cntt;
                if(data[i][j] == 'O') ++cnto;
            }
            //cntd += 4 - cntx - cntt - cnto;
            if(cntx == 4 || cntx == 3 && cntt == 1)
            {
                flg = 1;
                break;
            }
            if(cnto == 4 || cnto == 3 && cntt == 1)
            {
                flg = 2;
                break;
            }
        }
        if(flg == 0 && cntd != 0)
        {
            cntt = 0;
            cntx = 0;
            cnto = 0;
            for(int i = 0; i < 4; ++i)
            {
                if(data[i][i] == 'X') ++cntx;
                if(data[i][i] == 'T') ++cntt;
                if(data[i][i] == 'O') ++cnto;
            }
            if(cntx == 4 || cntx == 3 && cntt == 1)
            {
                flg = 1;
                //break;
            }
            if(cnto == 4 || cnto == 3 && cntt == 1)
            {
                flg = 2;
                //break;
            }
        }
        if(flg == 0 && cntd != 0)
        {
            cntt = 0;
            cntx = 0;
            cnto = 0;
            for(int i = 0; i < 4; ++i)
            {
                if(data[i][3 - i] == 'X') ++cntx;
                if(data[i][3 - i] == 'T') ++cntt;
                if(data[i][3 - i] == 'O') ++cnto;
            }
            if(cntx == 4 || cntx == 3 && cntt == 1)
            {
                flg = 1;
                //break;
            }
            if(cnto == 4 || cnto == 3 && cntt == 1)
            {
                flg = 2;
                //break;
            }
        }
        if(flg == 1)
        {
            printf("Case #%d: X won\n", ++cas);
        }
        else if(flg == 2)
        {
            printf("Case #%d: O won\n", ++cas);
        }
        else if(cntd == 0)
        {
            printf("Case #%d: Draw\n", ++cas);
        }
        else
        {
            printf("Case #%d: Game has not completed\n", ++cas);
        }
    }
    return 0;
}
