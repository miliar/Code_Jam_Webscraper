#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

struct ttime
{
    int t;
    bool start;
    char stantion;
};

bool operator<(ttime a, ttime b)
{
    if (a.t == b.t)
        return ((!a.start) && (b.start));
    else
        return (a.t < b.t);
}

void solve(int case_n)
{
    int remT, NA, NB;
    vector<ttime> T;

    in >> remT >> NA >> NB;
    for (int i = 0; i < NA; i++)
    {
        int h, m;
        char c;
        ttime t1, t2;

        in >> h >> c >> m;
        t1.start = true;
        t1.t = h*60+m;
        t1.stantion = 'A';

        in >> h >> c >> m;
        t2.start = false;
        t2.t = h*60+m+remT;
        t2.stantion = 'B';

        T.push_back(t1);
        T.push_back(t2);
    }
    for (int i = 0; i < NB; i++)
    {
        int h, m;
        char c;
        ttime t1, t2;

        in >> h >> c >> m;
        t1.start = true;
        t1.t = h*60+m;
        t1.stantion = 'B';

        in >> h >> c >> m;
        t2.start = false;
        t2.t = h*60+m+remT;
        t2.stantion = 'A';

        T.push_back(t1);
        T.push_back(t2);
    }

    sort(T.begin(), T.end());

    /*for (int i = 0; i < T.size(); i++)
    {
        cerr << T[i].t << ' ' << T[i].start << ' ' << T[i].stantion << endl;
    }
    cerr << "======\n";*/

    int curA = 0, curB = 0;
    int minA = 0, minB = 0;
    for (int i = 0; i < T.size(); i++)
    {
        if (T[i].start)
        {
            if (T[i].stantion == 'A')
            {
                if (curA == 0)
                    minA++;
                else
                    curA--;
            }
            else
            {
                if (curB == 0)
                    minB++;
                else
                    curB--;
            }
        }
        else
        {
            if (T[i].stantion == 'A')
            {
                curA++;
            }
            else
            {
                curB++;
            }
        }
    }

    out << "Case #" << case_n << ": " << minA << ' ' << minB << endl;
}

int main()
{
    int n;
    in >> n;
    for (int i = 0; i < n; i++)
        solve(i+1);
}
