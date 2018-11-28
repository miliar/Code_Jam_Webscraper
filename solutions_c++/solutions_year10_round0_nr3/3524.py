#include <iostream>
#include<fstream>
#include <conio.h>
using namespace std;



int check(long int r,long int k, int n, int g[])
{
    int i=0,j=0,sum=0,c=0,F=0;
    int fg[1000],fc[1000],k2=0,l=0,fk,pos,m,n2,Fold;
    bool flag = false;
    
    for(j=0;j<r;j++)
    {
        Fold=F;
        for(c=g[F],i=(F+1)%n;(c+g[i]<=k)&&(i!=F);i=(i+1)%n)
            c+=g[i];
        
        fg[l]=F;
        fc[l]=c;
        l++;
        sum+=c;
        F=i;
        
        for(k2=0,fk=0;k2<l;k2++)
        {
            if(fg[k2]==F && (j+1)<r)
            {
                flag=true;
                c=0;
                pos=k2;
            }        
            
            if(flag)
            {
                c+=fc[k2];
                fk++;
                
            }
        }
        
        if(flag)
        {
            sum+=((r-j-1)/fk)*c;
            for(m=0,n2=pos;m<((r-j-1)%fk);m++,n2++)
            sum+=fc[n2];
            break;
        }
   }   
    return sum;
}


int main()
{
    ofstream op("C-small-attempt0.out");
	ifstream ip("C-small-attempt0.in");
    
    int N,T,g[1000];
    int i,j;
    long int R,k;

    ip>>T;

    for(i=0;i<T;i++)
    {
        ip>>R>>k>>N;
        for(j=0;j<N;j++) ip>>g[j];
        
        j=check(R,k,N,g);
        cout<<"Case #"<<i+1<<": "<<j<<"\n";
        op<<"Case #"<<i+1<<": "<<j<<"\n";
    }

    getch();
    return 1;
}
