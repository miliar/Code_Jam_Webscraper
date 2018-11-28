#include<iostream>
#include<vector>
#include<string>
using namespace std;
int k=0;
int count(int a,int b)
{ int i=a;if(a<=9) i=10;
while(i<=b)
{if(i==1000) {i++;continue;}
if(i <100) {if( (i%10) == (i/10)) {i++;continue;}
           else {int j=(i%10)*10+ i/10;if(j>i && j<=b) k++;i++;continue;  }}
if(i>99 && ((i%10) == ((i/10)%10)) && ((i%10) == (i/100) )) {i++;continue;}
//processing nums between 100 and 1000
int num=0;
//1st rotation
int ii=i;
num=ii%100;num*=10;num+=(ii/100);
if(num>i && num <=b) k++;
//2nd rotation
ii=num;
num=ii%100;num*=10;num+=(ii/100);
if(num>i && num <=b) k++;
i++;                 
}                 
return 0;
}
int main(){
    int t,cases=1;cin>>t;
    while(t--)
    {k=0;
    int a,b;
    cin>>a>>b;
    count(a,b);
    cout<<"Case #"<<cases++<<": "<<k<<endl;
    }
return 0;
}

    
