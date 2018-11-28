/*
TASK: next number Code Jam '09 1B
LANG: C++
*/

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char str[100];

int sf(const void *a, const void *b)
{
    return *(char *)a - *(char *)b;
}

inline int check(int begin, int k)
{
    int i;
    for(i=begin;i<k-1;i++)
        if(str[i]<str[i+1])
            return 0; //don't need new digit
    
    return 1; //need new digit
}

int main()
{
    int cases,cc,k,i,t;
    int original;
    int a,b;
    
    scanf("%d", &cases);
    
    for(cc=0;cc<cases;cc++)
    {
        printf("Case #%d: ", cc+1);
        
        scanf("%s", &str);
        
        k = strlen(str);
        for(i=0;i<k;i++)
            str[i]-='0';
        
        a = 0; //begin
        
        while(1)
        {
            if(check(a,k)) //needs new digit
            {
                if(a==0) //special case
                {
                    str[k++]=0;
                    for(i=1;i<k;i++)
                    {
                        if(str[i]!=0 && str[i]<str[0])
                        {
                            t = str[i];
                            str[i]=str[0];
                            str[0]=t;
                        }
                    }
                    printf("%d", str[0]);
                    
                    qsort(&str[1],k-1,sizeof(str[0]),sf);
                    for(i=1;i<k;i++)
                        printf("%d", str[i]);
                    printf("\n");
                    break;
                }
                
                a--;
                original = str[a]; 
                
                t=str[a];
                str[a]=str[a+1];
                str[a+1]=t;
                
                for(i=a+2;i<k;i++)
                    if(str[i]<str[a] && str[i]>original)
                    {
                        t=str[a];
                        str[a]=str[i];
                        str[i]=t;
                    }
                
                qsort(&str[a+1], k-a-1, sizeof(str[0]), sf);
                
                for(i=a;i<k;i++)
                    printf("%d", str[i]);
                printf("\n");
                
                break;
            }
            else
            {
                if(a!=0)
                    printf("%d", str[a-1]);
                a++;
            }
            
        }
        
    }
    
    return 0;
}
