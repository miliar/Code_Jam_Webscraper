#include <iostream>
#include <algorithm>
using namespace std;

/*
    n - number of googlers
    s - surprising triplets
    p - a better or equal result to compare
    ti - result of the googlers
    nCase - the case count
    iCase - the current case
*/

void solveCase(int iCase)
{
    int n, s, p, ans = 0;
    scanf("%d %d %d", &n, &s, &p);
    for (int i=0; i<n; i++)
    {
        int current;
        scanf("%d", &current);
        int left = current - p;
        int p2 = p << 1;
        if(left < 0) continue;
        if (left >= p2 - 2){
            ans++;
        } 
        else if (left >= p2 - 4 && s>0){            
            ans++;
            s--;
        }
    }
    printf("Case #%d: %d\n", iCase, ans);
}

/*
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int nCase, iCase;
    scanf("%d", &nCase);
    for (iCase = 1; iCase <= nCase; iCase++) {
        solveCase(iCase);
    }
}
*/