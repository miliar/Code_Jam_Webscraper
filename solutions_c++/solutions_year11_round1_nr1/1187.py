#include <iostream>
#include <fstream>
#include <vector>


using namespace std; 

long lcf(long a, long b)
{
   if(a==b) return a;
  
   if(a<b) 
   {
      if(b%a == 0) return a;
      else return lcf(a, b%a);
    }
   else 
   {
      if(a%b == 0) return b;
      else return lcf(b, a%b); 
   } 
}

int main(int argc, char* argv[])
{
  std::ifstream input(argv[1]);
  int cases;
  input>> cases;
  for(int iter=1; iter<=cases; iter++)
  {

    long maxD;
    int pD;
    int pG;
    
    input >> maxD;
    input >> pD;
    input >> pG;
     //cout << "maxD =" << maxD << " pD="<<pD<<" pG="<<pG<<endl;
    if((pG>pD && pG == 100) 
      || (pG<pD && pG ==0)) 
    {
       cout<<"Case #"<<iter<<": Broken"<<endl;
       continue;
    }
    if(pG==0 && pD ==0)
   {
       cout<<"Case #"<<iter<<": Possible"<<endl;
       continue;

   }
   
    long D;
    D = 1;
    for ( D=1; D<=maxD; D++)
    { 

       long mul = pD*D;
       long wD = mul/100;
       long rD = mul - wD *100;
 
       if(rD == 0) {
          long n1 = 100*wD - pG*D;
          long n2=100;
          long n3 = pG;
          n1 = n1%pG;
          if(n1<=0) n1 = n1+pG;
          n2 = n2%pG;
          if(n2<=0) n2 = n2+pG;
          //cout << "n1="<< n1 <<" n2=" <<n2<<" n3=" <<n3<<endl;
          long mylcf = lcf(pG, n2);
          if (n1%mylcf == 0) {
             cout<<"Case #"<<iter<<": Possible"<<endl;
             break;
          }
          continue;
          
       }
       
    }
    if(D> maxD)
    	cout<<"Case #"<<iter<<": Broken"<<endl;
 
  }  

}
