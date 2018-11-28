#include<stdio.h>
#include<iostream>
#include<math.h>
 
using namespace std;
bool flag[2000006];
 
long long permute(int n)
{
        if(n<=1)
                return 0;
        else
                return ((long long)(n)*(n-1))/2;
}
 
int digit(int n)
{
        if(n==0)
                return 0;
        else
                return 1+digit(n/10);
}
 
int main()
{
        int i, count = 0;
        long long ans;
        int lastDig, numDig, NOD, tenPow;
        int A, B, T, num;
        int pair;
        scanf("%d", &T);
        
        while(T--)
        {       
                ans = 0;
                count++;
                
                scanf("%d", &A);
                scanf("%d", &B);
                
                numDig = digit(A);
                tenPow = pow(10, numDig-1);
                
                for(i=A; i<=B; i++)
                        flag[i] = 0;
                for(i=0; i<10; i++)
                        flag[i] = 1;
                
                for(i=A; i<=B; i++)
                {
                        if(flag[i] == 1)
                                continue;
 
                        flag[i] = 1;
                        num = i;
                        NOD = numDig-1;         
                        pair = 1;       
                        
                        while(NOD--)
                        {
                                lastDig = num%10;
                                num = num/10 + lastDig*tenPow;
                                
                                if(lastDig == 0)
                                        continue;
                                //cout<<num<<" ";
                                if(num >= A && num<=B)  
                                {
                                        if(flag[num] == 1)
                                        {
                                                continue;
                                        }
                                        else
                                        {
                                                flag[num] = 1;
                                                pair++;
                                        }
                                }
                        }       
                        ans += permute(pair);
                }
                
                cout<<"Case #"<<count<<": "<<ans<<"\n";
        }
        
        return 0;
}
