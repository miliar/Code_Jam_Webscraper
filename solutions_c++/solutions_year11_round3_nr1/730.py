#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

int main(int argc, char *argv[])
{
	ofstream fout("1.out");
    ifstream fin("1.in");
	
      int numCase;
      int r,c;
      bool possible;
      char a[50][50];
      char nowchar;
      fin >> numCase;
      for(int i=0; i<numCase; i++) {
			
			possible=true;
			
			for(int j=0; j<50; j++){
			    for(int k=0; k<50; k++){
				     a[j][k]='a';
				}	
			}



			
			fin>>r>>c;
			for(int j=0; j<r; j++){
			    for(int k=0; k<c; k++){
					 fin>>a[j][k];
				}	
			}
			
			for(int j=0; j<r; j++){
			    for(int k=0; k<c; k++){
				     cout<<a[j][k];
				}
				cout<<endl;	
			}
			
			
	         
	        for(int j=0; j<r; j++){
			    for(int k=0; k<c; k++){
				     if(a[j][k]=='#'){
					      if(a[j][k+1]=='#'&&a[j+1][k]=='#'&&a[j+1][k+1]=='#'){
						        a[j][k]=47;
								a[j][k+1]=92;
						        a[j+1][k]=92;
						        a[j+1][k+1]=47;
						  }
						  else{possible=false;}
					 
					 
					 }
				}	
			}
	
	
      

      fout<<"Case #"<<i+1<<": "<<endl;
      if(possible==false){fout<<"Impossible"<<endl;}
      else{
	     	for(int j=0; j<r; j++){
			    for(int k=0; k<c; k++){
				     fout<<a[j][k];
				}
				fout<<endl;	
			}
	  }
      
      
      }
	
	
	

	
    system("PAUSE");
    return EXIT_SUCCESS;
}
