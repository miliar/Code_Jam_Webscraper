#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream file1;
    ofstream file2;
    file1.open("C-small-attempt0.in");
    file2.open("C-small.out");
    int T;
    file1>>T;
    long long *b = 0;
    b = new long long [T];
    long long step=0;
    long long ts=T;
    while(T>0)
    {
        long long R,N,k;  
        file1>>R>>k>>N;             
        long long *a=0;
        a = new long long [N];
        for(int i=0; i<N; i++)
                file1>>a[i];
        int start=0;
        long long br=0;
        for(int i=0; i<R; i++)
        {
              long long brCt=0;
              bool nFact=false, cont=true;  
              int startOld=start;
              for(int j=startOld; j<N; j++ )
              {
                      if((brCt+a[j])<=k&&cont==true)
                      {
                                    br+=a[j];
                                    brCt+=a[j];
                                    start=j+1;
                                    if(j==(N-1)) nFact=true;
                      }
                      else cont=false;
              }  
              if(nFact==true)
              {
                  for(int j=0; j<startOld; j++ )
                  {
                      if((brCt+a[j])<=k&&cont==true)
                      {
                                    br+=a[j];
                                    brCt+=a[j];
                                    start=j+1;
                      }
                      else cont=false;
                  }                 
              }
              if(start>=N) start=0;
        }
        T--;
        b[step]=br;
        step++;        
    }
    for(int i=0; i<ts; i++)
            file2<<"Case #"<<i+1<<": "<<b[i]<<endl;
    file1.close();   
    file2.close();    
    system("PAUSE");
    return 0;
}
