#include<iostream>
using namespace std;


class candy
{
      private:
      int T,N,i,j,k, pos;
      long int C[1001], sum, xor_sum; 
      
      public:
      void control();
      void smallest();
};


void candy :: control()
{
     cin>>T;
     for(i=1;i<=T;++i)
     {
                      cin>>N;
                      for(j=0;j<N;++j)
                      cin>>C[j];
                      
                      smallest();
                      
                      xor_sum = C[pos];
                      sum = 0;
                      
                      for(j=0;j<N;++j)
                      {
                         if(j!=pos)
                         {
                            xor_sum = xor_sum ^ C[j];
                            sum += C[j];
                         }
                      }
                      
                      if(xor_sum!=0)
    	              { 
                    	  cout<<"Case #"<<i<<": NO\n";
       	              }
                  	  else 
 	                  {
                           cout<<"Case #"<<i<<": "<<sum<<"\n";
                      }
     }
}


void candy :: smallest()
{
     pos=0;
     
     for(k=0;k<N;++k)
     {
                     if(C[k]<C[pos])
                                    {
                                         pos = k;
                                    }
     }
}

int main()
{
    candy obj;
    obj.control();
    return 0;
}

