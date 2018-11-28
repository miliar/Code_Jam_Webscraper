#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

int digits(int n)
{
    int d=0;
    while(n>0)
    {
        n=n/10;
        d++;
    }
    return d;
}
main()
{
    int n,i;
    ifstream ifs;
    ifs.open("C-small-attempt1.in");
    ifs>>n;
    int a[n],b[n],count[n];
    for(i=0;i<n;i++)
    {
        ifs>>a[i]>>b[i];
        count[i]=0;
    }
    ifs.close();
    int c=0,nod;

    while(c<n)
    {
        nod = digits(a[c]);
        for(i=a[c];i<b[c];i++)
        {
            int newi[nod],l,m=0;
                for (l=0;l<nod;l++)
                {
                    newi[l]=0;
                }
            int cno=i;
            int k = 0;
            while(k<nod)
            {
                int d =  cno%10;
                cno = cno/10;
                cno = d*pow(10,(nod - 1)) + cno;
                for(int j=(i+1);j<=b[c];j++)
                {
                    if (cno==j)
                    {
                        bool check = false;
                        for (l=0;l<nod;l++)
                        {
                            if(cno == newi[l])
                             check = true;
                             break;
                        }
                        if(!check)
                        {
                        newi[m++] = cno;
                       // cout<<i<<" "<<cno<<endl;
                        count[c]++;
                        break;
                        }
                    }
                }
               k++;
            }
        }
        c++;
    }
    ofstream ofs;
    ofs.open("Out.txt");
    for(i=0;i<n;i++)
    {
        ofs<<"Case #"<<(i+1)<<": "<<count[i]<<endl;
    }
    ofs.close();
}


