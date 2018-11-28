#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("3.out");
    ifstream fin("3.in");
	
      int numCase;
      int n,l,h;
      int note[10000];
      int answer;
      bool possible;
      fin >> numCase;
      for(int i=0; i<numCase; i++) {
	         
	         possible=false;
	         answer=0;
	         fin>>n>>l>>h;
	         
	         for(int k=0; k<n; k++){
			   fin>>note[k];
			 }
	         
	         for(int j=l; j<=h; j++){
	             for(int k=0; k<n; k++){
			          if(note[k]%j==0||j%note[k]==0){;}
			          else{break;}
			          
			          if(k==n-1){possible=true; answer=j;}
			     }	
			     if(possible==true){break;}
			 }
	         
	         
	         
	         
	
	


      fout<<"Case #"<<i+1<<": ";
        if(possible==false){fout<<"NO";}
        else{fout<<answer;}
	  fout<<""<<endl;
  
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
