#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>

using namespace std;

int values[20];
int n;
char prime[1000000];
int limit[7] = {0, 10, 100, 1000, 10000, 100000, 1000000};
int d;

int ipow(int a, int exp, int mod)
{
    if (exp == 0) return 1;
    if (exp == 1) return a;
    long long aux = ipow(a, exp/2, mod);
    long long ret = (aux * aux) % mod;
    if (exp & 1)
    {
        ret = (ret * a) % mod;
    }
    return (int)ret;
}

int cinv(int a, int p)
{
    if (p == 2)
        return a;
    return ipow(a, p-2, p);
}

int main()
{
    int teste, nteste;
    scanf("%d", &nteste);
    long long resp;
    int i, j;
    for (i=0; i<1000000; i++)
    {
        prime[i] = 1;
    }
    prime[0] = prime[1] = 0;
    for (i=4; i<1000000; i+=2)
    {
        prime[i] = 0;
    }
    for (i=3; i<1000000; i+=2)
    {
        if (prime[i] == 0)
            continue;
        for (j=2*i; j<1000000; j+=i)
        {
            prime[j] = 0;
        }
    }
    
    for (teste = 0; teste < nteste; teste++)
    {
        resp = 0;
        scanf("%d %d", &d, &n);
        for (i=0; i<n; i++)
        {
            scanf("%d", &values[i]);
        }
        if (n == 1)
        {
            printf("Case #%d: I don't know.\n", teste + 1);
        }
        else if (n == 2)
        {
            if (values[0] == values[1])
            {
                printf("Case #%d: %d\n", teste + 1, values[0]);
            }
            else
            {
                printf("Case #%d: I don't know.\n", teste + 1);
            }
        }
        else
        {
            if (values[0] == values[1])
            {
                printf("Case #%d: %d\n", teste + 1, values[0]);
            }
            else
            {
                int a, b;
                resp = -1;
                bool unique = true;
                int p = 0;
                for (i=0; i<n; i++)
                {
                    if (p < values[i]) p = values[i];
                }
                p++;
                for (; p < limit[d]; p++)
                {
                    if (prime[p] == 0) continue;
                    //printf("p = %d\n", p);
                    long long aux = (values[1] - values[2] + p) % p;
                    int mm = (values[0] - values[1] + p) % p;
                    int inv = cinv(mm, p);
                    aux = (aux * inv) % p;
                    a = (int)aux;
                    //printf("a = %d\n", a);
                    
                    aux = (((long long)values[0])*((long long)values[2]) - ((long long)values[1])*((long long)values[1])) % p;
                    aux = (aux + p)%p;
                    aux = (aux * inv) % p;
                    b = (int)aux;
                    //printf("inv = %d\n", inv);
                    //printf("b = %d\n\n", b);
                    
                    for (i=1; i<n; i++)
                    {
                        aux = (((long long)values[i-1]) * ((long long)a) + ((long long)b))%p;
                        if (values[i] != aux)
                            break;
                    }
                    if (i<n) continue;
                    aux = (((long long)values[n-1]) * ((long long)a) + ((long long)b))%p;
                    if (resp == -1)
                    {
                        resp = aux;
                    }
                    else if (resp != aux)
                    {
                        unique = false;
                        break;
                    }
                }
                
                if (unique)
                    printf("Case #%d: %I64d\n", teste + 1, resp);
                else
                    printf("Case #%d: I don't know.\n", teste + 1);
            }
        }
    }
    return 0;
}
