#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<iostream>
using namespace std;
int l,d,n;
char a[5000][16];
char s[500];
int term[15][2];
int p[2][5005];
int main()
{   
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); 
    scanf("%d%d%d",&l,&d,&n);
    for(int i=0;i<d;i++)
    scanf("%s",a[i]);
    for(int i=1;i<=n;i++)
    {
           scanf("%s",s);
           int t=strlen(s); 
           int index=0;
           for(int j=0;j<l;j++)
           {
                   int num=0;
                   if(s[index]!='(')
                   {
                           term[j][0]=term[j][1]=index;
                           index++;
                   }
                   else
                   {       
                        index++;
                        term[j][0]=index;
                        while(s[index]!=')')
                        {                   
                               index++;             
                        }
                        index++;
                        term[j][1]=index-2;
                   }
           }
          // for(int j=0;j<l;j++)
          // cout<<term[j][0]<<" "<<term[j][1]<<endl;
           p[0][0]=d+1;
           for(int j=0;j<d;j++)
           p[0][j+1]=j;
           for(int j=0;j<l;j++)
           {        
                    
                    p[(j+1)&1][0]=1;
                    for(int q=1;q<p[j&1][0];q++)
                   
                   {
                           for(int k=term[j][0];k<=term[j][1];k++)
                           if(s[k]==a[p[j&1][q]][j])
                           {         
                                      //cout<<"nihao  "<<j<<" "<<k<<" "<<p[j&1][q]<<endl;
                                      p[(j+1)&1][p[(j+1)&1][0]]=p[j&1][q]; 
                                      p[(j+1)&1][0]++;  
                                      break;          
                           }
                   }
           }
           printf("Case #%d: %d\n",i,p[l&1][0]-1);
           
    }
    
    //system("pause");
    return 0;
}
