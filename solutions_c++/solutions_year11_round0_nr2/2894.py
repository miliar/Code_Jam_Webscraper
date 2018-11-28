#include <iostream>
#include<fstream>
#include <conio.h>
using namespace std;

int search(char c, char s[],int N)
{
    for(int i=0;i<N;i++) if(s[i]==c) return i;
    return -1;
}

int main()
{
    ofstream op("B.op");
	ifstream ip("B.ip");
    
    int N,T,C,D,mi,i,j,et,k,m,flag;
    char Cs[36][4], Ds[28][3], Ns[101], Es[101],ch;

    ip>>T;
    for(mi=0;mi<T;mi++)
    {
        ip>>C;
        for(j=0;j<C;j++) ip>>Cs[j];
        ip>>D;
        for(j=0;j<D;j++) ip>>Ds[j];
        ip>>N;
        ip>>Ns;
        
        cout<<"Case #"<<mi+1<<": [";
        op<<"Case #"<<mi+1<<": [";
        
        Es[0]=Ns[0];
        for(i=1,et=0;i<N;i++)
        {
            flag=1;
        
            for(j=0;j<C && flag && et>=0;j++)
            {
                k=search(Ns[i],Cs[j], 2);
                if(k!=-1)
                {
                    k=(k+1)%2;
                    if(Es[et]==Cs[j][k])
                    {
                        Es[et]=Cs[j][2];
                        flag=0;
                    }
                }
            }
        
            for(j=0;j<D && flag && et>=0;j++)
            {
                k=search(Ns[i],Ds[j],2);
                if(k!=-1)
                {
                    k=(k+1)%2;
                    m=search(Ds[j][k], Es, et+1);
                    if(m!=-1)
                    {
                        et=-1;
                        flag=0;
                    }
                }
            }
        
            if(flag)
            {
                et++;
                Es[et]=Ns[i];
            }
        }

        for(i=0;i<=et;i++) (i==et)?cout<<Es[i]:cout<<Es[i]<<", ";
        for(i=0;i<=et;i++) (i==et)?op<<Es[i]:op<<Es[i]<<", ";
        cout<<"]\n";
        op<<"]\n";
    }
    
    op.close();
    ip.close();
    getch();
    return 1;
}
