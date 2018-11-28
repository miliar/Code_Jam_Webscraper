#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    long long int ot,l,ol,bt,bl,systime,i,j,t,n;
    char c;
    ifstream fi("input.txt");
    ofstream fo("output.txt");
    fi>>t;
    for(j=1;j<=t;j++)
    {
        
        ot=bt=systime=0;
        bl=ol=1;
        fi>>n;
        for(i=0;i<n;i++)
        {
            fi>>c>>l;
            if(c=='O')
            {
                ot+=abs(l-ol)+1;
                ol=l;
                if(ot<=systime)
                {
                    systime++;
                    ot=systime;
                }
                else systime=ot;
            }
            else if(c=='B')
            {
                bt+=abs(l-bl)+1;
                bl=l;
                if(bt<=systime)
                {
                    systime++;
                    bt=systime;
                }
                else systime=bt;
            }
        }
        fo<<"Case #"<<j<<": "<<systime<<"\n";
    }       
    return 0;
}    
