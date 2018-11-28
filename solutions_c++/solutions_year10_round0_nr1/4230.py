#include <fstream>
using namespace std;

int main()
{
    ifstream file1;
    ofstream file2;
    file1.open("A-small-attempt0.in");
    file2.open("A-small.out");
    int T,N,K;
    file1>>T;
    int br=0;
    int step=1;
    while(T>0)
    {
              file1>>N>>K;
              int *b=0;
              b = new int [N];
              for(int i=0; i<N; i++)
                      b[i] = 0;
              while(K>0)
              {
                      for(int i=0; i<N; i++)
                      {
                              if(b[i]==0) 
                              {
                                          b[i]=1;
                                          break;
                              }
                              else b[i]=0;
                      }  
                      K--;
              }
              bool state=true;
              for(int i=0; i<N; i++)
                      if (b[i]==0) state=false;
              if(state==true) file2<<"Case #"<<step<<": ON"<<endl; 
              else file2<<"Case #"<<step<<": OFF"<<endl;    
              step++;       
              T--;
    }
    file1.close();
    file2.close();
    system("PAUSE");
    return 0;
}
