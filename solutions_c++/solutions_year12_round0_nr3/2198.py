#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include <windows.h>
using namespace std;

int main()
{
    int cnt,cnt1,i,j,l,low,high,t,old,n,total,x,d;
    int buff,str[100];
    fstream fp;
    fp.open("input.txt");
    fp >> t;
    //cout<<t<<endl;
    for(i=0;i<t;i++)
    {
        total=0;
            fp >> low;
            fp >> high;
            for(n=low;n<=high;n++)
            {
                old=n;
                cnt=0;
                while(old!=0)
                {
                    old=old/10;
                    cnt++;
                }
                x=-1;
                cnt1=cnt;
                old=n;
                if(n>9)
                {
                    while(cnt1--)
                    {
                        str[cnt1]=old%10;
                        old=old/10;
                    }
                    while(n!=x)
                    {
                        buff=str[cnt-1];
                        for(j=cnt-1;j>0;j--)
                        {
                            str[j]=str[j-1];
                        }
                        str[0]=buff;
                        cnt1=cnt;
                        x=0;
                        d=0;
                        while(cnt1--)
                        {
                            x=x+str[cnt1]*pow(10,d);
                            d++;
                        }
                       // Sleep(500);
                       // cout<<"Val of x:"<<x<<endl;
                        if(x>=low&&x<=high&&x!=n)
                            total++;
                        //    if(n==10)
                        //break;//exit(1);
                    }
                    //if(n==10)
                      //  exit(1);
                }

                    //cout<<"Case #"<<i+1<<": "<<total<<endl;

        }
        cout<<"Case #"<<i+1<<": "<<total/2<<endl;
        //if(i==2);
        //exit(0);
        //for(x=0;x<cnt;x++)
           // str[x]=0;
    }
}
