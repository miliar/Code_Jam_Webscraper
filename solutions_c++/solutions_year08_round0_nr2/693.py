#include <iostream>
#include <string>
#include <stdio.h>
#include <deque>
#include <utility>
#include <algorithm>

using namespace std;

struct Sch : public pair<int,int> {
        bool fromA;
};
 
typedef deque<Sch>::iterator iter;

iter next(const Sch& s, iter start, iter finish)
{
        int endtime = s.second;
        while (start != finish) {
                if (start->first >= endtime
                    && start->fromA != s.fromA)
                        return start;
                ++start;
        }
        return finish;
}


int main()
{
        int n;
        scanf("%d", &n);
        
        for (int c=0; c<n; ++c) {
                cout << "Case #" << c+1 << ": ";
                
                int t, a, b;
                
                scanf("%d %d %d", &t, &a, &b);
                
                deque< Sch > tt(a+b);
                
                int hi,  mi, hf, mf;
                for (int i=0; i<a; ++i) {
                        scanf("%d:%d %d:%d", &hi, &mi,
                              &hf, &mf);
                        tt[i].first = hi*60 + mi;
                        tt[i].second = hf*60 + mf + t;
                        tt[i].fromA = true;
                }
                for (int i=0; i<b; ++i) {
                        scanf("%d:%d %d:%d", &hi, &mi,
                              &hf, &mf);
                        tt[i+a].first = hi*60 + mi;
                        tt[i+a].second = hf*60 + mf + t;
                        tt[i+a].fromA = false;
                }

                sort(tt.begin(), tt.end());                

                int na = 0;
                int nb = 0;
                
                while (!tt.empty()) {
                        Sch f = tt.front();
                        tt.pop_front();

                        if (f.fromA)
                                na++;
                        else
                                nb++;
                        
                        iter start = tt.begin();
                        while (start != tt.end()) {
                                // elimina todos dessa trip
                                start = next(f, start, tt.end());
                                if (start == tt.end())
                                        break;
                                f = *start;
                                start = tt.erase(start);
                        }
                }

                cout << na << " " << nb << endl;
        }
        
}
