#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <cstdlib>

using namespace std;

int release[101];
struct part {
    int start;
    int end;
};

int main()
{
    int T;
    int P, Q;
    vector<struct part> parts;
    vector<struct part>::iterator end;
    struct part tmp;
    int bribe;
    int tmpp;
    int minbribe;
    cin >> T;
    for(int x = 0; x < T; ++x)
    {
        cin >> P >> Q;
        for(int i = 0; i < Q; ++i)
            cin >> release[i];
            
        
        minbribe = 1000000000;
        do {
            parts.clear();
            tmp.start = 1;
            tmp.end = P;
            parts.push_back(tmp);
            bribe = 0;
            
            for(int i = 0; i < Q; ++i)
            {
                // find release[i]
                end = parts.end();
                for(vector<struct part>::iterator iter = parts.begin(); iter != end; ++iter)
                {
                   
                    if(iter->start > iter->end) continue;
                    if(release[i] >= iter->start && release[i] <= iter->end)
                    {
                        bribe += (iter->end - iter->start);
                        if(release[i] == iter->start)
                            iter->start += 1;
                        if(release[i] == iter->end)
                            iter->end -= 1;
                        
                        else
                        {
                            tmpp = iter->end;
                            iter-> end = release[i] - 1;
                            
                            tmp.start = release[i] + 1;
                            tmp.end = tmpp;
                            parts.push_back(tmp);
                        }
                        break;
                    }
                }
            }
            if(minbribe > bribe) minbribe = bribe;
        }
        while(next_permutation(release, release + Q));
        cout << "Case #" << x + 1 << ": " << minbribe << endl;
    }
                        
                
            
            
    return 0;
}
