#include<cstdio>
#include<cstring>
#include<queue>
#include<set>
#include<bitset>
#include<map>
#include<vector>
#include<string>
#include<iostream>


using namespace std;

const int MAXN = 100100;

bool isp[MAXN];
int pr[MAXN], tot;

void init()
{
 for (int i = 2; i < MAXN;i++){
          if (!isp[i]){
             pr[tot++] = i;   
             for(long long j = (long long)i*i; j < MAXN; j += i)       
             {
                      isp[j] = true;
             }
          }
     }
}
int main()
{
// freopen("in.txt", "r", stdin);
// freopen("out.txt", "w", stdout);
 init();
 int T, t = 1;
 for (scanf("%d", &T); T--; )
 {
     printf("Case #%d: ",t++);
     int n;
     scanf("%d", &n);
     if(n==1){
              printf("0\n");
              continue;         
     }
     int Max = 0, Min = 0;
     for (int i = 0; i < tot && pr[i] <= n; i++){
        // cout<<pr[i]<<endl;
         Min ++;
         int nn = n;
         while(nn>=pr[i]){                     
              nn/=pr[i];
              Max++;            
         }
     }
    // cout<<Max<<" "<<Min<<endl;
    printf("%d\n",Max+1- Min);
 }
 
//system("pause");
 return 0;          
}

