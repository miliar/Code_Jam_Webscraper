#include <iostream>
#include <string>
#include <map>
using namespace std;
enum { NONE = 0, NORTH, WEST, EAST, SOUTH, MAXD };
int DX[] = { 0, 0, -1, 1, 0 };
int DY[] = { 0, -1, 0, 0, 1 };
class A {
    int H, W, Alt[102][102];
    char Lab[102][102], next;
    friend istream & operator>>(istream &, A &);
    friend ostream & operator<<(ostream &, const A &);
    void back(int i, int j, char c) 
    {
        for (;;) {
            int d = Lab[i][j];
            Lab[i][j] = c;
            if (!d) break;
            i -= DY[d];
            j -= DX[d];
        }
    }
    void go(int i, int j)
    {
        if (Lab[i][j]) return;
        for (;;) {
            int min_a = 100000, min_d = NONE;
            for (int d = NONE; d < MAXD; ++d) {
                int a = Alt[i + DY[d]][j + DX[d]];
                if (a < min_a) {
                    min_a = a;
                    min_d = d;
                }
            }
            i += DY[min_d];
            j += DX[min_d];
            if (min_d) {
                char c = Lab[i][j];
                if (!c)
                    Lab[i][j] = min_d;
                else 
                    return back(i - DY[min_d], j - DX[min_d], c);
            } else
                return back(i, j, next++);
        }
    }
public:
    A() : next('a') 
    { 
        for (int i = 102; i--; )
            for (int j = 102; j--; )
                Alt[i][j] = 1000000;
    }
    A & operator()()
    {
        for (int i = 1; i <= H; ++i) {
            for (int j = 1; j <= W; ++j) {
                go(i, j);
            }
        }
        return *this;
    }
};
istream & operator>>(istream & s, A & a)
{
    s >> a.H >> a.W;
    for (int i = 1; i <= a.H; ++i) {
        for (int j = 1; j <= a.W; ++j) {
            s >> a.Alt[i][j];
            a.Lab[i][j] = NONE;
        }
    }
    return s;
}
ostream & operator<<(ostream & s, const A & a)
{
    for (int i = 1; i <= a.H; ++i) {
        for (int j = 1; j <= a.W; ++j) {
            char c = a.Lab[i][j];
            if (c < 'a') c += '0';
            s << c << " ";
        }
        s << "\n";
    }
    return s;
}
int main()
{
    unsigned N;
    cin >> N;
    for (unsigned i = 1; i <= N; ++i) {
        A a;
        cin >> a;
        cout << "Case #" << i << ":\n" << a();
    }
}
