#include "iostream"

using namespace std;

struct Robot{
       char ch;
       int  c;
};
Robot r[1000];
int n , T , f[1000];

void solve()
{
    
     for(int i = 0; i < n ;i++)
     {
          bool flag = false;   
          for(int j = i - 1 ; j >= 0 ; j--)
          {
                if(r[i].ch == r[j].ch)
                {
                    f[i] = f[j] + abs(r[i].c - r[j].c) + 1;
                    if(f[i] <= f[i - 1])
                       f[i] = f[i - 1] + 1;
                    flag = true;    
                    break;         
              }
         }
         if(flag == false)
         {
             f[i] = abs(r[i].c - 1) + 1;
             if(i - 1 >= 0 && f[i] <= f[i - 1])
             {
                  f[i] = f[i - 1] + 1;
                   
             }
         }
     }
}

int  main()
{
     freopen("A-large.in","r",stdin);
     freopen("A-large.out","w",stdout);
     
     cin >> T;
     for(int t = 1 ; t <= T ;t++)
     {
        cin >> n ;
        memset(f , 0 , sizeof(f));
        for(int i =  0 ; i < n ;i++)
        {
             cin >> r[i].ch >> r[i].c;
        }
        solve();
        cout <<"Case #"<<t<<": "<<f[n - 1]<<endl; 
     }
   //  while(1);
     return 0;
}
