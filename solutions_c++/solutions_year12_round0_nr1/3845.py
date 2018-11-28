#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("A-small-attempt0.in");
    ofstream cout("A-small-attempt0.out");
    
    char srt1[] = "zyqeeejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
    char srt2[] = "qazooourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";
    char mapp[26];
    
for (int i = 0;i<110;i++)
mapp[srt1[i] - 'a'] = srt2[i];

//for (int i = 0;i<26;i++)
//cout << (char) ('a' + i) << "->" << mapp[i]<<endl;
int n;
    cin>>n;
    char t;
    cin.get(t);
    for(int i=0;i<n;i++)
    {
            cout << "Case #" << i+1<<": ";
            char c;
            while(1)
            {
                    cin.get( c);
                    if (c>'z' || c<'a')
                    {
                              if (c==' ')
                              cout <<" ";
                              else
                              {
                              cout<<endl;
                              break;
                              }
                    }
                    else
                    {
                        cout<<mapp[c-'a'];
                    }
            }
                        
    }

    cin.close();
    cout.close();
    return 1;
}
