#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
void exec();

int main()
{
    exec();
    return 0;
}

void exec()
{
      ifstream file("A-large.in");
      int T=0,N=0,Pi=0,posO=1,posB=1,tO=0,tB=0,dernier=-1;
      char Ri;
      file>>T;
      for(int i=1;i<=T;i++)
      {
            file>>N;
            dernier=-1;
            posO=1;
            posB=1;
            tO=0;
            tB=0;
            for(int j=0;j<N;j++)
            {
                  file>>Ri;
                  file>>Pi;
                  if(Ri=='O')
                  {

                        tO=tO+abs((double)Pi-(double)posO)+1;
                        posO=Pi;
                        if(dernier==1&& tO<=tB)
                        {
                              tO=tB+1;
                        }
                         dernier=0;

                  }
                  else
                  {
                        tB=tB+abs((double)Pi-(double)posB)+1;
                        posB=Pi;
                        if(dernier==0 && tB<=tO)
                        tB=tO+1;
                        dernier=1;

                  }

            }
            if(tB<tO)
            cout<<"Case #"<<i<<": "<<tO<<endl;
            else
            cout<<"Case #"<<i<<": "<<tB<<endl;

      }
      file.close();
}
