#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <string>

using namespace std;

const int N = 10086;

const char table[] = {'y', 'h', 'e', 's', 'o',
                      'c', 'v', 'x', 'd', 'u',
                      'i', 'g', 'l', 'b', 'k',
                      'r', 'z', 't', 'n', 'w',
                      'j', 'p', 'f', 'm', 'a', 'q'
                     };
char A[N];

int main()
{
    freopen("ans.txt", "w", stdout);
    int tcas, cas = 0;
    scanf("%d", &tcas);
    getchar();
    while(tcas --)
    {
        gets(A);
        printf("Case #%d: ", ++cas);
        for(int i = 0; A[i]; i++)
            if(A[i] >= 'a' && A[i] <= 'z')
                printf("%c", table[A[i] - 'a']);
            else printf("%c", A[i]);
        printf("\n");
    }
    return 0;
}
