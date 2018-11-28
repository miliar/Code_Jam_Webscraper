#include <iostream>
#include <fstream>
#include <memory>
using namespace std;

int main()
{
       fstream fin("A-large.in");
       ofstream fout("A-large-out.out");
       int cas,cnt,N,K,t;
       fin>>cas;
       for(cnt=1;cnt<=cas;cnt++)
       {
            fin>>N>>K;
            t=(1<<N);
            if((K+1)%t==0)
              fout<<"Case #"<<cnt<<":"<<" "<<"ON"<<endl;
            else
              fout<<"Case #"<<cnt<<":"<<" "<<"OFF"<<endl;
       }

}
