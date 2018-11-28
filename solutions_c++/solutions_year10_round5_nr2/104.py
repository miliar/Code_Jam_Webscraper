#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>

using namespace std;

long long best[1001000];

int main()
{
    int teste, nteste;
    scanf("%d", &nteste);
    long long resp;
    long long l;
    int n;
    vector<int> size;
    int a;
    int i, j;
    for (teste = 0; teste < nteste; teste++)
    {
        scanf("%I64d %d", &l, &n);
        size.clear();
        for (i=0; i<n; i++)
        {
            scanf("%d", &a);
            size.push_back(a);
        }
        sort(size.begin(), size.end());

        for (i=0; i<1001000; i++)
        {
            best[i] = -1;
        }
        best[0] = 0;
        
        for (i=0; i<n-1; i++)
        {
            for (j = size[i]; j<1001000; j++)
            {
                if (best[j-size[i]] == -1)
                    continue;
                long long aux = best[j-size[i]] + 1;
                if (best[j] == -1 || best[j] > aux)
                {
                    best[j] = aux;
                }
            }
        }
        resp = -1;
        for (i=l%size[n-1]; i<1001000; i+=size[n-1])
        {
            if (best[i] == -1)
                continue;
            long long aux = best[i] + (l - i)/size[n-1];
            if (resp == -1 || resp > aux)
                resp = aux;
        }
        if (resp != -1)
            printf("Case #%d: %I64d\n", teste + 1, resp);
        else
            printf("Case #%d: IMPOSSIBLE\n", teste + 1);
    }
    return 0;
}
