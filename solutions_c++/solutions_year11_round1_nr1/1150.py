#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("1.out");
    ifstream fin("1.in");
	
	  int pd, pg; 
	  long long int n;
	  bool possible;
	
      int numCase;
      fin >> numCase;
      
//      cout<<"numCase="<<numCase<<endl;
      for(int i=0; i<numCase; i++) {
	         fin>> n>>pd>>pg;
	         possible=false;
//	  cout<<"fin>> n>>pd>>pg;"<<endl;       
	         for(int j=0; j<n; j++){
			      if((pd*(j+1))%100==0){possible=true; break;}		
			 }
	         
//	  cout<<"if((pd*(j+1))%100==0)"<<endl;
	         if(pg==0&&pd!=0){possible=false;}
	         if(pg==100&&pd!=100){possible=false;}

      fout<<"Case #"<<i+1<<": ";
        if(possible){fout<<"Possible";}
        else{fout<<"Broken";}
	  fout<<""<<endl;
  
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
