#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
  int N;
  
  ifstream in("C-small-attempt0.in");
  ofstream out("output.txt");
  
  in >> N;
  
  string n_string;
  getline(in, n_string);
  
  for( int i = 1; i <= N; i++ )
  {
    string phrase;
    getline(in, phrase);
    
    int answer = 0;
    
    if ( phrase.size() >= 19 )
    {
    for( int j = 0; j <= phrase.size() - 19; j++ )
    {
      if ( phrase.at(j) == 'w' )
      {
        for( int k = j + 1; k <= phrase.size() - 18; k++ )
        {
          if ( phrase.at(k) == 'e' )
          {
            for( int l = k + 1; l <= phrase.size() - 17; l++ )
            {
              if ( phrase.at(l) == 'l' )
              {
                for( int m = l + 1; m <= phrase.size() - 16; m++ )
                {
                  if ( phrase.at(m) == 'c' )
                  {
                    for( int n = m + 1; n <= phrase.size() - 15; n++ )
                    {
                      if ( phrase.at(n) == 'o' )
                      {
                        for( int o = n + 1; o <= phrase.size() - 14; o++ )
                        {
                          if ( phrase.at(o) == 'm' )
                          {
                            for( int p = o + 1; p <= phrase.size() - 13; p++ )
                            {
                              if ( phrase.at(p) == 'e' )
                              {
                                for( int q = p + 1; q <= phrase.size() - 12; q++ )
                                {
                                  if ( phrase.at(q) == ' ' )
                                  {
                                    for( int r = q + 1; r <= phrase.size() - 11; r++ )
                                    {
                                      if ( phrase.at(r) == 't' )
                                      {
                                        for( int s = r + 1; s <= phrase.size() - 10; s++ )
                                        {
                                          if ( phrase.at(s) == 'o' )
                                          {
                                            for( int t = s + 1; t <= phrase.size() - 9; t++ )
                                            {
                                              if ( phrase.at(t) == ' ' )
                                              {
                                                for( int u = t + 1; u <= phrase.size() - 8; u++ )
                                                {
                                                  if ( phrase.at(u) == 'c' )
                                                  {
                                                    for( int v = u + 1; v <= phrase.size() - 7; v++ )
                                                    {
                                                      if ( phrase.at(v) == 'o' )
                                                      {
                                                        for( int w = v + 1; w <= phrase.size() - 6; w++ )
                                                        {
                                                          if ( phrase.at(w) == 'd' )
                                                          {
                                                            for( int x = w + 1; x <= phrase.size() - 5; x++ )
                                                            {
                                                              if ( phrase.at(x) == 'e' )
                                                              {
                                                                for( int y = x + 1; y <= phrase.size() - 4; y++ )
                                                                {
                                                                  if ( phrase.at(y) == ' ' )
                                                                  {
                                                                    for( int z = y + 1; z <= phrase.size() - 3; z++ )
                                                                    {
                                                                      if ( phrase.at(z) == 'j' )
                                                                      {
                                                                        for( int a = z + 1; a <= phrase.size() - 2; a++ )
                                                                        {
                                                                          if ( phrase.at(a) == 'a' )
                                                                          {
                                                                            for( int b = a + 1; b <= phrase.size() - 1; b++ )
                                                                            {
                                                                              if ( phrase.at(b) == 'm' )
                                                                              {
                                                                                answer++;
                                                                              }
                                                                            }
                                                                          }
                                                                        }
                                                                      }
                                                                    }
                                                                  }
                                                                }
                                                              }
                                                            }
                                                          }
                                                        }
                                                      }
                                                    }
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                  }
                                }
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    }
    
    out << "Case #" << i << ": ";
    
    if ( answer > 1000 )
    {
      answer = answer % 10000;
    }
    
    if ( answer < 10 )
    {
      out << "000" << answer;
    }
    else if ( answer < 100 )
    {
      out << "00" << answer;
    }
    else if ( answer < 1000 )
    {
      out << "0" << answer;
    }
    else
    {
      out << answer;
    }
    out << endl;
  }
  
  in.close();
  
  return 0;
}
