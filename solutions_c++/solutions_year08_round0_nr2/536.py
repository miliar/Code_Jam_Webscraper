#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
using namespace stdext;

int readtime()
{
    char s[100];
    scanf("%s",s);
    int h1=s[0]-'0', h2=s[1]-'0',m1=s[3]-'0',m2=s[4]-'0';
    return 60*(h1*10+h2) + m1*10+m2;
}

int main()
{
    int N;
    scanf("%i", &N);
    for (int ti = 0; ti < N; ++ti)
    {
        int A = 0, B = 0;
        int T;
        cin >> T;
        int na, nb;
        cin >> na >> nb;

        multiset<int> Adep, Bdep, Aarr, Barr;
        for (int i = 0; i < na; ++ i)
        {
            Adep.insert(readtime());
            Barr.insert(readtime());
        }
        for (int i = 0; i < nb; ++ i)
        {
            Bdep.insert(readtime());
            Aarr.insert(readtime());
        }
        
        multiset<int>::iterator it;

        for (it=Aarr.begin(); it!=Aarr.end(); ++it)
        {
            int t = *it + T;
            if (Adep.lower_bound(t) != Adep.end())
                Adep.erase(Adep.lower_bound(t));
        }
        for (it=Barr.begin(); it!=Barr.end(); ++it)
        {
            int t = *it + T;
            if (Bdep.lower_bound(t) != Bdep.end())
                Bdep.erase(Bdep.lower_bound(t));
        }
        
        A = Adep.size();
        B = Bdep.size();

        cout << "Case #" << ti+1 << ": " << A << " " << B << endl;
    }
    return 0;
}
