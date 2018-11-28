#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>

using namespace std;

int main()
{
    int n;
    int i, j;
    int a, b;
    int teste, nteste;
    scanf("%d", &nteste);
    long long resp;
    for (teste = 0; teste < nteste; teste++)
    {
        scanf("%d", &n);
        map<int, int> vendor;
        bool ok = true;
        for (i=0; i<n; i++)
        {
            scanf("%d %d", &a, &b);
            vendor[a] = b;
            if (b > 1)
            {
                ok = false;
            }
        }
        resp = 0;
        map<int,int>::iterator it;
        while(ok == false)
        {
            ok = true;
            for ( it=vendor.begin() ; it != vendor.end(); it++ )
            {
                int pos = (*it).first;
                int qnt = (*it).second;
                if (qnt > 1)
                {
                    int dist = qnt/2;
                    resp += dist;
                    vendor[pos] = (qnt & 1);
                    if (vendor.count(pos-1) == 0)
                    {
                        vendor[pos-1] = dist;
                        if (dist > 1)
                            ok = false;
                    }
                    else
                    {
                        int value = vendor[pos-1] + dist;
                        vendor[pos-1] = value;
                        if (value > 1)
                            ok = false;
                    }
                    if (vendor.count(pos+1) == 0)
                    {
                        vendor[pos+1] = dist;
                        if (dist > 1)
                            ok = false;
                    }
                    else
                    {
                        int value = vendor[pos+1] + dist;
                        vendor[pos+1] = value;
                        if (value > 1)
                            ok = false;
                    }
                }
            }
        }
        printf("Case #%d: %I64d\n", teste + 1, resp);
    }
    return 0;
}
