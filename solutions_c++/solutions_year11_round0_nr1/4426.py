#include<fstream>
#include<iostream>
#include<stdio.h>
using namespace std;
int mod(int);
main()
{
    ifstream fin;
    ofstream fout("small.txt");
    fin.open("A-large.in");
    if(!fin)
        cout<<"File not foound";
    int t,n,j,texp,ttotal=0,to=0,tb=0,poso=1,posb=1;
    int h[100];
    char c;
    fin>>t;
    for(int i=1;i<=t;i++)
    {
        fin>>n;
        for(j=0;j<n;j++)
        {
            fin>>c;
            fin>>h[j];
            if(c=='B')
                h[j]*=-1;
        }
        for(j=0;j<n;j++)
        {
            if(h[j]>0)
            {
                texp=mod(h[j]-poso);
                if(texp>to)
                {
                    ttotal+=texp-to+1;
                    tb+=texp-to+1;
                }
                else
                {
                    ttotal+=1;
                    tb+=1;
                }
                poso=h[j];
                to=0;
            }
            else
            {
                texp=mod((-1*h[j])-posb);
                if(texp>tb)
                {
                    ttotal+=texp-tb+1;
                    to+=texp-tb+1;
                }
                else
                {
                    ttotal+=1;
                    to+=1;
                }
                posb=(-1*h[j]);
                tb=0;
            }

        }
        fout<<"Case #"<<i<<": "<<ttotal<<endl;
        ttotal=0,to=0,tb=0,poso=1,posb=1;

    }
    fin.close();
    fout.close();
}
int mod(int x)
{
    if(x>0)
    return x;
    else return x*-1;
}
