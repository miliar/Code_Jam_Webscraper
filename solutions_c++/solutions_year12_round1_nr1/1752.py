#include<iostream>
#include<algorithm>
using namespace std;

float arr[10];
float prob[3];
float anss[5];

int main()
{
    int a, b, t, s = 0;
    int i, j, k, tmp, cnt, cse=0;
    float ans;
    
    scanf("%d", &t);
    while(t--)
    {
      scanf("%d %d", &a, &b);
       
      for(i=0;i<a;i++)
       scanf("%f", &prob[i]);
              
      for(i=0;i<(1<<a);i++)
      {
        tmp = i;
        cnt = 0;
        j = 0;
        ans = 1;
        while(j != a)
        {
          if(tmp&1)
           {
              ans = ans * prob[(a - j)-1];
           }
          else
           ans = ans * (1.000000-prob[(a - j)-1]);
           tmp = tmp >> 1;
           j++;
        }
                 
        arr[s] = ans;
        s++;
      }
      
      if(a == 1)
          {  
           anss[0] = arr[1]*(b-a+1) + ((1.000000-arr[1])*(b-a+b+2));
           anss[1] = (b+a+1)*1;
           anss[2] = (b+2)*1;
           
           sort(anss, anss+3);
           cse++;
           printf("Case #%d: %.6f\n", cse, anss[0]);
          }
      else if(a == 2)
       {
           anss[0] = arr[3]*(b-a+1) + ((1.000000-arr[3])*(b-a+b+2));
           anss[1] = (b+a+1)*1;
           anss[2] = (b+2)*1;
           anss[3] = ((arr[3] + arr[2])*(b-a+3)) + ((1-(arr[3] + arr[2]))*(b-a+3+b+1));
           
           sort(anss, anss+4);
           cse++;
           printf("Case #%d: %.6f\n", cse, anss[0]);
       }
      else if(a == 3)
       {
           anss[0] = arr[7]*(b-a+1) + ((1.000000-arr[7])*(b-a+b+2));
           anss[1] = (b+a+1)*1;
           anss[2] = (b+2)*1;
           anss[3] = ((arr[7] + arr[6])*(b-a+3)) + ((1-(arr[7] + arr[6]))*(b-a+3+b+1));
           anss[4] = ((arr[7] + arr[5])*(b-a+5)) + ((1-(arr[7] + arr[5]))*(b-a+5+b+1));
                       
           sort(anss, anss+5);
           cse++;
           printf("Case #%d: %.6f\n", cse, anss[0]);
       }
       s = 0;
    }
    //system("pause");
}
            
      
