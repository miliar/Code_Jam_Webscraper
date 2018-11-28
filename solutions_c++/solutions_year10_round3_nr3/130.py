#include<fstream>
#include<iostream>
#include<string>
#include<cstring>
#include<algorithm>
using namespace std;
int a[512][512];
int b[512],d[512];
main()
{
    int n,m,i,j,l,p,k,t,c;
    int max;
    FILE* in=fopen("c.txt","r");
    FILE* out=fopen("c.out","w");
    
    char temp[1000];
    int ans;
    
    fscanf(in,"%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        fscanf(in,"%d%d",&m,&n);
        for(i=0;i<m;i++)
        {
            fscanf(in,"%s",temp);
            k=0;
            for(j=0;j<strlen(temp);j++)
            {
                int te;
                if(temp[j]>='0' && temp[j]<='9')te=temp[j]-'0';else te=temp[j]-'A'+10;
                a[i][k++]=(te&0x8)>0;
                a[i][k++]=(te&0x4)>0;
                a[i][k++]=(te&0x2)>0;
                a[i][k++]=(te&0x1)>0;
            }    
        }    
        p=n*m;
        ans=0;
        int mx,my;
        while(p>0)
        {
            max=0;
            for(i=0;i<m;i++)
            {
                for(j=0;j<n;j++)
                {
                    if(a[i][j]!=-1)
                    {
                        k=1;
                        bool ok=true;
                        while(ok)
                        {
                            if(i+k<m && j+k<n && ok)
                            {
                                for(l=i;l<=i+k;l++)if(a[l][j+k]!=1-a[l][j+k-1]){ok=false;break;}
                                for(l=j;l<=j+k;l++)if(a[i+k][l]!=1-a[i+k-1][l]){ok=false;break;}
                            } else ok=false;    
                            k++;
                        }    
                        if(--k>max)
                        {
                            max=k;mx=i;my=j;
                        }    
                    }    
                }    
            }      
            p-=max*max;
            for(i=mx;i<mx+max;i++)for(j=my;j<my+max;j++)a[i][j]=-1;
            if(b[ans-1]==max)d[ans-1]++;
            else 
            {
                b[ans]=max;d[ans]=1;
                ans++;
            }    
        }   
        fprintf(out,"Case #%d: %d\n",tt,ans); 
        for(i=0;i<ans;i++)
        {
            fprintf(out,"%d %d\n",b[i],d[i]); 
        }    
    }    
}    
