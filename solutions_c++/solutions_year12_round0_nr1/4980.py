# include <iostream>
#include <fstream>
#include <string>

using namespace std;


void kiir(string vegso){
	ofstream mfile ("taner.txt");
  if (mfile.is_open())
  {
  }
  else cout << "Unable to open file";
 
}
string feldolgoz(string line1, string abc){
	int i;
	string ered="";
	int index;
	int n=line1.length();
	for (i=0; i<n; i++){

		index=line1[i]-97;
		if (index<0){
			ered=ered+' ';
		}
		else{
		ered=ered+abc[index];
		}
	}
	  return ered;   
}
void main()
{ 
  ofstream mfile ("taner.txt");
  if (mfile.is_open())
  {
  string abc="yhesocvxduiglbkrztnwjpfmaq";
  string line1; 
  ifstream myfile ("form1.txt");
    if (myfile.is_open())
    {
	  if ( myfile.good() ){
		getline (myfile,line1);
		int i=0;
        while ( myfile.good() )
        {
		  i++;
		  mfile<<"Case #"<<i<<": ";
          getline (myfile,line1);
	      
		  string vegso=feldolgoz(line1,abc);
		  mfile<<vegso<<'\n';
        }
	  }
	 myfile.close();
 
	}	
  else cout << "Unable to open file"; 
  }
  else cout << "Unable to open file";
}