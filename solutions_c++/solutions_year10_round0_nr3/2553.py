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
    int step=1;
    while(T>0)
    {
        int N;
        unsigned long R,k;  
        file1>>R>>k>>N;             
        unsigned long *a=0;
        a = new unsigned long [N];
        for(int i=0; i<N; i++)
                file1>>a[i];
        int start=0;
        unsigned long long br=0;
        for(int i=0; i<R; i++)
        {
              unsigned long long brCt=0;
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
        file2<<"Case #"<<step<<": "<<br<<endl;
        T--;
        step++;        
    }
    file1.close();   
    file2.close();    
    system("PAUSE");
    return 0;
}
