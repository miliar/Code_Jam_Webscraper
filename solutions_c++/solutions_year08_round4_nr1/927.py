#include <iostream>
#include <iterator>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

int value[10001];
int gate[10001];
int change[10001];

int acc(int j, int v, int m)
{
    int a,b;
    if (value[j] == v) return 0;
    else
    {
        if (2 * j <= m)
        {
           if (gate[j] == 1)
           {
              if (v == 1)
              {
                if (change[j] == 1)
                {
               
                 if (value[2 * j] == 1 || value[2 *j+1] == 1)
                   return 1;
                 else
                 {
                     a = acc(2*j, 1, m);
                        b = acc(2 * j + 1, 1, m);
                        if (a != -1 && b != -1)
                          return 1 + min(a, b);
                        else
                        {
                            if (a != -1) return 1 + a;
                            if (b != -1) return 1 + b;
                            return -1;
                        }
                 }
               }
                 else
                {
                   a = acc(2*j, 1, m); b = acc(2*j +1, 1, m);
                   if (a != -1 && b != -1)
                     return a+b;
                   else
                     return -1;
                }
             
              }
              else
              {
                  //cout<<"Hi";
                  a = acc(2*j, 0, m);
                  b = acc(2 * j +1, 0, m);
                  if (a != -1 && b != -1) return min(a,b);
                  if (a != -1) return a;
                  if (b != -1) return b;
                  return -1;
              }
            }
            else
            {
               if (v == 0)
               {
                  if (change[j] == 1)
                  {
                    if (value[2 * j] == 0 || value[2 *j+1] == 0)
                      return 1;
                    else
                    {
                        a = acc(2*j, 0, m);
                        b = acc(2 * j + 1, 0, m);
                        if (a != -1 && b != -1)
                          return 1 + min(a, b);
                        else
                          {
                                 if (a != -1) return 1+a;
                                 if (b != -1) return 1+b;
                                 return -1;
                          }
                    }
                  }
                  else
                 {
                     a = acc(2*j, 0, m); b = acc(2*j +1, 0, m);
                     if (a != -1 && b != -1)
                       return a+b;
                     else
                       return -1;
                 }
               }
               else
               {
                   //cout<<"Hi";
                   a = acc(2*j, 1, m);
                  b = acc(2 * j +1, 1, m);
                  if (a!= -1 && b != -1)
                   return min(a,b);
                  if (a != -1) return a;
                  if (b != -1) return b;
                  return -1;
               }
            }
           }
            else
              return -1;
        }
} 


int main()
{
    int n, m, v, ret;
    cin>>n;
    
    for (int i = 0; i < n; i++)
    {
       cin>>m>>v;
       for (int j = 0; j < m; j++)
       {
           value[j] = 0;
           gate[j] = 0;
           change[j] = 0;
       }
       for (int j = 1; j <= (m - 1) / 2; j++)
         cin>>gate[j]>>change[j];
       for (int j = (m + 1) / 2; j <= m; j++)
         cin>>value[j];
       
       for (int j = (m - 1) / 2; j > 0; j--)
       {
           if (gate[j] == 0)
             value[j] = max(value[2 * j], value[2 * j + 1]);
           else
             value[j] = min(value[2 * j], value[2 * j + 1]);
       }
       /*for (int j = 1; j <=m; j++)
         cout<<value[j]<<" ";
         cout<<endl;
       for (int j = 1; j <=m; j++)
         cout<<gate[j]<<" ";
         cout<<endl;
       for (int j = 1; j <=m; j++)
         cout<<change[j]<<" ";
         cout<<endl;*/
       
       ret = acc(1, v, m);
       if (ret == -1)
          cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl; 
       else
         cout<<"Case #"<<i+1<<": "<<ret<<endl;       
    }
    return 0;
}
