#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
  char* x="yhesocvxduiglbkrztnwjpfmaq";
  fstream ip ("A-small-attempt2.in");
fstream op ("output.txt");
  
  
  int t=0;
  string line;
  //getline(ip,line);
  int size=line.length();
   
  int i=0;
  ip>>t;
  //cout<<line;
  /*(while(i<size)
  {
    t=t*10+((int)line[i]);
        
    i++;       
  }*/
  t++;
  //cout<<t;
  int N=t;
  while(t--)
 {
   
	getline (ip,line);
   
   
   for(int i=0;i<line.length();i++)
   { 
     if(i==0)op<<"Case #"<<N-t-1<<": ";
     
     if(line[i]==' ')op<<" "; 
    else
    {
      int m=line[i]-97;
      op<<x[m];
    
    }
 
   }
    op<<"\n";
 }
    ip.close();
 op.close();
  system("pause");
}
