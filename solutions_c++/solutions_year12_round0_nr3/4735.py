#include <cstdio>
#include <cstring>
using namespace std;

int a, b, t, c;

int ndig(int num)
{
    if(num==0) return 1;
    int r = 0;
    while(num>0) {
        r++;
        num /= 10;
    }
    return r;
}

bool isR(int n, int m)
{
    int aux;
    char nm[10];
    sprintf(nm, "%d", m);
    int tam = strlen(nm);
    char ult;
    for(int i=0; i<tam; i++) {
        ult = nm[tam-1];
        for(int j=tam-1; j>0; j--)
            nm[j] = nm[j-1];
        nm[0] = ult;
        sscanf(nm, "%d", &aux);
        if(aux==n)
            return true;
    }
    return false;
}

bool isRecycled(int n, int m) {
    int aux = m;
    int d;
    bool res = false;
    int digm = ndig(m);
    int dig = ndig(m) - 1;
    while(digm>0 && !res) {
        d = m % 10;
        m /=10;
        dig = ndig(m);
        while(dig--)
            d *= 10;
        m += d;
        res = (m==n);
        digm--;
        //printf("n=%d, m=%d\n", n, m);
    }
    //printf("fin\n");
    return res;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &t);
    for(int p=0; p<t; p++) {
        c = 0;
        scanf("%d %d", &a, &b);

        for(int j=a; j<=b; j++)
        {
            for(int k=j+1; k<=b; k++)
            {
                //printf("%d, %d\n", j, k);
                if(isR(j, k)) {
                    c++;
                }
            }
        }
        printf("Case #%d: %d\n", p+1, c);
    }

    return 0;
}
