#include"stdio.h"
#include"stdlib.h"
#include"string.h"
#include"algorithm"
#include"iostream"
#include"map"
#include"set"
#include"math.h"
#include"vector"

using namespace std;

map<long long , int> f[520];
vector<int> set1 , set2;
long long num[520];

void Print(int p , long long v)
{
     if(p == 0) return;
     if(f[p][v] == 0)
                Print(p - 1 , v);
     else if(f[p][v] == 1)
          set1.push_back(num[p]) , Print(p - 1 , v - num[p]);
     else set2.push_back(num[p]) , Print(p - 1 , v + num[p]);
}
                
     
int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    
    int T , n;
    
    scanf("%d", &T);
    for(int Case = 1 ; Case <= T ; Case++)
    {
            scanf("%d" , &n);
            for(int i = 1 ; i <= n ; i++)
                    scanf("%I64d", &num[i]);
            
            printf("Case #%d:\n" , Case);
            
            set<long long> now , next;
            now.insert(0);
            
            for(int i = 1 ; i <= n ; i++)
            {
                    for(set<long long> :: iterator iter = now.begin() ; iter != now.end() ; iter++)
                    {
                                           long long k = *iter;
                                           
                                           next.insert(k);
                                           f[i][k] = 0;
                                           f[i][k + num[i]] = 1;
                                           f[i][k - num[i]] = -1;
                                           
                                           if(k + num[i] == 0)
                                           {
                                                set1.clear() , set2.clear();
                                                Print(i , 0);
                                                
                                                int size = set1.size();
                                                printf("%d" , set1[0]);
                                                for(int i = 1 ; i < size ; i++)
                                                        printf(" %d", set1[i]);
                                                printf("\n");
                                                
                                                size = set2.size();
                                                printf("%d" , set2[0]);
                                                for(int i = 1 ; i < size ; i++)
                                                        printf(" %d", set2[i]);
                                                printf("\n");
                                                
                                                goto NEXT;
                                           }
                                           next.insert(k + num[i]);
                                           
                                           if(k - num[i] == 0)
                                           {
                                                set1.clear() , set2.clear();
                                                Print(i , 0);
                                                
                                                
                                                int size = set1.size();
                                                printf("%d" , set1[0]);
                                                for(int i = 1 ; i < size ; i++)
                                                        printf(" %d", set1[i]);
                                                printf("\n");
                                                
                                                size = set2.size();
                                                printf("%d" , set2[0]);
                                                for(int i = 1 ; i < size ; i++)
                                                        printf(" %d", set2[i]);
                                                printf("\n");
                                                
                                                goto NEXT;
                                           }
                                           next.insert(k - num[i]);
                    }
                    now = next;
                    next.clear();
            }
            
            printf("Impossible\n");
            NEXT: for(int i = 1 ; i <= n ; i++) f[i].clear();
    }
    
    return 0;
}
