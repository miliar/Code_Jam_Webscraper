#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;
short T[30];
void limpiar(long long n)
{
    for(int i=0;i<n;i++)
      T[i]=0;
}
bool isLight(long long  num)
{
    long long cont=0;
    for(long long i=(num-1);i>=0;i--)
    {
        if(T[i]==1)
            cont++;
        //cout<<T[i];
    }
    //cout<<endl;
    if(cont==num)
        return true;
    else return false;
}
void add(long long n)
{
    short carry=0;
    T[0]=T[0]+1;
    for(long long j=0;j<n;j++)
    {

        if(carry==1)
        {
            T[j]=T[j]+carry;
        }
        if(T[j]==2)
       {
           carry=1;
           T[j]=0;
       }
       else if(T[j]==3)
       {
           carry=1;
           T[j]=1;
       }
       else
       {
           carry=0;
       }

       if(carry==0)
        break;
    }
}
void sumar(long long n,long long num)
{

   for(long long i=0;i<n;i++)
   {
       add(num);
       isLight(num);

   }
}

int main(int argc,char **argv)
{
    ifstream in;
	ofstream out;

	in.open(argv[1],ifstream::in);
	out.open("salida.txt");


    int num;
    in.fail();
    long long n,k;

	in>>num;
	for(int i=0;i<num;i++)
    {
        in>>n>>k;

        limpiar(n);
        sumar(k,n);
        if(isLight(n)==true)
          out<<"Case #"<<(i+1)<<": ON\n";
        else
            out<<"Case #"<<(i+1)<<": OFF\n";
    }
	in.close();
	out.close();
    return 0;
}
