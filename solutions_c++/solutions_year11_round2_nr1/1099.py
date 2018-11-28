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

int main()
{
    ifstream in("input1.txt",ios::in);
    ofstream out("outq1s.txt",ios::out);
    
    int test, testi = 0;
    in >> test;
    
    double wp[100], owp [100] , oowp [100];
    int owpn[100];
    
    while ( test -- )
    {
          testi ++;
          
          int n;
          
          in >> n;
          
          FR ( i, n )
          {
               wp [i] = 0;
               owp [i] = 0;
               oowp [i] = 0;
               owpn [i] = 0;
          }
          
          vector <string> all;
          
          FR (i, n )
          {
                 string s;
                 in >> s;
                 all . PB (s);
                 
                 double avp = 0;
                 int noplay = 0;
                 
                 FR ( j, n )
                 {
                      if ( s[j] == '.' )
                      continue;
                      if ( s[j] == '1' )
                      avp ++;
                      noplay ++;
                 }
                 wp [i] = avp / noplay;
                 owpn [i] = noplay;
                 FR ( j, n )
                 {
                      if ( s[j] == '.' )
                      continue;
                      if ( s[j] == '1' )
                      {
                           double newavp = avp - 1;
                           int newnop = noplay - 1;
                           owp [j] += newavp / newnop;
                      }
                      else
                      {
                          double newnop = noplay - 1;
                          owp [j] += avp / newnop;
                      }
                 }
          }
          
          // now calculate owps
          FR ( i, n )
          {
               owp [i] /= owpn[i];
               FR ( j, n )
               if ( all [i] [j] != '.' )
               oowp [j] += owp [i];
          }
          
          FR ( i, n )
          {
               oowp [i] /= owpn[i];
          }
          out << "Case #" << testi << ": " << endl;
          FR ( i, n )
          {
               float res = wp[i] / 4 + owp[i] / 2 + oowp[i] / 4;
               out << res << endl;
          }
    }
    
    in . close ();
    out . close ();
}
