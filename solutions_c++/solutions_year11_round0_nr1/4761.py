#include<iostream>
#include<stdio.h>
#include<vector>
using namespace std;
int main()
{   int n,t,i,temp,stateo,stateb,count=0,j,flag;
    long time;
    char ch;
    vector<int> ob;
    vector<char> b;
    FILE *fp1,*fp2;
    fp1=fopen("C:\\a.txt","r");
    fp2=fopen("C:\\res.txt","w");
    fscanf(fp1,"%d",&n);
    ob.clear();
    b.clear();
    while(n--)
    {
             fscanf(fp1,"%d",&t);
             time=0;
             stateo=1;
             stateb=1;
             for(i=0;i<t;i++)
             {        ch=getc(fp1);
                      fscanf(fp1,"%c%d",&ch,&temp);
                      b.push_back(ch);
                      ob.push_back(temp);

             }
             for(i=0;i<t;i++)
             {        flag=0;
                      if(b[i]=='O')
                      {            temp=ob[i]-stateo;
                                   if(temp<0)
                                             temp=-(temp);
                                   time+=temp; //move
                                   temp++;
                                   time++;    //push btn 
                                   stateo=ob[i];
                                   for(j=i+1;j<t;j++)
                                   {                 if(b[j]=='B')
                                                     {             flag=1;
                                                                   break;
                                                     }
                                   }
                                   if(flag==1)
                                   {          if(ob[j]>stateb)
                                              {               while(temp-- && stateb<ob[j])
                                                                           stateb++;
                                              }
                                              else if(ob[j]<stateb)
                                              {               while(temp-- && stateb>ob[j])
                                                                           stateb--;
                                              }
                                   }
                      }
                      else if(b[i]=='B')
                      {            temp=ob[i]-stateb;
                                   if(temp<0)
                                             temp=-(temp);
                                   time+=temp;  //move
                                   temp++; 
                                   time++;    //push btn 
                                   stateb=ob[i];
                                   for(j=i+1;j<t;j++)
                                   {                 if(b[j]=='O')
                                                     {             flag=1;
                                                                   break;
                                                     }
                                   }
                                   if(flag==1)
                                   {          if(ob[j]>stateo)
                                              {               while(temp-- && stateo<ob[j])
                                                                           stateo++;
                                              }
                                              else if(ob[j]<stateo)
                                              {               while(temp-- && stateo>ob[j])
                                                                           stateo--;
                                              }
                                   }
                      }     
             }
             count++;
             fprintf(fp2,"%s","Case #");
             fprintf(fp2,"%d",count);
             fprintf(fp2,"%s ",":");
             fprintf(fp2,"%d\n",time);
             ob.clear();
             b.clear();
    }
    return 0;
}

