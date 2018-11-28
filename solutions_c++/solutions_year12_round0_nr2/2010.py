#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ofstream out("out3.in");
int main()
{
    int t,i,j,n,c,p,x,r1,r2,cnt;
    ifstream in("b.in");
    if(in.is_open())
    {
        in>>t;
        for(j=1;j<=t;j++)
        {
            in>>n;
            in>>c;
            in>>p;
            cnt=r1=r2=0;
            out<<"Case #"<<j<<": ";
            for(i=0;i<n;i++)
            {
                in>>x;
                if(p!=0)
                {
                    r1=p+2*(p-1);
                    if(p>1)
                        r2=p+2*(p-2);
                    else
                        r2=1;

                    if(c==0 && x>=r1)
                        cnt+=1;
                    else if(c!=0)
                    {
                        if(x>=r1)
                            cnt+=1;
                        else if(x>=r2)
                        {
                            cnt+=1;
                            c--;
                        }
                    }
                }
                else
                    cnt++;
            }
            out<<cnt;
            out<<endl;
        }
    }
    return 0;
}
