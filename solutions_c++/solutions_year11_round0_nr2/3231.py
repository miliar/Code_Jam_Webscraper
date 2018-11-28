#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

int main()
{
    int T, C, D, N;
    char c1, c2, c3;
    
    cin >> T;
    //cout << "T = " << T << endl;
    
    for(int t = 0; t < T; t++)
    {
        map<char, map<char, char> > combined;
        map<char, set<char> > opposed;
        map<char, int> count;
    
        cin >> C;
        //cout << "C = " << C << endl;
        
        for(int c = 0; c < C; c++)
        {
            cin >> c1;
            cin >> c2;
            cin >> c3;
            
            combined[c1][c2] = c3;
            combined[c2][c1] = c3;
            
            //cout << c1 << c2 << c3 << " ";
        }
        
        //cout << endl;
        
        cin >> D;
        //cout << "D = " << D << endl;
        
        for(int d = 0; d < D; d++)
        {
            cin >> c1;
            cin >> c2;
            
            opposed[c1].insert(c2);
            opposed[c2].insert(c1);
            
            //cout << c1 << c2 << " ";
        }
        
        //cout << endl;
        
        cin >> N;
        //cout << "N = " << N << endl;
        
        cin >> c1;
        
        vector<char> ordered;
        
        count[c1] = count[c1] + 1;
        ordered.push_back(c1);
        
        for(int n = 1; n < N; n++)
        {
            cin >> c1;
            c2 = ordered.back();
            
            if(combined[c1].find(c2) != combined[c1].end())
            {
                count[c2] = count[c2] - 1;
                ordered.pop_back();
                
                c3 = combined[c1][c2];
                
                count[c3] = count[c3] + 1;
                ordered.push_back(c3);
            }
            else
            {
                set<char>::iterator it;
                bool clear = false;
                
                for(it = opposed[c1].begin(); it != opposed[c1].end() && !clear; it++)
                {
                    if(count[*it] > 0)
                        clear = true;
                }
                
                if(clear)
                {
                    ordered.clear();
                    count.clear();
                }
                else
                {
                    count[c1] = count[c1] + 1;
                    ordered.push_back(c1);
                }
            }
        }
        
        cout << "Case #" << (t + 1) << ": [";
        
        for(int i = 0; i < ordered.size(); i++)
        {
            if(i > 0) cout << ", ";
            cout << ordered[i];
        }
        
        cout << "]" << endl;
        
        //cout << endl;
    }

    return 0;
}