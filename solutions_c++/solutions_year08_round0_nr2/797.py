#include<iostream>
using namespace std;

int N,T,NA,NB,AA[110],AD[110],BA[110],BD[110],FA[110],FB[110],CA=0,CB=0,FLAG=0,t=0,ti,tj,i,j,ctr;

void bubblesort(int num1[],int num2[],int n)
{
     int i,j,temp,FFLAG=1;
     for(i=0;i<n-1 && FFLAG==1;i++)
     {
                 FFLAG=0;
                 for(j=0;j<n-i-1;j++)
                                     if(num1[j+1]<num1[j])
                                     {
                                                        FFLAG=1;
                                                        temp=num1[j];
                                                        num1[j]=num1[j+1];
                                                        num1[j+1]=temp;
                                                        temp=num2[j];
                                                        num2[j]=num2[j+1];
                                                        num2[j+1]=temp;
                                     }
                                     if (num1[j+1]==num1[j])
                                     {
                                        if (num2[j+1]<num2[j])
                                        {
                                                        FFLAG=1;
                                                        temp=num1[j];
                                                        num1[j]=num1[j+1];
                                                        num1[j+1]=temp;
                                                        temp=num2[j];
                                                        num2[j]=num2[j+1];
                                                        num2[j+1]=temp;
                                        }
                                     }
                                                           
     }
}


int main()
{
    freopen("input6.txt","r",stdin);
    freopen("output9.txt","w",stdout);
    char str1[8],str2[8];
    AD[0]=0,AA[0]=0,BD[0]=0,BA[0]=0;
    scanf("%d",&N);
    while (N)
    {
          ctr++;
          scanf("%d",&T);
          scanf("%d%d",&NA,&NB);
          for (i=1;i<=NA+1;i++)
              FA[i]=0;
          for (i=1;i<=NB+1;i++)
              FB[i]=0;
          for (i=1;i<=NA;i++)
          {
              scanf("%s%s",str1,str2);
              AD[i]=((str1[0]-48)*10+(str1[1]-48))*60+(str1[3]-48)*10+str1[4]-48;
              BA[i]=((str2[0]-48)*10+(str2[1]-48))*60+(str2[3]-48)*10+str2[4]-48+T;
          }
          bubblesort(AD,BA,NA+1);
          for (i=1;i<=NB;i++)
          {
              scanf("%s%s",str1,str2);
              BD[i]=((str1[0]-48)*10+(str1[1]-48))*60+(str1[3]-48)*10+str1[4]-48;
              AA[i]=((str2[0]-48)*10+(str2[1]-48))*60+(str2[3]-48)*10+str2[4]-48+T;
          }
          bubblesort(BD,AA,NB+1);    
          CA=NA;CB=NB;
          i=1;j=1;
          for (i=1;i<=NA;i++)
          {
              FLAG=0;
              for (j=1;j<=NB && FLAG==0;j++)
                  if (BA[i]<=BD[j] && FB[j]==0)
                  {
                                  FB[j]=1;
                                  CB-=1;
                                  FLAG=1;
                  }
          }
          for (i=1;i<=NB;i++)
          {
              FLAG=0;
              for (j=1;j<=NA && FLAG==0;j++)
                  if (AA[i]<=AD[j] && FA[j]==0)
                  {
                                  FA[j]=1;
                                  CA-=1;
                                  FLAG=1;
                  }
          }
          printf("Case #%d: %d %d\n",ctr,CA,CB);
          N--;
    }
}
