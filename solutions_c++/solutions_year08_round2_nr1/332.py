#include <iostream>
using namespace std;

const int maxN = 100000 + 10;

int N, A, B, C, D, M;
long long x[maxN], y[maxN];
int cnt[3][3];

void rdata()
{
    
    cin >> N >> A >> B >> C >> D >> x[0] >> y[0] >> M;
//    cout << x[0] << ' ' << y[0] << endl;
    memset(cnt, 0, sizeof cnt);
    
//    ++cnt[x[0]][y[0]];
    for (int i = 1; i<N; i++)
    {
//          X = (A * X + B) mod M
//  Y = (C * Y + D) mod M
        x[i] = (A * x[i-1] + B) % M;
        y[i] = (C * y[i-1] + D) % M;
//        cout << x[i] << ' ' << y[i] << endl;

    }

//    N = 3;
//    x[0] = y[0] = x[1] = y[1] = x[2] = y[2] = 0;    
    
    for (int i = 0; i<N; i++)
    ++        cnt[x[i]%3][y[i]%3];
  //  for (int a0 = 0; a0 <3; a0++)
    //    for (int b0 = 0; b0 < 3; b0++)
//            cout << a0 <<' ' << b0 << ' '<< cnt[a0][b0] << endl;
//    cout << endl;
//    return;
    long long ret = 0;
    for(int a1 = 0; a1<3; a1++)
        for (int b1 = 0; b1<3; b1++)
            for (int a2 = 0; a2<3; a2++)
                for (int b2 = 0; b2<3; b2++)
                {
                    for (int a3 = 0; a3 < 3; a3++)
                        for (int b3 = 0; b3 < 3; b3++)
                            if ((a1+a2+a3)%3==0 && (b1+b2+b3)%3==0)
                            {
                                if (a1==a2 && b1==b2)
                                {
                                    ret += (long long)cnt[a1][b1] * (cnt[a1][b1]-1) * (cnt[a1][b1]-2);
                                }
                                else
                                {
                                ret += (long long)cnt[a1][b1] * cnt[a2][b2] * cnt[a3][b3];
                              }
                            }
                }
    cout << ret / 6 << endl;
}

int main()
{
    freopen("A-large.in", "r", stdin);
//    freopen("A.out", "w", stdout);
    int task;
    cin >> task;
    for (int cs = 1; cs<=task; cs++)
    {
        cout << "Case #" << cs << ": ";
        rdata();
    }
//    system("pause");
}
