#include<iostream>
using namespace std;
int main()
{

    int a,b,c,d,e,f;
   int ctr;
    cin>>a;
    ctr=0;
    while(ctr<a){

            cin>>d>>e;
            f=0;
            c=d;
            while(c<=e){
    //for(c=d;c<=e;c++)
                       b=c;

                        if(c<10)
                        {
                                f=0;
                                //f=1;
                        }

                        else if(c<100)
                        {


                           b=((b%10)*10)+(b/10);
                           if(b>c && b<=e)
                                  f++;
                                  //f--;
                        }
                        else if(c<1000)
                        {


                             for(int j=0;j<2;j++)
                             {
                                     b=((b%10)*100)+(b/10);
                                     if(b>c && b<=e)

                                         f++;

                             }
                        }
c++;

    }
    ctr++;
    cout<<"Case #"<<ctr<<": "<<f<<"\n";
}}
