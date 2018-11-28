#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int main(int argc, char *argv[])
{
 //   ifstream cin("Test.txt");
 //   ofstream cout("Output.txt");
    string Dboard;
    int combine[26][26];
    bool opposed[26][26];
    int found[26];
    
    int TestNum;
    cin >> TestNum;
    int C, D, N;
    char c1, c2, c3;
    string s, o;
    
    int i, m, n;
    
    for(int j = 0; j < TestNum; j++)
    {
            for( m=0; m<26; m++)
                    {
                         for( n=0; n<26; n++)
                         {
                                 combine[m][n] = -1;
                                 opposed[m][n] = false;
                         }
                         found[m] = 0;
                    }
            cin >> C;//cout << C << ' ';
            for(i=0; i<C; i++)
            {
                    cin >> c1 >> c2 >> c3;//cout << c1 << c2  << c3<< ' ';
                    combine[c1-'A'][c2-'A'] = c3-'A';
                    combine[c2-'A'][c1-'A'] = c3-'A';                    
            }
            cin >> D;//cout << D << ' ' ;
            for(i=0; i<D; i++)
            {
                    cin >> c1 >> c2; //cout << c1 << c2 << ' ';
                    opposed[c1-'A'][c2-'A'] = true;
                    opposed[c2-'A'][c1-'A'] = true;                    
            }
                    
            cin >> N;
            cin >> s;
            o = "";
            int end = -1;
            for(i=0; i<N; i++ )
            {
                 if(end == -1)
                 {
                       o += s.at(i);
                       found[s.at(i)-'A']++;
                       end++;    
                 }
                 else    
                 {
                 if(combine[o.at(end)-'A'][s.at(i)-'A'] != -1)
                       {
                       found[o.at(end)-'A']--;
                       o.at(end) = combine[o.at(end)-'A'][s.at(i)-'A'] + 'A';
                       }
                 else
                    { o += s.at(i); end++;}
                 if(found[o.at(end)-'A'] < 2) 
                 {
                       for(n=0; n<26; n++)
                       if((found[n] > 0) && opposed[n][o.at(end)-'A'])
                                    {
                                         o = "";
                                         for( n=0; n<26; n++)
                                              found[n] = 0;
                                              end = -1;                                            
                                    }                      
                 }
                if(end != -1)
                     found[o.at(end)-'A']++;  
                 }    
            }
            cout << "Case #"<< j+1 << ": [" ;
            for(i=0; i+1 < o.length(); i++)
                     cout << o.at(i) << ", "; 
            if(o.length() > 0)
                        cout << o.at(o.length()-1);                    
            cout << "]" << endl;
    }                 
            
    system("PAUSE");
    return EXIT_SUCCESS;
}
