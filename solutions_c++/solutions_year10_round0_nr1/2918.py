//Vignesh M
//Code


//Oh dear lord!~! you are great!

#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
using namespace std;

int Solution(int n, long long double k);
long long double PowerFx(long long double expov)
{
     long long double ExpValue=1;
     for(long long double MyTicker=0;MyTicker<expov;MyTicker++)
     ExpValue*=2;  
     return(ExpValue);     
}

int main()
{
    int n;
    long long double k;
    ifstream inStream;
    inStream.open("myQuestion.in");
    ofstream outStream;
    outStream.open("myAnswer.out");
    
    int T=0;    inStream>>T;
    
    for(int tcount=0;tcount<T;tcount++)
    {
       inStream>>n;
       inStream>>k;
       if(Solution(n,k)) outStream<<"Case #"<<tcount+1<<": ON\n";
       else outStream<<"Case #"<<tcount+1<<": OFF\n";
    }
   
    return 0;
}



int Solution(int n, long long double k)
{
    int TickingMyTicker=1;
    long long double IncrementValue;
    IncrementValue= (PowerFx(n)-1)+((TickingMyTicker-1)*PowerFx(n));    
    int res=-1,SwitchStateFlag=0;
    
    if(k<IncrementValue)
    { 
     res=0;
      SwitchStateFlag=1;
    }
    else if(k==IncrementValue) res=SwitchStateFlag=1;
    else
    {        
        while(k>IncrementValue)
        {
           TickingMyTicker++;
           IncrementValue= (PowerFx(n)-1)+((TickingMyTicker-1)*PowerFx(n));
            if(k < IncrementValue)
                { 
                                res=0;
                      SwitchStateFlag=1;
                 }          
            else if(k==IncrementValue)res= SwitchStateFlag=1;
    
        }
    
    }
    
    if(!SwitchStateFlag) res=0;
    
    return res;
}

