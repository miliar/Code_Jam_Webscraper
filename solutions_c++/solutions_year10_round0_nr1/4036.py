# include <iostream>
# include <cmath>
using namespace std;
int main()
{
    int N;
    long long K;
    int T,I=1;
    cin>>T;
    while (I<=T)
    {
          cin>>N>>K;
          
          long long  L=pow(2,(double)N);
          
          K=K%L;
          
          L--; 
          
    
          
          if (K!=L)
          cout<<"Case #"<<I++<<": "<<"OFF"<<endl;
          else      cout<<"Case #"<<I++<<": "<<"ON"<<endl;
    }
    
    
}
