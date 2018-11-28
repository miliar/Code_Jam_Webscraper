#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
ofstream out("out3.in");
int findLength(int n)
{
    int c=0;
    while(n>0)
    {
        n/=10;
        c++;
    }
    return c;
}
int main()
{
    int t,i,j,n,c,start,end,s,e,p,abc,newnum,x,cnt,dig,tot,arr[10000],ab;
    ifstream in("b.in");
    if(in.is_open())
    {
        in>>t;
        for(j=1;j<=t;j++)
        {
            in>>start;
            in>>end;
            tot=0;
            for(i=start;i<end;i++)
            {
                p=findLength(i)-1;
                x=10;dig=p;
                cnt=0;arr[0]=0;
                for(abc=1;abc<=p;abc++)
                {
                    s=i%x;
                    e=i/x;
                    newnum=s*pow(10,dig)+e;
                    /*if(i==123)
                        cout<<"I = "<<i<<"\t"<<newnum<<"\t"<<s<<"\t"<<e<<endl;*/
                    if(newnum>i && newnum<=end)
                    {
                        for(ab=0;ab<cnt;ab++)
                            if(arr[ab]==newnum)
                                break;
                        if(ab==cnt)
                            arr[cnt++]=newnum;
                        /*if(p==3)
                            cout<<"I:\t"<<i<<"\t"<<newnum<<"\tCnt: "<<cnt<<endl;*/

                    }
                    x*=10;
                    dig--;
                }
                tot+=cnt;
            }
            out<<"Case #"<<j<<": "<<tot<<endl;
        }
    }
        return 0;
}
