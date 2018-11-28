#include <iostream>
#include <string>
#include <list>

using namespace std;

class googol : public string
{
public:
    template<class c, class t, class a> bool operator<(const basic_string<c, t, a>& s)
        { return size() == s.size() ? *(string*)this < s : size() < s.size(); };
    template<class c, class t, class a> bool operator>(const basic_string<c, t, a>& s)
        { return size() == s.size() ? *(string*)this > s : size() > s.size(); };
    template<class c, class t, class a> basic_string<c, t, a> operator-=(const basic_string<c, t, a>& s);
    using string::operator=;
};


template<class c, class t, class a> basic_string<c, t, a> googol::operator-=(const basic_string<c, t, a>& s)
{
    const_reverse_iterator si;
    reverse_iterator i;
    int d, b;

    for (i = rbegin(), si = s.rbegin(), b = 0; ; i++)
    {
        if (i == rend())
        {
            d = find_first_not_of('0');
            if (d > 0) erase(0, d);
            else if (d == npos) *this = "0";
            break;
        }
        if (si != s.rend()) d = *si++;
        else 
        {
            if (b == 0) break;
            d = '0';
        }
        d = *i - d - b;
        if (d < 0)
        {
            d += 10;
            b = 1;
        }
        else b = 0;
        
        *i = d + '0';
    }
    return *this;
}


int main(int i, char **argv)
{
    int C, N, j;
    googol s;
    list <googol> t;
    list <googol>::iterator ti;

    cin >> C;
    for (i = 1; i <= C; i++, t.clear())
    {
        cin >> N;
        for (j = N; j > 0; j--) 
        {
            cin >> s;
            t.push_back(s);
        }
        
        t.sort();
        t.unique();
        s = t.front();
        t.remove(s);
        for (ti = t.begin(); ti != t.end(); ti++) *ti -= s;
        while (t.size() > 1)
        {
            for (ti = t.begin(), ti++; ti != t.end(); ti++) *ti -= t.front();
            t.sort();
            t.unique();
        }
        while (s > t.front()) s -= t.front();
        cout << "Case #" << i << ": " << (t.front() -= s) << endl;
    }

    return 0;
}
