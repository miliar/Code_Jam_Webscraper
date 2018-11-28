#include<iostream>
using namespace std;

int arr[55][55];
int n;
int q[100000]={0};
int cnt = 0;
int cn[51]={0};

int main()
{
    int i, j, k, t, cse = 0;
    int tmp, flg = 2;
    
    scanf("%d", &t);
    while(t--)
    {
     for(i=0;i<50;i++)
      {
         for(j=0;j<50;j++)
           arr[i][j] = 0;
      }
       
      scanf("%d", &n);
      for(i=0;i<n;i++)
       {
         cin >> k;
         for(j=0;j<k;j++)
          {
            cin >> tmp;
            arr[i][tmp-1] = 1;
          }
       }
       
     for(i=0;i<n;i++)
      {
         q[0] = i;
         k = 1;
       for(tmp=0;tmp<k;tmp++)
        {
         for(j=0;j<n;j++)
          {
             if(arr[q[tmp]][j] == 1)
              {
                q[k] = j;
                k++;
              }
          }
         }
        for(j=1;j<k;j++)
           cn[q[j]]++;
           
         for(j=0;j<51;j++)
          {
            if(cn[j] >= 2)
             {
               flg = 1;
               break;
             }
            else
             cn[j] = 0;
          }
        if(flg == 1)
         break;
      }
      cse++;
      if(flg == 1)
       printf("Case #%d: Yes\n", cse);
      else
       printf("Case #%d: No\n", cse);
       
       flg = 2;
       for(i=0;i<51;i++)
        cn[i] = 0;
        
    } 
}
              
