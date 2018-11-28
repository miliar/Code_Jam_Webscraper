#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>

using namespace std;

#define FOR(_i, _times) for(int _i = 1; _i <= (_times); _i++)
#define FORV(_i, _times) for(int _i = 0; _i < (_times); _i++)
#define FORR(_i, _st, _ed) for(int _i = (_st); _i >= (_ed); _i--)
#define FORE(_i, _st, _ed) for(int _i = (_st); _i <= (_ed); _i++)

int T;
int n, k;
bool check;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &T);
    FOR(ttt, T)
    {
        scanf("%d %d", &n, &k);
        printf("Case #%d: ", ttt);
        check = 1;
        FORV(i, n)
        {
            if(!((1 << i) & k))
            {
                check = 0;
                break;
            }
        }
        if(check) printf("ON\n");
        else printf("OFF\n");
    }
}
