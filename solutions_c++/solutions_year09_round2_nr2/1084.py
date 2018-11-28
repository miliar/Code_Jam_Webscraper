#include<cstdio>
#include<algorithm>
#include<string>
using namespace std;

int a[25];

int test(int to)
{
    int i;
    for(i=to-1;i>0;i--)
    {
        if(a[i]<a[i-1]) return 0;
    }
    return 1;
}

int compare(int left,int right)
{
    return left>right;
}

int main()
{
    FILE *p,*in;
    p=fopen("out.txt","w");
    in=fopen("B-large.in","r");
    int t,i,count=1,j,k,min,sub;;
    long long n;
    char ttt[30];
    fscanf(in,"%d",&t);
    while(t--)
    {
        fscanf(in,"%s",ttt);
        i=0;
        for(i=0;ttt[i]!=0;i++) ;
        for(i--,j=0;i>=0;i--,j++)
        {
            a[j]=ttt[i]-48;
        }
        i=j;
        if(test(i)) 
        {
            a[i]=0;
            i++;
        }
        for(j=1;j<i;j++)
        {
            min=10;
            for(k=0;k<j;k++)
            {
                
                if(a[j]<a[k]&&min>a[k]) 
                {
                    min=a[k];
                    sub=k;
                }
            }
            
            if(min!=10)
            {
                a[j]^=a[sub];a[sub]^=a[j];a[j]^=a[sub];
                sort(a,a+j,compare);
                break;
            }
        }
        fprintf(p,"Case #%d: ",count++);
        for(j=i-1;j>=0;j--) fprintf(p,"%d",a[j]);
        fprintf(p,"\n");
    }
    fclose(p);
    fclose(in);
    return 0;
}
