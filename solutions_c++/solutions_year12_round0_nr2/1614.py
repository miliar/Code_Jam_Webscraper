#include<stdio.h>
#include<iostream>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<map>
using namespace std;

int main()
{
    FILE *in = fopen("B-large.in","r");
    FILE *out = fopen("B_out.txt","w");

    int testcase,n,s,p,t[110];
    fscanf(in,"%d\n",&testcase);
    for(int Case=1; Case<=testcase; Case++){
        fprintf(out,"Case #%d: ",Case);
        
        fscanf(in,"%d\n",&n);
        fscanf(in,"%d\n",&s);
        fscanf(in,"%d\n",&p);
        
        for(int i=0;i<n;i++)
            fscanf(in,"%d\n",&t[i]);
        
        sort(t,t+n);
        
        int ans =0,normal = p*3-2,strange = p*3-4;
        if(strange<0)   strange=0;
        
       // printf("%d %d\n",normal,strange);
       
        for(int i=n-1;i>=0;i--)
        {
            //printf("\n%d %d",t[i],s);
            if(t[i]<p)
                continue;
                
            if(t[i]>=normal)
                ans++;
            else if(t[i]>=strange && s>0){
                s--;
                ans++;
            }
            
        }
        fprintf(out,"%d\n",ans);
           // printf("%d  ",t[i]);
       // printf("%d\n",ans);
    }
//scanf("1");
    return 0;
}
