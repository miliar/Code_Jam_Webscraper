#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream in("x.in");
    ofstream out("x.out");
    long i,p,j,ide,l,t,n,s,ss,x,y;
    in>>t;
    for(i=1;i<=t;i++)
    {
        ide=5;
        y=0;
        ss=0;
        in>>n>>s>>p;
        for(j=1;j<=n;j++)
        {
            in>>l;
            if (l%3==0)
            {

                if (l>=2&&l<=28&&ss<s)
                {
                x=l/3-1;

                if (x+2>=p)
                {y++;
                ss++;
                ide=0;
                }
                }

                else {
                //    if (l>=2&&l<=28&&ss<s){
                    x=l/3;
                if (x>=p) y++;

            }

            if (l/3>=p&&ide==0)
            {
                ss--;
            }
            }



            if (l%3==1)
            {
                if (l>=2&&l<=28&&ss<s)
                {
                    x=l/3-1;
                    if (x+2>=p)
                    {
                        ide=1;
                      y++;
                      ss++;
                    }
                }
                else
                {
                    //if (l>=2&&l<=28&&ss<s){
                    x=l/3;
                if (x+1>=p) y++;

                }
                if (l/3+1>=p&&ide==1) ss--;


            }
            if (l%3==2)
            {
                if (l>=2&&l<=28&&ss<s)
                {
                    x=l/3;
                    if (x+2>=p)
                    {
                        ide=2;
                      ss++;
                      y++;
                    }
                }
                else {
                //    if (l>=2&&l<=28&&ss<s){
                    x=l/3;
                if (x+1>=p) y++;


                }
                if (l/3+1>=p&&ide==2) ss--;
                }

              }

        out<<"Case #"<<i<<": "<<y<<"  "<<endl;
    }
}
