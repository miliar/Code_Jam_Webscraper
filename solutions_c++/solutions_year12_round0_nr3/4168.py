#include<iostream>
using namespace std;

int arr[4]={0, 0, 0, 0};
int lim1[4]={0, 0, 0, 0};
int lim2[4]={0, 0, 0, 0};
int tmpz[4]={0, 0, 0, 0};
int ans=0, l1, l2, num, s;

int main()
{
    int i, j, t, n=0, tmps, cse=0;
    int a, b, tmp, k, flg=2;
    cin >> t;
    while(t--)
    {
      scanf("%d", &a);
      scanf("%d", &b);
    if(a >= 10 && b>=10)
    {
      tmp = b;
      n=0;
      while(tmp > 0)
        { 
         tmps = tmp%10;
         lim1[3-n] = tmps;
         n++;
         tmp = tmp/10;
        }
      l1 = n;
      
      tmp = a;
      n=0;
      while(tmp > 0)
        { 
         tmps = tmp%10;
         lim2[3-n] = tmps;
         n++;
         tmp = tmp/10;
        }
      l2 = n;
        
      n=0;
      for(i=a;i<b;i++)
       {
         tmp = i;
         n = 0;
        while(tmp > 0)
        { 
         tmps = tmp%10;
         arr[3-n] = tmps;
         n++;
         tmp = tmp/10;
        }
        
        for(j=0;j<4;j++)
         tmpz[j] = arr[j];
         
        num = n;
         tmps = 0;
         while(tmps < n-1)
         {
             
             tmp = arr[3];
             if(4-n < 3)
             arr[3] = arr[2];
             if(4-n < 2)
             arr[2] = arr[1];
             if(4-n < 1)
             arr[1] = arr[0];        
             arr[4-n] = tmp;
             
             for(j=0;j<4;j++)
              {
                if(arr[j] < tmpz[j])
                   {
                    flg = 1;    
                    break;
                   }
                 else if(arr[j] > tmpz[j])
                   break;
              }
              
              if(j==4)
               flg = 1;
                          
             if(flg == 2)
             {
             for(j=4-num;j<4;j++)
              {
                 if(arr[j] < lim2[j])
                   {
                    flg = 1;    
                    break;
                   }
                 else if(arr[j] > lim2[j])
                   break;
              }
             }
             if(flg == 2)
             {
             for(j=4-l1;j<4;j++)
              {
                 if(arr[j] > lim1[j])
                  {
                    flg = 1;    
                    break;
                   }
                 else if(arr[j] < lim1[j])
                   break;
              }
             }
             if(flg == 2)
              ans++;
             tmps++;
             flg = 2;
         
         }
        arr[0] = 0;arr[1] = 0;arr[2] = 0;arr[3] = 0;
       }
      }
      else
         ans = 0;
       cse++;
       printf("Case #%d: %d\n", cse, ans);
       ans = 0;
        arr[0] = 0;arr[1] = 0;arr[2] = 0;arr[3] = 0;
        lim1[0] = 0;lim1[1] = 0;lim1[2] = 0;lim1[3] = 0;
        lim2[0] = 0;lim2[1] = 0;lim2[2] = 0;lim2[3] = 0;
    }
}
