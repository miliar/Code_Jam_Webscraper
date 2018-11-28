#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdlib.h>
#include <list>

using namespace std;

/*
bool isPrime[];

void prime(int n)
{
    int i,j,end;

    memset(isPrime,true,sizeof(isPrime));

    end = sqrt(n) +1;
    for (i=2; i<end; i++)
        if (isPrime[i]) {
            for(j=i*2; j<1001; j+=i)
                isPrime[j] = false;
        }
}
*/

#define for0(i,n)  for ((i)=0; (i)<(n); (i++))
#define for1(i,n)  for ((i)=1; (i)<=(n); (i++))
#define foriter(i,v)  for ((i)=(v).begin(); (i)!=(v).end(); (i)++)

bool graph[1001][1001], visit[1001];
int n;

bool go(int index)
{
    if (visit[index])
        return true;

    visit[index] = true;
    int i;
    for1(i,n)
        if (graph[index][i])
            if (go(i))
                return true;
    return false;
}

int main()
{
    int i,j,k,T,tt;
    int x,y;

    scanf("%d", &T);

    for0(tt,T) {
        scanf("%d", &n);
        memset(graph, 0, sizeof(graph));

        for1(i,n) {
            scanf("%d", &x);
            for0(j,x) {
                scanf("%d", &y);
                graph[i][y] = 1;
            }
        }

        bool ans = false;
        for1(i,n) {
            memset(visit, 0, sizeof(visit));
            if (go(i)) {
                ans = true;
                break;
            }
        }

        printf("Case #%d: ", tt+1);
        if (ans)
            printf("Yes\n");
        else
            printf("No\n");
    }
}
