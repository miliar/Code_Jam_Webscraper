#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
      int t;
      //char A[100];
      string A;
      char B[]="yhesocvxduiglbkrztnwjpfmaq";
      ifstream inp("1.txt");
      ofstream oup;
      oup.open("b.out");
      inp>>t;
      getline(inp,A);
      for(int i=0;i<t;++i)
      {
              getline(inp,A);
              oup<<"Case #"<<i+1<<": ";
              for(int j=0;A[j]!='\0';++j)
              {
                      if(A[j]==' ')
                          oup<<' ';
                      else
                          oup<<B[A[j]-'a'];
              }
              oup<<"\n";
      }
      oup.close();
      inp.close();
      return 0;
}
