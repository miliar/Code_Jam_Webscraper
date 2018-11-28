#include <iostream>
#include<fstream>
#include <conio.h>
#include <math.h>
using namespace std;



int check(int C[], int N)
{
    int i,j,s,p,sb,pb,set,tset,ls=0,lst;
    
    for(i=1,s=C[0];i<N;i++) s = s ^ C[i];
    if(s) return 0;
    
    for(i=0,set=0;i<N;i++) set+=pow(2,i); 
    set/=2;
//    cout<<"   set   = "<<set<<"       \n";
    for(i=0;i<set;i++)
    {
        for(j=0,tset=(set-i),sb=0,pb=0,s=0,p=0;j<N;j++)
        {
//            cout<<"\n   tset   = "<<tset<<"       ";
            if(tset%2==0)
            {
                sb = sb ^ C[N-j-1];
                s = s + C[N-j-1];
            } else
            {
//                cout<<"p";
                pb = pb ^ C[N-j-1];
                p = p + C[N-j-1];
            }
            tset = tset>>1;
        }
        if(sb == pb)
        {
            lst=(s>p)?s:p;
            ls=(lst>ls)?lst:ls;
//            cout<<" "<<lst;
        }
    }
    
    return ls;
}


int main()
{
    ofstream op("C.op");
	ifstream ip("C.ip");
    
    int N,T,i,j;
    int C[1000];

    ip>>T;
    for(i=0;i<T;i++)
    {
        ip>>N;
        for(j=0;j<N;j++) ip>>C[j];
        
        j=check(C,N);

        (j)?cout<<"Case #"<<i+1<<": "<<j<<"\n":cout<<"Case #"<<i+1<<": "<<"NO\n";
        (j)?op<<"Case #"<<i+1<<": "<<j<<"\n":op<<"Case #"<<i+1<<": "<<"NO\n";
    }
    op.close();
    ip.close();
    getch();
    return 1;
}
