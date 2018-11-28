#include <iostream>
#include<fstream>
#include <conio.h>
using namespace std;

int check(char R[], int P[], int N)
{
    int i=0,j=0,o=1,b=1,s=0;
    int op=0,bp=0;
    
    for(j=op;j<N;j++) if(R[j]=='O' || R[j]=='o') {op=j; break;}
    for(j=bp;j<N;j++) if(R[j]=='B' || R[j]=='b') {bp=j; break;}
    
    for(s=0,i=0;i<N;s++)
    {
        if(R[i]=='O' || R[i]=='o')
        {
            //O needs to press button
            if(o==P[i])
            {
                //Press button
                i++;
                for(j=op+1;j<N;j++) if(R[j]=='O' || R[j]=='o') {op=j; break;}
            } else if(o<P[i]) o++;
            else o--;
            
            if(b<P[bp]) b++;
            else if(b>P[bp]) b--;
            
        } else
        {
            //B needs to press button
            if(b==P[i])
            {
                //Press button
                i++;
                for(j=bp+1;j<N;j++) if(R[j]=='B' || R[j]=='b') {bp=j; break;}
            } else if(b<P[i]) b++;
            else b--;
            
            if(o<P[op]) o++;
            else if(o>P[op]) o--;
        }
    }

    return s;
}


int main()
{
    ofstream op("A.op");
	ifstream ip("A.ip");
    
    int N,T,i,j;
    char R[100];
    int P[100];

    ip>>T;
    for(i=0;i<T;i++)
    {
        ip>>N;
        for(j=0;j<N;j++)
        {
            ip>>R[j];
            ip>>P[j];
        }
        j=check(R,P,N);
        cout<<"Case #"<<i+1<<": "<<j;
        op<<"Case #"<<i+1<<": "<<j;

        cout<<"\n";
        op<<"\n";
    }
    op.close();
    ip.close();
    getch();
    return 1;
}
