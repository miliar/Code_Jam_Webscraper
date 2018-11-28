#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <cstring>
#include <vector>
#include <deque>
#include <queue>
#include <cmath>
#include <new>
#include <map>
#include <set>
using namespace std;

struct Wrap
{
    long long number, ID;
    Wrap(long long number, int ID) : number(number), ID(ID) {}
    Wrap() {}
    friend inline bool operator==(Wrap const& lhs, Wrap const& rhs);
};

inline bool operator==(Wrap const& lhs, Wrap const& rhs)
{
    return lhs.number == rhs.number && lhs.ID == rhs.ID;
}

int main()
{
    ifstream fin("3.in");
    ofstream fout("3.out");
    long long tests;
    fin >> tests;
    for (long long brojac = 1; brojac <= tests; ++brojac)
    {
        long long R, capacity, N;
        fin >> R >> capacity >> N;
        long long niz[1000];
        memset(niz, 0, sizeof niz);

        vector<bool> onboard(N, false);
        for (long long i = 0; i < N; ++i)
            fin >> niz[i];
        long long nextToGo = 0;
        vector<vector<Wrap> > Groups;
        vector<Wrap> Grupa;
        long long totalOn = 0;
        // ako se grupa ponavlja == kraj
        for (;;)
        {
            if (onboard[nextToGo])
            {
                if (std::find(Groups.begin(), Groups.end(), Grupa)
                        != Groups.end())
                {
                    break;
                }
                else
                    Groups.push_back(Grupa);
                Grupa.resize(0);
                totalOn = 0;
                std::fill(onboard.begin(), onboard.end(), false);
            }
            else if (niz[nextToGo] + totalOn < capacity)
            {
                totalOn += niz[nextToGo];
                Grupa.push_back(Wrap(niz[nextToGo], nextToGo));
                onboard[nextToGo] = true;
                ++nextToGo;
                if (nextToGo == N)
                    nextToGo = 0;
            }
            else if (niz[nextToGo] + totalOn == capacity)
            {
                totalOn += niz[nextToGo];
                Grupa.push_back(Wrap(niz[nextToGo], nextToGo));
                if (std::find(Groups.begin(), Groups.end(), Grupa)
                        != Groups.end())
                {
                    break;
                }
                else
                    Groups.push_back(Grupa);
                Grupa.resize(0);
                totalOn = 0;
                std::fill(onboard.begin(), onboard.end(), false);
                ++nextToGo;
                if (nextToGo == N)
                    nextToGo = 0;
            }
            else if (niz[nextToGo] + totalOn > capacity)
            {
                if (std::find(Groups.begin(), Groups.end(), Grupa)
                        != Groups.end())
                {
                    break;
                }
                else
                    Groups.push_back(Grupa);
                Grupa.resize(0);
                totalOn = 0;
                std::fill(onboard.begin(), onboard.end(), false);
            }
        }
        vector<long long> Money;
        long long suma = 0;
        long long one = 0;
        long long index;
        bool locirao = false;
        for (long long i = 0; i < Groups.size(); ++i)
        {
            suma = 0;
            for (long long j = 0; j < Groups[i].size(); ++j)
                suma += Groups[i][j].number;
            if (Groups[i] == Grupa) { locirao = true; index = Money.size(); }
            if (locirao) one += suma;
            Money.push_back(suma);
        }
        long long ans = 0;
        for (long long i = 0; i < index; ++i)
            ans += Money[i];
        ans += one * ((R - index) / (Money.size() - index));
        long long limit = (R  - index) % (Money.size() - index);
        long long kk = index;
        for (long long i = 0; i < limit; ++i)
        {
            ans += Money[kk];
            ++kk; if (kk == Money.size()) kk = index;
        }
        fout << "Case #" << brojac << ": " << ans << endl;

    }
    return 0;
}
