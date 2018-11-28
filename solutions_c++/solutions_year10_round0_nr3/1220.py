#include <iostream>
#include <deque>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin >> t;
    
    int r, k, n, a;
    deque<int> v;
    vector< pair< deque<int>, int > > history;
    for (int caso = 1; caso <= t; ++caso)
    {
        cin >> r >> k >> n;
        v.clear();
        history.clear();
        for ( int i = 0; i < n; ++i )
        {
            cin >> a;
            v.push_back( a );
        }
        cout << "Case #" << caso << ": ";
        
        long long int total = 0;
        pair< deque<int>, int > p;
        int ciclo = 0, cap, equal = -1;
        while ( ciclo++ < r and equal == -1 )
        {
            p.first = v;
            cap = k;
            deque<int> va;
            while ( cap-v.front() >= 0 and v.size() > 0 )
            {
                cap -= v.front();
                va.push_back( v.front() );
                v.pop_front();
            }
            total += (p.second = (k-cap));
            history.push_back( p );
            
            while (va.size() > 0)
            {
                v.push_back( va.front() );
                va.pop_front();
            }
            
            for ( int i = 0; i < history.size(); ++i )
            {
                if ( v == history[i].first )
                {
                    equal = i;
                    
                    /*cout << "equal: ";
                    for (int i = 0; i < v.size(); ++i) cout << v[i] << " ";
                    cout << endl;
                    */
                    break;
                }
            }
            //cout << "\ntotal: " << total << endl;
        }
        
        if ( equal != -1 )
        {
            r -= (ciclo-1);
            long long int totCiclo = 0, partCiclo = 0;
            int cicloSize = history.size() - equal;
            for ( int i = equal; i < history.size(); ++i )
            {
                totCiclo += history[i].second;
                if ( (i-equal) < (r%cicloSize) )
                    partCiclo += history[i].second;
            }
            
            total += ( totCiclo*(r/cicloSize) );
            total += partCiclo;
            
            //cout << ciclo << " " << r << " " << equal << " " << cicloSize << " " << 
            //        totCiclo << " " << partCiclo << " " << total << endl;
        }
        cout << total << endl;
    }
    
    return 0;
}
