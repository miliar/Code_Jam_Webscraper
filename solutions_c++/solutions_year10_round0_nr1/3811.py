#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;

int testResult(int,int);
int testResult(int sw_num, int snaps)
{
    if(sw_num==1)
    {
                 if(snaps%2==0)
                               return 0;
                 else 
                               return 1;
    }
    else
    {
                 if((snaps%(int)(pow(2,sw_num-1))==(int)(pow(2,sw_num-1)-1)) && testResult(sw_num-1,snaps)==1)
                                                           return(1);
                 else 
                                                           return 0;
                                                                        
    }                 
}    

int main()
{
    int no_Snappers;
    long int no_Snaps;
    int testCases,cases;
    cin>>testCases;
    cases=testCases;
    for(int i=1;testCases>1;testCases--,i++)
    {
                                 scanf("%d %d",&no_Snappers,&no_Snaps);
                                 if(testResult(no_Snappers+1,no_Snaps))
                                        cout<<"Case #"<<i<<": ON\n";
                                 else
                                        cout<<"Case #"<<i<<": OFF\n";
    }
    scanf("%d %d",&no_Snappers,&no_Snaps);
    if(testResult(no_Snappers+1,no_Snaps))
                                 cout<<"Case #"<<cases<<": ON";
    else
                                 cout<<"Case #"<<cases<<": OFF";
}

