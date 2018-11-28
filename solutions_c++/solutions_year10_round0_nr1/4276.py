#include <iostream>
#include<fstream>
#include <conio.h>
using namespace std;



int check(int n, int k)
{
    int i=0,j=0;
    int state[30];
    for(i=0; i<n;i++) state[i]=0;
    
    for(i=0;i<k;i++)
    {
        for(j=0;j<n;j++)
        {
            if(!state[j])
            {
                state[j] = 1;
                break;
            }else
                state[j] = 0;        
        }
    }
    j=1;
    
    for(i=0;i<n;i++)
    if(!state[i])
    {
        j=0;
        break;
    }
    
    return j;
}


int main()
{
    ofstream op("A-small-attempt1.on");
	ifstream ip("A-small-attempt1.in");
    
    int N,K,T,i;
    char ch[100];

    ip>>T;
    for(i=0;i<T;i++)
    {
        ip>>N>>K;
        cout<<"Case #"<<i+1<<": ";
        op<<"Case #"<<i+1<<": ";
        if(check(N,K))
        {
            cout<<"ON";
            op<<"ON";
        }
        else
        {
            cout<<"OFF";
            op<<"OFF";
        }
        cout<<"\n";
        op<<"\n";
    }

    getch();
    return 1;
}
