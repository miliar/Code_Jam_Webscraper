#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int T,i,ii,A,B;
    float p[4];
    float product,j,min;
    float x[3];
    cin>>T;
    for(i=0;i<T;i++)
    {
                    cin>>A;
                    cin>>B;
                    for(ii=0;ii<A;ii++) cin>>p[ii];
                    product=1;
                    for(ii=0;ii<A;ii++) product*=p[ii];
                    x[0]=(2*B-A+2)-(1+B)*(product);  //first case
                    product+=((product/p[A-1])*(1-p[A-1]));
                    x[1]=(3+B-A)*product+((4+2*B-A)*(1-product)); //second case
                    product=1;
                    if(A>2){
                            for(ii=0;ii<A-1;ii++) product*=p[ii];
                            j=product*(1-p[A-2])*(1-p[A-1]);
                            j=j+product*(1-p[A-2])*p[A-1];
                            product*=p[A-2];
                            j=j+product*(1-p[A-1]);
                            product*=p[A-1];
                            j=j+product;
                            product=j;
                            }
                    x[2]=(5+B-A)*product+((6+2*B-A)*(1-product)) ; //third case
                    min=2+B;
                    min=2+B;
                    for(ii=0;ii<3;ii++) if(min>x[ii]) min=x[ii];
                    cout<<"Case #"<<i+1<<": "<<setprecision (6)<< fixed<<min<<endl;
                    } 
                    }
