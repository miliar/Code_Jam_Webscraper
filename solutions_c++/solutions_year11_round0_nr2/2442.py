#include<iostream>
#include<string>
using namespace std;

const int MAXN = 512;

char c[MAXN][MAXN];
bool d[MAXN][MAXN];
char seq[MAXN];
int C,D,N;

int main()
{
    int t,test = 1;
    scanf("%d", &t);
    while(test <= t)
    {
               memset(c, 0, sizeof(c));  
               memset(d, 0, sizeof(d));
               char str[4];  
                            
               scanf("%d", &C);
               for(int i = 0; i < C; i++)
               {
                       cin>>str;
                       c[str[0]][str[1]] = str[2];
                       c[str[1]][str[0]] = str[2];  
               }
               
               scanf("%d", &D);
               for(int i = 0; i < D; i++)
               {
                       cin>>str;
                       d[str[0]][str[1]] = 1;
                       d[str[1]][str[0]] = 1; 
               }
               
               scanf("%d", &N);
               cin>>seq;
               
               string res;
               for(int i = 0; i < N; i++)
               {
                       res += seq[i];
                       
                       if(res.size() > 1)
                       {
                               if(c[res[res.size()-1]][res[res.size()-2]] != c[0][0])
                               {
                                     char non_based = c[res[res.size()-1]][res[res.size()-2]];
                                     res = res.substr(0, res.size()-2);
                                     res += non_based;
                               }
                               
                               for(int k1 = 0; k1 < res.size(); k1++)
                                for(int k2 = k1 + 1; k2 < res.size(); k2++)
                                 if(d[res[k1]][res[k2]])
                                  {
                                        res = "";
                                        break;
                                  }
                       }
               }
               
               printf("Case #%d: [", test);
               for(int j = 0; j < (int)res.size() - 1; j++) cout<<res[j]<<", ";
               if(res.size()) cout<<res[res.size()-1]; 
               printf("]\n");
               
               test++;
    }
    return 0;
}
