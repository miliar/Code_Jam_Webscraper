#include<stdio.h>
#include<iostream>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<map>
using namespace std;

int main()
{
    FILE *in = fopen("C-large.in","r");
    FILE *out = fopen("C_out.txt","w");

    int n;
    long long int a,b,temp;
    map<long long int,long long int> m;
    fscanf(in,"%d\n",&n);

    for(int Case=1; Case<=n; Case++){
        fprintf(out,"Case #%d: ",Case);

        fscanf(in,"%lld %lld\n",&a,&b);
        printf("a:%lld   b:%lld\n",a,b);
        int len = 1;
        temp = a;
        while((temp/10)!=0){
            len++;
            temp /= 10;
        }
        //printf("len : %d\n",len);
        long long int now = a;
        long long int ans = 0;
        m.clear();
        
        while(1)
        {
            temp = now;
            //m[now]=1;
           // printf("temp:%d\n",temp);
            
            long long int divi = 1;
            long long int x = 1;
            
            for(int i=0;i<len-1;i++)
                divi *= 10;
            for(int i=0;i<len;i++)
                x *= 10;            
           // printf("x: %d   divi:%d\n",x,divi);
            
            for(int i=0;i<len;i++){
               
                
                long long int left = temp/divi;
                temp *= 10;
                //printf("%d  %d \n",temp,left);
                temp += left;
               // printf("%d  %d \n",temp,left);
                temp = temp % x;
               // printf("%d  %d \n",temp,left);
                long long int z = now*x + temp;
                if(temp>=a && temp<=b && now<temp && m[z]==0)
                {
                    m[z]=1;
                    ans++;
                   // printf("now : %lld   ans : %lld   %lld\n",now,temp,z);
                }
            }
           // system("pause");
            if(now==b)
                break;
            now++;
        }//system("pause");
        fprintf(out,"%d\n",ans);
    }
//scanf("1");
    return 0;
}
