#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

#define REP(i, n) for((i); (i) < (n); (i)++)
#define gout cout << "Case #" << kase << ": ", cout

int t, n, m;
string temp;
set<string> existing;
vector<string> toput;

unsigned long int ans;

void requires_how_many()
{
    vector<string>::iterator vit = toput.begin();
    REP(vit, toput.end())
    {
        string::iterator it = (*vit).begin();
        int pass = 0;
        bool hasFound = false;
        REP(it, (*vit).end())
        {
            if(*it == '/')
            {
                if(pass == 0) { pass++; continue; }
                //printf("Here!\n");
                set<string>::iterator setit = existing.find((*vit).substr(0, it - (*vit).begin()));
//                cout << (setit != existing.end()) << ' ' << (*vit).substr(0, it - (*vit).begin()) << endl;
                if(setit != existing.end()) continue;
                else { existing.insert((*vit).substr(0, it - (*vit).begin())); ans++; }
            }
        }
        set<string>::iterator setit = existing.find(*vit);
        if(setit == existing.end()) { existing.insert(*vit); ans++; /*cout << *vit << endl;*/}
        /*if(!hasFound)
        {
            //pass = 0;
            string::iterator it = (*vit).begin();
            REP(it, (*vit).end())
            {
                if(*it == '/')
                {
                    //if(pass == 0) { pass++; continue; }
                    //set<string>::iterator setit = existing.find((*vit).substr(0, it - (*vit).begin()));
                    existing.insert((*vit).substr(0, it - (*vit).begin())); ans++;
                    cout << (*vit).substr(0, it - (*vit).begin());
                }
            }
        }*/
    }
}

int main()
{
    int kase = 1;
    scanf("%d", &t);
    REP(kase, t+1)
    {
        existing.clear();
        toput.clear();
        ans = 0;
        scanf("%d %d", &n, &m);
        int i = 0;
        REP(i, n)
        {
            cin >> temp;
            existing.insert(temp);
        }
        i = 0;
        REP(i, m)
        {
            cin >> temp;
            toput.push_back(temp);
        }
        sort(toput.begin(), toput.end());
        requires_how_many();
        gout << ans << endl;
    }
}
