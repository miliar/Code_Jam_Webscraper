#include <iostream>
using namespace std;

const int N = 1000010;
int pos[N] = {0};

void init()
{
    pos[1] = 0;
    pos[2] = 1;
    pos[3] = 1;
    pos[4] = 2;
    pos[5] = 3;
    pos[6] = 3;

    for(int i = 7; i < N; i++)
    {
        int x = pos[i-1];
        //if(i % 2) x++;

        while(1)
        {
            int y = i - x;
            if(pos[x] < y) x++;
            else break;
        }
        x--;
        //printf("%d %d\n", i, x);
        pos[i] = x;
    }
}

bool judge(int a, int b)
{
    int Min = min(a, b);
    int Max = max(a, b);
    if(Min <= pos[Max]) return 1;
    else return 0;
}

void solve(int tcase)
{
    int a1, a2, b1, b2;
    cin>>a1>>a2>>b1>>b2;

    int res = 0;
    for(int i = a1; i <= a2; i++)
    {
        for(int j = b1; j <= b2; j++)
        {
            if(judge(i, j)) res++;
        }
    }
    printf("Case #%d: %d\n", tcase, res);
}

int main()
{
    //
    init();

    /*cout<<judge(10, 5)<<endl;
    cout<<judge(10, 6)<<endl;
    cout<<judge(10, 7)<<endl;*/

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin>>T;

    for(int i = 1; i <= T; i++)
    {
        solve(i);
    }
}
