#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<stack>
#include<queue>
//#include<fstream>

#define iter(n) for( int i = 0 ; i < n ; i++ )

using namespace std;

#define MAX 16
#define MAXS 5001

//typedef vector<int> vint;
//typedef vector<float> vfloat;
//typedef vector<double> vdouble;
//typedef vector<char> vchar;
//typedef vector< pair<int , int> > vpair;

int L,D,N;
char str[MAXS][MAX];

int countPatterns(string pattern)
{
    vector<set<char> > v;
    int cnt = 0 , sz = 0;
    while(cnt < pattern.size())
              {
                 v.push_back(set<char>());
                 
                 if(pattern[cnt] == '(')
                 {
                     cnt++;
                  
                     while(pattern[cnt] != ')')
                       {
                        // cout << pattern[cnt] << endl;
                        v[sz].insert(pattern[cnt]);
                        cnt++;
                       }
                  }
                 else
                   {
                      v[sz].insert(pattern[cnt]);
                   }
               cnt++;
               sz++;
              }

    int num = 0;
    
    if(L != v.size()) return 0;
    
    for(int i = 0 ; i < D ; i++)
            {
             int j;
             for(j = 0 ; j < L ; j++)
                     {
                      if(v[j].find(str[i][j]) == v[j].end()) break;
                     } 
             if(j == L) num++;
            }
            
    return num;
}

int main()
{

//ifstream cin("A-large.in");
//ofstream cout("A-large.out");

string pattern;
cin >> L >> D >> N;

for(int i = 0 ; i < D ; i++)
        cin >> str[i];

for(int i = 1 ; i <= N ; i++)
        {
         cin >> pattern;
         cout << "Case #" << i << ": " << countPatterns(pattern) << endl;
        }

//  system("pause");
return 0;
}
