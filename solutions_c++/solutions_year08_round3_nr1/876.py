#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    
    for ( int i = 0; i < n; i++ )
    {
        int p, k, l;
        cin >> p >> k >> l;
        
        vector <int> slova;
        
        for ( int j = 0; j < l; j++ )
        {
            int tmp;
            cin >> tmp;
            slova.push_back ( tmp );
        }
        
        sort ( slova.begin(), slova.end() );
        int rez = 0;
        
        int cnt = 0;
        int mnoz = 1;
        for ( int j = slova.size() - 1; j >= 0; j-- )
        {
            cnt ++;
            rez += slova[j] * mnoz;
            
            if ( cnt == k )
            {
                 cnt = 0;
                 mnoz ++;
            }
        }
        
        cout << "Case #" << i + 1 << ": " << rez << endl;
        
    }
    
}              
            
            
            
                
            
        
        
