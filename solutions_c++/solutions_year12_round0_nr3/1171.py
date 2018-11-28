#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<map>
using namespace std;
long long a,b;

int check(long long num)
{
    
    char arr[10];
    itoa(num,arr,10);
    int len=strlen(arr);
    char temp[10];
    int ub=0;
    int count=0;
    int ct=1;
  //  cout<<endl<<"got:"<<arr<<endl;
    // int hatch[2000001]={0};
    map<int,int> hatch;
    do
    {
   
    for(int i=ct;i<len;i++)
    {
        temp[ub]=arr[i];
        ub++;
            
    }
    for(int i=0;i<ct;i++)
    {
            temp[ub]=arr[i];
            ub++;
    }
    /*cout<<endl<<"string:";
    for(int i=0;i<ub;i++)
            cout<<temp[i];
    cout<<endl;
    cout<<endl;*/
    temp[ub]='\0';
    long long i2=atoi(temp);
   
    if(i2>=a && i2<=b && i2!=num && hatch[i2]==0)
    {        count++;hatch[i2]=1;}
   // cout<<i2<<" "<<ub<<" "<<count<<endl;
    ct++;
    ub=0;
    }while(ct<len);
    return count;
}
int main()
{
    int test;
    int ctr=0;
    cin>>test;
    while(test--)
    {
    ctr++;
    cin>>a>>b;
    
//    check(12345);
long long ct=0;
    for(long long i=a;i<=b;i++)
    {
           //  cout<<"going:"<<i<<endl;
            // if(hatch[i]==0)
             //{
             long long num=check(i);
            // cout<<i<<" "<<ct+num<<endl;
             ct+=num;
            // cout<<endl<<endl;        
            //}
             
    }
    cout<<"Case #"<<ctr<<": "<<(ct/2)<<endl;
}
    return 0;
}
    
