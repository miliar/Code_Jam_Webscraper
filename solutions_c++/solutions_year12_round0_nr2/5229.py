#include <fstream.h>
#include <conio.h>
#include <string.h>
#include <stdio.h>
#include<stdio.h>
#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<memory.h>
int main()
{
    int check(int,int,int,int);
    int score[100][100],iscore[100][100][3],i,j,k,t,n[100],s[100],p[100],flag[100],temp,sp[100],max[100],entry;
    long ind(int,int),ii;
    FILE *fp=fopen("D:/google codejam/qualification round/b/files/B-small-attempt8.in", "r"); 
    FILE *ofp=fopen("D:/google codejam/qualification round/b/files/out.out", "w");
   	int mod(int);
    fscanf(fp, "%d", &t);
    for(i=0;i<t;i++)
    {
             fscanf(fp,"%d",&n[i]);//cout<<n[i]<<endl;
             fscanf(fp,"%d",&s[i]);//cout<<s[i]<<endl;
             fscanf(fp,"%d",&p[i]);//cout<<p[i]<<endl;
     
    
            
             for(j=0;j<n[i];j++)
             {
                                fscanf(fp,"%d",&score[i][j]);//cout<<score[i][j]<<endl;
                                
             }
     
     }
     
     for(i=0;i<t;i++)
     {       
             entry=s[i];
             for(j=0;j<n[i];j++)
             {
                                if(score[i][j]>=(p[i]*3))
                                flag[i]+=1;
                                else if(score[i][j]==((p[i]*3))-1)
                                flag[i]+=1;
                                else if(score[i][j]==((p[i]*3))-2)
                                flag[i]+=1;
                                else if(score[i][j]==((p[i]*3))-3)
                                {if(score[i][j]>3)
                                    { if(entry>=1)
                                     {
                                                 flag[i]+=1;
                                                 entry=entry-1;
                                     }}
                                    // else if(entry==0){cout<<"#"<<i<<" done s = "<<s[i]<<endl;}
                                }
                                else if(score[i][j]==((p[i]*3))-4)
                                {if(score[i][j]>4)
                                    { if(entry>=1)
                                     {
                                                 flag[i]+=1;
                                                 entry=entry-1;
                                     }}
                                    // else if(entry==0)
                                     //{cout<<"##"<<i<<" done s = "<<s[i]<<endl;}// else{cout<<s[i]<<endl;}
                                }
             }
                                     
                                
     
     }
    for(i=0;i<t;i++)
    {
                    cout<<"Case #"<<i+1<<": "<<flag[i]<<endl;
                    fprintf(ofp, "Case #%d: %d\n", i+1, flag[i]);
    }
    getch();
    return 0;
}     
     
//functions after main

int mod(int x)
{
        if(x<0)
        x=-x;
        return x;
}
