#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

struct Time
{
    int h, m;
    Time(int hh = 0, int mm = 0) : h(hh), m(mm) {}
};

const istream& operator >> (const istream& in, Time& t)
{
    scanf("%d:%d", &t.h, &t.m);
    return in;
}

const ostream& operator << (const ostream& out, const Time& t)
{
    printf("%d:%d ", t.h, t.m);
    return out;
}

Time operator + (const Time& a, int add)
{
    return Time(a.h + (a.m + add) / 60, (a.m + add) % 60);
}

bool operator < (const Time& a, const Time& b)
{
    if (a.h != b.h) return a.h < b.h;
    return a.m < b.m;
}

void Read(vector <Time>& start, vector <Time>& end, int n, int t)
{
    for (int i=0;i<n;i++)
    {
        Time t1, t2;
        cin >> t1 >> t2;
        start.push_back(t1);
        if (t2 < t1) t2.h += 24;
        end.push_back(t2 + t);
    }
    sort(start.begin(), start.end());
    sort(end.begin(), end.end());
}

int calc(const vector <Time>& start, const vector <Time>& end)
{
    int cnt = 0;
    vector <Time>::const_iterator is = start.begin();
    vector <Time>::const_iterator ie = end.begin();
    for (; is != start.end(); is++)
    {
        if (ie == end.end() || *is < *ie) cnt++;
        else ie++;
    }
    return cnt;
}

void prt(const vector <Time>& st)
{
    for (vector <Time>::const_iterator iter = st.begin(); iter != st.end(); iter++)
        cout << *iter;
    printf("\n");
}

int main()
{
    int tt, cnt = 0;
    cin >> tt;
    for (int i=0;i<tt;i++)
    {
        int t, na, nb;
        cin >> t >> na >> nb;
        //Start A, End A, Start B, End B
        vector <Time> sa, ea, sb, eb;
        Read(sa, eb, na, t);
        Read(sb, ea, nb, t);
//prt(sa);
//prt(eb);
//prt(sb);
//prt(ea);
        printf("Case #%d: %d %d\n", ++cnt, calc(sa, ea), calc(sb, eb));
    }
    return 0;
}
