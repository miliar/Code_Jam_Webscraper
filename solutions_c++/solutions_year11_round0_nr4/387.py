#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("4.out");
    ifstream fin("4.in");
	
      int numCase;
      fin >> numCase;
      int numIntegar; 
      int nowNumber; 
      int expectedTime; 
      
      
      for(int i=0; i<numCase; i++) {
             fin>> numIntegar;
             expectedTime=0; 
	         for(int j=0;j<numIntegar;j++){
                 fin>>nowNumber; 
                 if(nowNumber!=j+1){expectedTime++;}                         
             } 

      fout<<"Case #"<<i+1<<": ";
      fout<<fixed<<setprecision(6)<<float(expectedTime)<<endl; 
  
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
