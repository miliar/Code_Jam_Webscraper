#include<iostream>

using namespace std;

int c, d, n;
char ca, cb, cc;
char da, db;
char nn[11];
char res[11];
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);    
    freopen("B-small-attempt0.out", "w", stdout);
    
    int cas, icas, i, j;
    cin >> cas;
    for(icas = 1; icas <= cas; icas++)
    {
             cin >> c;
             if(c==1) cin >> ca >> cb >> cc;
             cin >> d;
             if(d==1)  cin >> da >> db;
             cin >> n;
             for(i = 0; i < n; i++)
             {
                   cin >> nn[i];
             }
             int last = 1;
             for(i = 1; i < n; i++)
             {
                   if(last==0)
                   {
                               nn[last++] = nn[i];
                               continue;
                   }
                   if(c>0)
                   {
                      if((nn[i]==ca&&nn[last-1]==cb) || (nn[i]==cb&&nn[last-1]==ca))
                      {
                          nn[last-1] = cc;
                          continue;
                      }
                   }
                   if(d>0)
                   {
                          bool clear = false;
                          for(j = 0; j < last; j++)
                          {
                                 if((nn[i]==da&&nn[j]==db) || (nn[i]==db&&nn[j]==da))
                                 {
                                        clear = true;
                                 }
                          }
                          if(clear==true)
                          {
                                      last = 0;
                                      continue;
                          }
                   }
                   nn[last++] = nn[i];
             }
             printf("Case #%d: [", icas);
             for(i = 0; i < last; i++)
             {
                   if(i==0)
                           printf("%c", nn[i]);
                   else
                       printf(", %c", nn[i]);
             }
             printf("]\n");
    }
    return 0;
}
