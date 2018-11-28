#include <iostream>
#include <list>
using namespace std;




int main()
{
    int C;
    cin >> C;
    
    while(C--)
    {
        int N, M;
        cin >> N >> M;
        
        list< pair<int, int> > adj[128];
                  
        for(int i = 0; i < M; i++)
        {
            int T;
            cin >> T;
            
            while(T--)
            {
                int X, Y;
                cin >> X >> Y;
                
                adj[i].push_back(make_pair(X - 1, Y));                                
            }        
                
        }
        
        
        int ans;
        int minans = INT_MAX;
        for(int z = (1 << N) - 1; z >= 0; z--)
        {
            int c = 0;
            for(int i = 0; i < N; i++)
                if(z & (1 << i))
                    c++;
                
            if(c < minans)
            {
                bool finish = true;
                
                for(int i = 0; i < M; i++)
                {
                    bool f = true;
                    for(list<pair<int, int> >::iterator it = adj[i].begin(); it != adj[i].end(); it++)
                        if(((z & (1 << it->first)) == 0) == (it->second == 0))
                        {
                            f = false;
                            break;      
                        }
                    
                    if(f)
                    {
                        finish = false;
                        break;     
                    }
                }
                 
                if(finish)
                {
                    minans = c;
                    ans = z;          
                }
            }
                              
        }
              
              
        static int times = 0;
        cout << "Case #" << ++times << ":";
        if(minans == INT_MAX)
            cout << " IMPOSSIBLE\n";
        else
        {
            for(int i = 0; i < N; i++)
                if(ans & (1 << i))
                    cout << " 1";
                else
                    cout << " 0";
            
            cout << '\n';
        }
              
    }    
    
    return 0;   
}
