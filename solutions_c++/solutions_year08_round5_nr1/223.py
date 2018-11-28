#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
using namespace std;
const int N = 102;

char str[100];

int dx[] = {0,-2,0,2};
int dy[] = {2,0,-2,0};
int dd = 0;
int nowx, nowy;

int row[4 * N][4 * N];
int col[4 * N][4 * N];
int rowsum[4 * N];
int colsum[4 * N];
bool vis[4 * N][4 * N];

int lowbit(int x){
    return x&-x;
}

void add(int i,int v, int *a){
    while(i<4 * N){
        a[i]+=v;
        i+=lowbit(i);
    }
}

int sum(int i, int *a){
    int s=0;
    while(i>0){
        s+=a[i];
        i-=lowbit(i);
    }
    return s+a[0];
}


int main()
{
    int i, j, k, t, T, n, res;
    int num, tmp;
    int times;
    
    scanf("%d", &T);
    //freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    for (t = 1; t <= T; t++)
    {
        res = 0;
        memset(row, 0, sizeof(row));
        memset(col, 0, sizeof(col));
        memset(rowsum, 0, sizeof(rowsum));
        memset(colsum, 0, sizeof(colsum));        
        scanf("%d", &n);
        
        nowx = N * 2; nowy = N * 2;
        for (i = 0; i < n; i++)
        {
            scanf("%s%d", str, &times);
            while (times--)
            {
                for (j = 0; str[j] ; j++)
                {
                    if (str[j] == 'L')
                    {
                        dd++;
                        if (dd == 4) dd = 0;
                        if (dd == -1) dd = 3;
                        continue;
                    }    
                    else if (str[j] == 'R')
                    {
                        dd--;
                        if (dd == 4) dd = 0;
                        if (dd == -1) dd = 3;
                        continue;
                    }    
                    

                    //printf("{%d, %d},\n", nowx, nowy);
                    if (dx[dd] == 0)
                    {
                        add(nowx, 1, col[nowy + dy[dd]/2]);
                        colsum[nowy + dy[dd]/2]++;
                    }    
                    else
                    {
                        add(nowy, 1, row[nowx + dx[dd]/2]);
                        rowsum[nowx + dx[dd]/2]++;
                    }    
                    
                    nowx += dx[dd];
                    nowy += dy[dd];
                }    
            }    
        }
        num = 0;

        for (i = 1; i < 4 * N; i+=2)
        {
            for (j = 1; j < 4 * N; j+=2)
            {
                tmp = sum(j, row[i]);
                if (tmp > 0 && tmp % 2 == 0 && tmp < rowsum[i])
                {
                    res++;
                //    printf("%d %d\n", i, j);
                    continue;
                }  
                tmp = sum(i, col[j]);
                if (tmp > 0 && tmp % 2 == 0 && tmp < colsum[j])
                {
                    res++;
                //    printf("%d %d\n", i, j);
                    continue;
                }   
            }
        }    
       
        printf("Case #%d: %d\n", t, res);
    }   
    return 0; 
}    

