#include <iostream>
#include <vector>
using namespace std;
vector<int> used[2000002];

int main()
{
    int t;
    cin >> t;
    int u;
    for(u = 1; u <= t; u++)
    {
        int n;
        cin >> n;
        vector<int> v;
        int i;
        for(i = 0; i < 2000002; i++)
            used[i].clear();
        used[0].push_back(0);
        
        
        
        int r = 0;
        for(i = 0; i < n; i++)
        {
            int k;
            cin >> k;
            v.push_back(k);
            r +=k;
        }
        int j;
        bool found = 0;
        cout << "Case #" << u <<":\n";
        for(j = 0; j < n && !found; j++)
        {
            for(i = r; i >= 0 && !found; i--)
                if(i >= v[j])
                    if(used[i-v[j]].size() != 0)
                    {
                        used[i].push_back(v[j]);
                        //cout << "add " << v[j] << " to" << ' ' << i << endl;
                        if(used[i].size() == 2)
                        {
                            if(i - used[i][0] == 0)
                                cout << used[i][0] << "\n";
                            else
                                cout << used[i][0] << ' ';
                            
                            int w = i - used[i][0];

                            while(w > 0)
                            {
                                if(w - used[w][0] == 0)
                                    cout << used[w][0] << "\n";
                                else
                                    cout << used[w][0] << ' ';
                                
                                w -= used[w][0];
                            }
                            
                            if(i - used[i][1] == 0)
                                cout << used[i][1] << "\n";
                            else
                                cout << used[i][1] << ' ';

                            w = i - used[i][1];

                            while(w > 0)
                            {
                                if(w - used[w][0] == 0)
                                    cout << used[w][0] << "\n";
                                else
                                    cout << used[w][0] << ' ';
                                w -= used[w][0];
                            }

                            found = 1;
                        }
                    }
            

            
        }
        
    }
    return 0;
}
