#include <vector>
#include <stdio.h>
#include <list>
using namespace std;
int ans[1000000];

int main()
{
    int Q;
    scanf("%d\n", &Q);
    for (int q = 0; q < Q; q++)
    {
    printf("Case #%d:", q + 1);
    
    
    int K, n;
    int d[100];
    scanf("%d%d\n", &K, &n);
    for (int i = 0; i < n; i++) scanf("%d", &d[i]);
    
    vector<int> l;
    for (int i = 0; i < K; i++) l.push_back(i);
    
    int pos = 0;
    for (int i = 1; i <= K; i++)
    {
        int next = (pos + i - 1)%l.size();
        //printf("%d %d %d\n", i, pos, next);
        //system("pause");
        
        ans[ l[next] ] = i;
        l.erase( l.begin() + next );
        if (l.size()) pos = next%l.size();
    }
    for (int i = 0; i < n; i++) printf(" %d", ans[ d[i] - 1]);
    printf("\n");
    
    
    }
    return 0;
}
