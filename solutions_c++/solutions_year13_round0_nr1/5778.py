#include <vector>
#include <iomanip>
#include <stack>
#include <map>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <string>
#include <set>

using namespace std;

#define DEBUG

#ifdef DEBUG
    #define debug(x...) msg(x);
#else
    #define debug(x...)
#endif

template <class t1>
void msg(t1 a)
{ cerr << a << endl; }
template <class t1, class t2>
void msg(t1 a, t2 b)
{ cerr << a << '\t' << b << endl; }
template <class t1, class t2, class t3>
void msg(t1 a, t2 b, t3 c)
{ cerr << a << '\t' << b << '\t' << c << endl; }
template <class t1, class t2, class t3, class t4>
void msg(t1 a, t2 b, t3 c, t4 d)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << endl; }
template <class t1, class t2, class t3, class t4, class t5>
void msg(t1 a, t2 b, t3 c, t4 d, t5 e)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << '\t' << e << endl; }
template <class t1, class t2, class t3, class t4, class t5, class t6>
void msg(t1 a, t2 b, t3 c, t4 d, t5 e, t6 f)
{ cerr << a << '\t' << b << '\t' << c << '\t' << d << '\t' << e << '\t' << f << endl; }

////////////////////////////////////////////////////////////////////////////


char m[5][5];
int h_o[5];
int h_x[5];
int v_o[5];
int v_x[5];
int d_o[8];
int d_x[8];
int bd_o[8];
int bd_x[8];
int emp_h[5];
int emp_v[5];
int emp_d[8];
int emp_bd[8];
#define X 'X'
#define O 'O'
#define P '.'

void func()
{
    memset(h_o, 0, sizeof(h_o));
    memset(h_x, 0, sizeof(h_x));
    memset(v_o, 0, sizeof(v_o));
    memset(v_x, 0, sizeof(v_x));
    memset(d_o, 0, sizeof(d_o));
    memset(d_x, 0, sizeof(d_x));
    memset(bd_o, 0, sizeof(bd_o));
    memset(bd_x, 0, sizeof(bd_x));
    memset(emp_h, 0, sizeof(emp_h));
    memset(emp_v, 0, sizeof(emp_v));
    memset(emp_d, 0, sizeof(emp_d));
    memset(emp_bd, 0, sizeof(emp_bd));

    int total_empty = 0;
    for (int r = 1; r <= 4; ++r)
    {
        string str;
        cin >> str;
        for (int c = 1; c <= 4; ++c)
        {
            if (str[c-1] == P)
            {
                emp_h[r]++;
                emp_v[c]++;
                emp_d[4-(c-r)]++;
                emp_bd[r+c-1]++;
                total_empty++;
            }
            else if (str[c-1] == X)
            {
                h_x[r]++;
                v_x[c]++;
                d_x[4-(c-r)]++;
                bd_x[r+c-1]++;
            }
            else if (str[c-1] == O)
            {
                h_o[r]++;
                v_o[c]++;
                d_o[4-(c-r)]++;
                bd_o[r+c-1]++;
            }
            else if (str[c-1] == 'T')
            {
                h_x[r]++;
                v_x[c]++;
                d_x[4-(c-r)]++;
                bd_x[r+c-1]++;

                h_o[r]++;
                v_o[c]++;
                d_o[4-(c-r)]++;
                bd_o[r+c-1]++;
            }
        }
    }

    // check for h and v
    bool x_win = false;
    bool o_win = false;
    bool x_will_win = false;
    bool o_will_win = false;

    // chance
    int shang = total_empty / 2;
    int yu    = total_empty % 2;
    int x_chance = shang;
    int o_chance = shang + yu;

    // horizon
    for (int i = 1; i <= 4; ++i)
    {
        if (h_o[i] == 4)
            o_win = true;
        else if (h_o[i] + emp_h[i] == 4 && o_chance >= emp_h[i])
            o_will_win = true;

        if (h_x[i] == 4)
            x_win = true;
        else if (h_x[i] + emp_h[i] == 4 && x_chance >= emp_h[i])
            x_will_win = true;

        if (v_o[i] == 4)
            o_win = true;
        else if (v_o[i] + emp_v[i] == 4 && o_chance >= emp_v[i])
            o_will_win = true;

        if (v_x[i] == 4)
            x_win = true;
        else if (v_x[i] + emp_v[i] == 4 && x_chance >= emp_v[i])
            x_will_win = true;
    }

    // diagonal
    if (bd_o[4] == 4)
        o_win = true;
    else if (bd_o[4] + emp_bd[4] == 4 && o_chance >= emp_bd[4])
        o_will_win = true;

    if (bd_x[4] == 4)
        x_win = true;
    else if (bd_x[4] + emp_bd[4] == 4 && x_chance >= emp_bd[4])
        x_will_win = true;

    if (d_o[4] == 4)
        o_win = true;
    else if (d_o[4] + emp_d[4] == 4 && o_chance >= emp_d[4])
        o_will_win = true;

    if (d_x[4] == 4)
        x_win = true;
    else if (d_x[4] + emp_d[4] == 4 && x_chance >= emp_d[4])
        x_will_win = true;

    if (x_win)
        cout << "X won" << endl;
    else if (o_win)
        cout << "O won" << endl;
#if 0
    else if (o_will_win && !x_will_win)
        cout << "O won" << endl;
    else if (x_will_win && !o_will_win)
        cout << "X won" << endl;
#endif
    else if (!x_will_win && !o_will_win)
        cout << "Draw" << endl;
    else //if (x_will_win && o_will_win)
        cout << "Game has not completed" << endl;
}


////////////////////////////////////////////////////////////////////////////

char in_file[] = "test.in";
char out_file[] = "test.out";

int main()
{
    int case_count, t;

    freopen(in_file, "r", stdin);
    freopen(out_file,"w", stdout);

    cin >> case_count;
    for (t = 1; t <= case_count; t++)
    {
        cerr << "\nDealing Case #" << t << endl;
        cout << "Case #" << t << ": ";
        func();
    }

	return 0;    
}
