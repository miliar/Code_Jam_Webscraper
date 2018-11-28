# include <cstdio>
# include <cstdlib>
# include <vector>
# include <set>
# include <map>
# include <deque>
# include <algorithm>
# include <cctype>
# include <iostream>
# include <cstring>
# include <fstream>

# define FR(i, n)           for( int i = 0; i < n; i++)
# define FRin(i, m, n)     for( int i = m; i < n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define PF    printf
# define SF    scanf
# define PB    push_back

using namespace std;

long long int gcd( long long a, long long b)
{
     if ( a < b) a ^= b ^= a ^= b;
     if ( b == 0 ) return a;
     else
     return gcd ( b, a%b );
}

int main()
{
    ifstream in("input1.txt",ios::in);
    ofstream out("outq1s.txt",ios::out);
    
    
    
    int test;
    cin >> test;
    cout << test << endl;
    int testi = 1;
    while ( test -- )
    {
          long long n, pd, pg;
          cin >> n >> pd >> pg;
          
          out << "Case #" << testi << ": ";
          
          if ( pd != 100 && pg == 100 )
          {
               out << "Broken" << endl;
                 testi ++;
               continue;
           }
          if ( pd != 0 && pg == 0 )
          {
               out << "Broken" << endl;
                 testi ++;
               continue;
           }
           if ( pd == 100 && pg == 100 )
           {
                out << "Possible" << endl;
                 testi ++;
                continue;
            }
            if ( pd == 0 && pg == 0)
            {
                 out << "Possible" << endl;
                 testi ++;
                 continue;
             }
            if ( pd == 0 || pd == 100)
            {
                 out << "Possible" << endl;
                 testi ++;
                 continue;
             } 
             
             
          long long first = gcd ( 100, pd );
          first = 100 / first;
          
          if ( first > n )
          {
               out << "Broken" << endl;
               testi ++;
               continue;
           }
           else
           {
               out << "Possible" << endl;
                 testi ++;
                 continue;
           }
          
    }
    in.close();
    out.close();
}
