#include <iostream>
#include <vector>
#include <string>
#include <deque>

struct Num;

bool operator<(const Num &n1, const Num &n2);
std::ostream &operator<<(std::ostream &stream, const Num &num);

struct Num
{
    typedef std::deque<int> Digits;

    void swap(Num &n)
    {
        d.swap(n.d);
    }

    void shl(int n)
    {
        if (d.size() == 1 && d[0] == 0)
            return;

        for (int i = 0 ; i < n ; ++i)
            d.push_front(0);
    }

    void normalize()
    {
        while (d.size() > 1 && d.back() == 0)
            d.pop_back();
    }

    void set(const std::string &s)
    {
        d.resize(s.size());
        for (size_t i = 0 ; i < s.size() ; ++i)
            d[s.size() - i - 1] = s[i] - '0';
        normalize();
    }

    Num &operator-=(const Num &n)
    {
        int c = 0;
        size_t i = 0;
        for ( ; i < n.size() ; ++i)
        {
            d[i] -= n[i] + c;
            c = 0;
            if (d[i] < 0)
            {
                d[i] += 10;
                c = 1;
            }
        }
        while (c)
        {
            d[i] -= c;
            c = 0;
            if (d[i] < 0)
            {
                d[i] += 10;
                c = 1;
            }
            ++i;
        }
        normalize();
        return *this;
    }

    Num &operator%=(const Num &n)
    {
        //std::cout << *this << " %= " << n << " = ";
        while (!(*this < n))
        {
            Num t = n;
            int z = (int)(d.size() - t.size()) - 1;
            t.shl(z);
            while (!(*this < t))
                *this -= t;
        }
        normalize();

        //std::cout << *this << "\n";

        return *this;
    }

    bool empty() const
    {
        if (d.size() == 1 && d[0] == 0)
            return true;

        return false;
    }

    size_t size() const { return d.size(); }
    int &operator[](size_t i) { return d[i]; }
    int operator[](size_t i) const { return d[i]; }

    Digits d;
};

std::istream &operator>>(std::istream &stream, Num &num)
{
    std::string s;
    stream >> s;
    num.set(s);
    return stream;
}

std::ostream &operator<<(std::ostream &stream, const Num &num)
{
    for (int i = (int)num.size() - 1 ; i >= 0 ; --i)
        stream << num[i];
    return stream;
}

bool operator<(const Num &n1, const Num &n2)
{
    if (n1.size() != n2.size())
        return n1.size() < n2.size();

    for (int i = (int)n1.size() - 1 ; i >= 0 ; --i)
        if (n1[i] != n2[i])
            return n1[i] < n2[i];

    return false;
}


int n;
Num a[1000];

/*
  T = gcd(	

 */

Num gcd(const Num &n1, const Num &n2)
{
    Num r1 = n1;
    Num r2 = n2;
    while (!r1.empty() && !r2.empty())
    {
        r1 %= r2;
        r1.swap(r2);
    }
    if (r1.empty())
        return r2;

    return r1;
}

int main()
{
    //freopen("B-small-attempt0.in", "rt", stdin);

    int T;
    std::cin >> T;
    for (int t = 1 ; t <= T ; ++t)
    {
        std::cout << "Case #" << t << ": ";
        std::cin >> n;
        for (int i = 0 ; i < n ; ++i)
            std::cin >> a[i];

        Num min = a[0];
        for (int i = 1 ; i < n ; ++i)
            if (a[i] < min)
                min = a[i];

        for (int i = 0 ; i < n ; ++i)
            a[i] -= min;

        Num T = gcd(a[0], a[1]);
        for (int i = 2 ; i < n ; ++i)
            T = gcd(T, a[i]);

        Num y = min;
        y %= T;
        Num tmp = T;
        tmp -= y;
        tmp %= T;
        y = tmp;

        std::cout << y << "\n";
    }
    return 0;
}
