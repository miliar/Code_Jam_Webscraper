#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <sstream>
#include <utility>
using namespace std;

int s2i(string s)
{
    return s[0]*600+s[1]*60+s[3]*10+s[4];
}

int main()
{
    int n;
    cin >> n;
    for(int i=0;i<n;i++) {
        typedef pair<int, int> time;
        typedef pair<time, bool> timetable;

        int ta, na, nb;
        cin >> ta >> na >> nb;
        multiset<timetable> table;
        for(int j=0;j<na;j++) {
            string d, a;
            cin >> d >> a;
            table.insert(make_pair(make_pair(s2i(d), s2i(a)), true));
        }
        for(int j=0;j<nb;j++) {
            string d, a;
            cin >> d >> a;
            table.insert(make_pair(make_pair(s2i(d), s2i(a)), false));
        }
        
        int ca = 0, cb = 0;
        bool run = false;
        int tm = 0;
        bool astation;
        typedef multiset<timetable>::iterator iterator;
        while(table.size()) {
            if(!run) {
                for(iterator j=table.begin();j!=table.end();j++) {
                    tm = j->first.second+ta;
                    run = true;
                    astation = !j->second;
                    if(j->second)
                        ca++;
                    else
                        cb++;
                    table.erase(j);
                    break;
                }
            }
            if(run) {
                run = false;
                for(iterator j=table.begin();j!=table.end();j++) {
                    if(astation == j->second && tm <= j->first.first) {
                        tm = j->first.second+ta;
                        astation = !j->second;
                        table.erase(j);
                        run = true;
                        break;
                    }
                }
            }
        }
        cout << "Case #" << i+1 << ": " << ca << " " << cb << endl;
    }
    
    return 0;
}
