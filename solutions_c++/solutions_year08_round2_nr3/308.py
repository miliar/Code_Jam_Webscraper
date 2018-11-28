#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("C.out");
    
    
    long K[5000];
    int vis[5000];
    long T,num,ind,i,j,n,aux;

    in>>T;
    for (int X=1; X<=T; X++)
    {
        in>>num;
        for (i=0; i<num; i++)
            vis[i]=0;
        ind=0;
        for (i=0; i<num; i++)
        {
            j=i+1;    
            while (j!=0)
            {                                
                if (ind<num)
                {
                    if (vis[ind]==0)
                    {
                        j--;
                        if (j==0)
                            break;
                    }
                    ind++;
                }
                else
                    ind=0;                
            }
            K[ind]=i+1;
            vis[ind]=1;            
        }
        in>>n;
        out<<"Case #"<<X<<":";
        for (i=0; i<n; i++)
        {
            in>>aux;
            out<<" "<<K[aux-1];
        }
        out<<endl;
    }
    
	return 0;
}