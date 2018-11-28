#include<iostream>
//#include<conio.h>
using namespace std;
int main(void)
{
     freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    unsigned long long int k,a;
    int n,t,i=1,d=1;
    scanf("%d",&t);
    while(t-->0)
    {unsigned long long b=1;
        cin>>n>>k;
        for(i=0;i<n;i++)
        {   
            b=2*b;
        }
        if(k%b==b-1)
        cout<<"Case #"<<d<<": "<<"ON"<<endl;
        else
        cout<<"Case #"<<d<<": "<<"OFF"<<endl;
        d++;
    }
//getch();
}
        
    
 
