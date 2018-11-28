#include<iostream>
using namespace std;
char a[5000][15],b[1000];
int sub;

int find(char t)
{
    int mark=0;
    if(b[sub]!='(')
    {
        
        if(b[sub]==t)
        {
            sub++;         
            return 1;
        }
        else 
        {
            sub++;
            return 0;
        }
        
    }
    for(;b[sub]!=')';sub++)
    {
        if(b[sub]==t) mark=1;
    }
    sub++;
    if(mark) return 1;
    else return 0;
}

int main()
{
    int l,d,n,i,j,k,count;
    FILE *p,*in;
    p=fopen("out.txt","w");
	in=fopen("A-large.in","r");
    fscanf(in,"%d%d%d",&l,&d,&n);
    
        for(i=0;i<d;i++)
        {
            fscanf(in,"%s",a[i]);
        }
        for(i=1;i<=n;i++)
        {
            fscanf(in,"%s",b);
            count=0;
            for(j=0;j<d;j++)
            {
                sub=0;
                for(k=0;k<l;k++)
                {
                    if(find(a[j][k])) continue;
                    else break;
                }
                if(k==l) count++;
            }
            fprintf(p,"Case #%d: %d\n",i,count);
        }
    fclose(p);
	fclose(in);
    return 0;
}
        
