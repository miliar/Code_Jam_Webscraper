#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<stdlib.h>
int t,i,j,a,b;
double p[10000];
int flag[99999];
double prob,sum[100];
double small[1000];
int smallno=0;
float keep[100]={0},back[100][99]={0},enter[100]={0};
int allcorect=0;
int backtry(int pos)
{
    int i,j,k;
    allcorect=1;
    for(i=0;i<a-pos+1;i++)
    {
                        if(flag[i]==0)
                                      allcorect=0;
    }
    if(allcorect)
                 return pos+b-a+1;
    else         return pos+b-a+1+b+1;
}
int keeptry()
{
    int i,j,k;
    
    if(allcorect)
                 return b-a+1;
    else         return b-a+b+2;
}
int entertry()
{
    return b+2;
}
int check(int pos)
{
    int i,j,k;
    
    double min;
    prob=1;
    allcorect=1;
    
    for(i=0;i<a;i++)
    {               prob*=((flag[i]==0)?1-p[i]:p[i]);
                    if(flag[i]==0)
                                  allcorect=0;
        }
    prob=1;
            for(i=0;i<a;i++)
                  {
                            if(flag[i])
                                       prob*=p[i];
                            else
                                       prob*=(1-p[i]);
                                       if(prob==0)
                                                  ;//cout<<"p[i]="<<p[i]<<endl;
                            } 
           
                            if(prob==0)
                       ;//cout<<"heeeeeeeeeeeeeeeeeeeee";
    keep[smallno]=keeptry();
    for(i=0;i<a;i++)
    {
                   back[smallno][i]=backtry(i+1);
                   back[smallno][i]*=prob;
                   if(prob==0)
                                          cout<<"";
    }
    enter[smallno]=entertry();
    enter[smallno]*=prob;
    keep[smallno]*=prob;
    //cout<<"//"<<enter[smallno]<<"//";
    smallno++;
}
int val()
{
    int i,j,k;
    for(i=0;i<a;i++)
                    flag[i]=0;
    check(0);
    while(1)
    {
            int carry=1;
            for(i=a-1;i>=0;i--)
            {
                       if(carry)
                       {
                                if(flag[i]==1)
                                              flag[i]=0;
                                else{
                                     flag[i]=1;
                                     carry=0;
                                     }
                       }else break;
            }
            check(0);
            prob=1;
            for(i=0;i<a;i++)
                   prob*=(flag[i]==1?p[i]:1-p[i]);
            
            int tmpflag=1;
            for(i=0;i<a;i++)
                            if(flag[i]==0)
                                       tmpflag=0;
            if(tmpflag)
                       break;
    }
}
int main()
{   int i,j,k;
    double entersum,keepsum,backsum[100],min;
    ifstream fin("C://google//password//a.in");
    ofstream fout("C://google//password//out.out");
    fin>>t;
    for(i=0;i<t;i++)
    {               smallno=0;
                    for(j=0;j<100;j++)
                                      sum[j]=0;
                    fin>>a>>b;
                    for(j=0;j<a;j++)
                    {
                            fin>>p[j];        
                    }
                    for(j=0;j<a;j++)
                                    flag[j]=0;
                    val();
                    for(j=0;j<100;j++)
                                      backsum[j]=0;
                    for(j=entersum=keepsum=0;j<smallno;j++)
                    {
                                                           entersum+=enter[j];
                                                           keepsum+=keep[j];
                                                           for(k=0;k<a;k++)
                                                           {               backsum[k]+=back[j][k];
                                                                          // cout<<"//"<<backsum[k]<<"//";
                                                           }
                    }
                    //min=entersum;
                    if(keepsum<entersum)
                                        min=keepsum;
                    else
                                        min=entersum;
                    for(k=0;k<smallno;k++)
                                   if(backsum[k]<min&&backsum[k])
                                                      min=backsum[k];
                    char asd[100];
                    sprintf(asd,"Case #%d: %f\n",i+1,min);
                    fout<<asd;
    }
    getch();
    
}
