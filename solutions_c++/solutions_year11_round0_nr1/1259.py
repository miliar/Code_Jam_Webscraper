#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
ifstream fin("a.in");
ofstream fout("a.out");
#define cin fin
#define cout fout
struct Dtype
{
    int loc;
    char person;
};

Dtype d[200];
int lo, lb, go, gb;//location, goal
int ans;
int T, n;
char ch;
 
int nexto(int x)
{
    if (x==n) return 150;
    for ( ++x; (d[x].person!='O')&&(x!=n); ++x );
    if ((x==n) && (d[x].person!='O')) x = 150;
    return x;
}

int nextb(int x)
{
    if (x==n) return 150;
    for ( ++x; (d[x].person!='B')&&(x!=n); ++x );
    if ((x==n) && (d[x].person!='B')) x = 150;
    return x;
}

int main()
{
   
    cin >> T;
    int tt = T;
    while (T--)
    {
        cin >> n;
        for (int i = 1; i <= n; ++i )
            cin >> d[i].person >> d[i].loc;  
        ans = go = gb = 0;
        lo = lb = 1;
        go = nexto(go);
        gb = nextb(gb);
        
        while ((go!=150) || (gb!=150))
        {
            //cout << ans << " " << lo << " " << go << " " << lb << " " << gb << endl; 
            ////cout << "<"<<d[3].person<<">"<<endl;
            if (go == 150 )
            {
                //cout << "gb from" << lb << " to " << d[gb].loc << " which costs " << abs(d[gb].loc-lb)+1 << endl;
                
                ans += abs(d[gb].loc-lb)+1;
                lb = d[gb].loc;
                gb = nextb(gb);
                
                continue;
            }
            if (gb == 150 )
            {
                
                //cout << "go from" << lo << " to " << d[go].loc << " which costs " << abs(d[go].loc-lo)+1 << endl;
                
                ans += abs(d[go].loc-lo)+1;
                lo = d[go].loc;
                go = nexto(go);
                continue;
            }
            if (go < gb)
            {
                
                //cout << "go from" << lo << " to " << d[go].loc << " which costs " << abs(d[go].loc-lo)+1 << endl;
                
                ans += abs(d[go].loc-lo)+1;
                if (abs(d[gb].loc-lb)<=abs(d[go].loc-lo)+1)
                {
                    lb = d[gb].loc;
                       
                }
                else 
                {
                    if (d[gb].loc>lb) lb += abs(d[go].loc-lo)+1;
                    else lb -= abs(d[go].loc-lo)+1;
                }
                lo = d[go].loc;
                //cout << "\t" << "Meamwhile " << "gb goes to " << lb << "\t";
                go = nexto(go);
            }
            else 
            {
                
                //cout << "gb from" << lb << " to " << d[gb].loc << " which costs " << abs(d[gb].loc-lb)+1 << endl;
                
                ans += abs(d[gb].loc-lb)+1;
                if (abs(d[go].loc-lo)<=abs(d[gb].loc-lb)+1)
                    lo = d[go].loc;
                else 
                {
                    if (d[go].loc>lo) lo += abs(d[gb].loc-lb)+1;
                    else lo -= abs(d[gb].loc-lb)+1;
                }
                lb = d[gb].loc;
                //cout << "\t" << "Meamwhile " << "go goes to " << lo << "\t";
                gb = nextb(gb);
                
            } 
            
        }
        cout << "Case #" << tt-T << ": " << ans << endl;
    }
    system("pause");
} 
