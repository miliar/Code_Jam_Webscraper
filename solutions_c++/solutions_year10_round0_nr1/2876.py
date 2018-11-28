#include<iostream>
#include<string>
#include<math.h>
using namespace std;
int main()
{
    double n;
    long long k , temp;
    int i , j , t ,ii=0;
    freopen("F:\\google2010\\A-large.in" ,"r" ,stdin);
    freopen("F:\\google2010\\outl.txt","w" ,stdout);  
    
    cin>>t;
    i=0;
    while(t--)
    {   
    cin>>n>>k; 
    i++;
    temp=pow(2, n);
	if((k+1)%temp == 0)
	cout<<"Case #"<<i<<": ON"<<endl;
	else cout<<"Case #"<<i<<": OFF"<<endl;
    }    
        
}  

