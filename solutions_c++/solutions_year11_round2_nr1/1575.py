#include<iostream>
using namespace std;

int main()
{
    FILE *inp=fopen("input.txt","r");
    FILE *out=fopen("output.txt","w");
    int t,i,n;
    int res[100][2];
    float wp[100];
    float owp[100];
    float oowp[100];
    char a[100][100];
    float rpi[100];
    fscanf(inp,"%d",&t);
    for(i=0;i<t;i++)
    {
               fscanf(inp,"%d",&n);
               for(int j=0;j<n;j++)
                       //for(int k=0;k<n;k++)
                       {
                               fscanf(inp,"%s",a[j]);
                               //fprintf(out,"%c\n",a[j][k]);
                               } 
               for(int j=0;j<n;j++)
               {
                       int w=0,l=0;
                       for(int k=0;k<n;k++)
                       {
                        if(a[j][k]=='1')
                            w++;
                        else if(a[j][k]=='0')
                             l++;
                        }
                        res[j][0]=w;
                        res[j][1]=l;
                        wp[j]=(float)w/(float)(w+l);
                        //fprintf(out,"WP::%f   %d   %d\n",wp[j],j,n);
               }
               for(int j=0;j<n;j++)
               {
                       owp[j]=0.0;
                       int ct=0;
                       for(int k=0;k<n;k++)
                       {
                               if(k==j || a[k][j]=='.')
                                       continue;
                                  ct++;
                                  int w,l;
                                  w=res[k][0];
                                  l=res[k][1];
                                  if(a[k][j]=='1')
                                                  w--;
                                  else if(a[k][j]=='0')
                                       l--;
                                  owp[j]+=(float)w/(float)(w+l);
                       }
                       owp[j]/=ct;
               }      
                for(int j=0;j<n;j++)
                {
                        oowp[j]=0.0;
                        int ct=0;
                        for(int k=0;k<n;k++)
                        {
                                if(k==j || a[j][k]=='.')
                                        continue;
                                ct++;
                                oowp[j]+=owp[k];
                        }
                        oowp[j]/=ct;
                }
                fprintf(out,"Case #%d:\n",i+1);
                for(int j=0;j<n;j++)
                fprintf(out,"%f\n",0.25*wp[j]+0.5*owp[j]+0.25*oowp[j]);
                }
                }
                               
                                       
                    
