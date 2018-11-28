#include<iostream>
#include<math.h>
using namespace std;

int main()
{
    
    long int t;
    //ifstream fin("A-small-input.in");
    //ofstream fout("out.txt");
    int n[100000];
    long int k[100000];
    cin>>t;
    for(long int i=0;i<t;i++)
    {
        cin>>n[i]>>k[i];
    }
    
    for(long int i=0;i<t;i++)
    {
        if(k[i]==0)
        {
            cout<<"Case #"<<i+1<<": OFF\n";
            continue;
        }
        if(k[i]%(int)pow(2,n[i]) == pow(2,n[i])-1)
            cout<<"Case #"<<i+1<<": ON\n";
            
        else
            cout<<"Case #"<<i+1<<": OFF\n";
            
    } 
       return 0;
       
}
