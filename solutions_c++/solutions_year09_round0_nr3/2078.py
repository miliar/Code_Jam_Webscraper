#include<iostream>
#include<string>
using namespace std ;
typedef long long LL ;
int t[510][20] ;
char napis[] = "welcome to code jam" ;
main()
{
      ios_base::sync_with_stdio(0) ;
      string s ;
      int C, n, i, j ;
      cin >> C ; cin.ignore() ;
      for(int test=1 ; test<=C ; test++)
      {
            getline(cin,s);
            n = s.size() ;
            for(i=0 ; i<19 ; i++) t[0][i] = 0 ;
            for(i=1 ; i<=n ; i++)
            {
                  for(j=0 ; j<19 ; j++) t[i][j] = t[i-1][j] ;
                  char x = s[i-1] ;
                  for(j=0 ; j<19 ; j++)
                        if(napis[j]==x)
                        {
                              if(j==0) t[i][j] ++ ;
                              else t[i][j] += t[i-1][j-1] ;
                              t[i][j] %= 1000 ;
                          //    cout << "t[" << i << "][" << j << "=" << t[i][j] << endl ;
                        }
            }
            cout << "Case #" << test << ": " ;
            cout.fill('0') ;
            cout.width(4) ;
            cout << t[n][18] << endl ;
      }
}
