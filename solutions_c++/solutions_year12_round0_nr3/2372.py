#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int i,j,k,T;
    FILE* fin = fopen("c.in","r");
    FILE* fout = fopen("c.out","w");
    int pow10[9]={0};
    pow10[0]=1;
    for (i=1;i<=8;++i) pow10[i] = 10*pow10[i-1];
    
    fscanf(fin, "%d", &T);
    for (i=1;i<=T;++i)
    {
        int a,b, tdigit=0,temp;
        long long count=0;
        bool state[2000010]={0};
        
        fscanf(fin, "%d %d",&a,&b);
        temp = a;
        while (temp > 0)
        {
              temp /= 10;
              tdigit++;      
        }
        
        
        for (j=a;j<=b-1;++j)
        {
            if (state[j]==1) continue;
            int temp2=0;
            state[j] = 1;
            for (k=1;k<=tdigit-1;++k)
            {
                temp = (j%pow10[k])*pow10[tdigit-k] + j/pow10[k];
                if  (temp > j && temp <= b && state[temp]==0)
                {
                    state[temp] = 1;
                    temp2++;
                    //count++;
                }
            }   
            count += (temp2*(temp2+1))/2;
        }
        fprintf(fout,"Case #%d: %lld\n", i,count);
    }
    /*
    int a1 = 3153256;
    int n1 = 7;
    int a2 = (a1%pow10[n1])*pow10[7-n1] + a1/pow10[n1];
    fprintf(fout, "%d --> %d\n",a1,a2);
    */
}


