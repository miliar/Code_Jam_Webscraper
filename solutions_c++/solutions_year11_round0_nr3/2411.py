#include <iostream>
#include <fstream>


using namespace std;
void exec();
int main()
{
    exec();
    return 0;
}

void exec()
{
      ifstream file("C-large.in");
      int T,N,small=1000001,sumP=0,sumS=0,part;
      file>>T;
      for(int i=1;i<=T;i++)
      {
            file>>N;
            small=1000001;
            sumP=0;
            sumS=0;
            for(int j=0;j<N;j++)
            {
                  file>>part;
                  sumP^=part;
                  sumS+=part;
                  if(part<small)
                  small=part;
               
            }
            if(sumP!=0)
            cout<<"Case #"<<i<<": "<<"NO"<<endl;
            else
            cout<<"Case #"<<i<<": "<<sumS-small<<endl;

      }

      file.close();

}

