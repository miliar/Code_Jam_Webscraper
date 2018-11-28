#include <iostream.h>
#include <math.h>
#include <fstream.h>
class Buffer
{
 private:
         long M[8];
         long total;
 public:
         Buffer (){total=0;}
         void add(long n){M[total]=n; total++;}
         bool inBuffer(long n){ for (long i=0; i<total; i++) if(M[i]==n) return true; return false;}
};
int main()
{
    long K[8]={1,10,100,1000,10000,100000,1000000,10000000};
    ifstream in("C-large.in",ios::in);
    ofstream out("BIGoutputCPP.txt",ios::out);
    long T,A,B,cases=0,i,j;
    in>>T;
    while (in>>A>>B)
    {
          cases++;
          long total=0;
          long numOfDigits=long(log10(B))+1;
          long lastDigit,M;
          //cout<<"Case "<<cases<<" Number of digits="<<numOfDigits<<endl;
          for (i=A; i<B; i++)
          {
              M=i;
              Buffer buffer;
              for (j=0; j<numOfDigits; j++)
              {
                  M*=10;
                  lastDigit=M/K[numOfDigits];
                  M%=K[numOfDigits];
                  M+=lastDigit;
                  //cout<<M<<endl;
                  if (M>i && M<=B && !buffer.inBuffer(M))
                  {
                     total++;
                  }
                  buffer.add(M);
              }
          }
          out<<"Case #"<<cases<<": "<<total<<endl;          
    }
    system("pause");
    return 0;
}
