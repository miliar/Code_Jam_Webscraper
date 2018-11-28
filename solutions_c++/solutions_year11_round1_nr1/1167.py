
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
  const char filein[] = "A-large.in";
  const char fileout[] = "A-large.out";
  ifstream i_file;
  ofstream o_file;
  int num_case = 0;

  i_file.open(filein);
  o_file.open(fileout);
  if(i_file.is_open())
    {
      i_file>>num_case;
      for(int i=0; i<num_case; i++)
	{
	  string str;
	  int N=100, PD, PG;
	  i_file>>str;
	  if(str.length()<4) {
	    N = atoi(str.c_str());
	  }
	  i_file>>PD;
	  i_file>>PG;
	  bool flag = true;
	  if(N<100) {
	    for(int j=0; j<N; j++) {
	      for(int k=0; k<=(j+1); k++) {
		if((float)k*100/(j+1) == PD) {
		  flag = false;
		  break;
		}
	      }
	    }
	    if(flag)o_file<<"Case #"<<(i+1)<<": Broken"<<endl;
	  }
	  if(!flag || N >=100) {
	    if(PG==100 && PD<100 || PG==0 && PD>0) {
	      o_file<<"Case #"<<(i+1)<<": Broken"<<endl;
	    }
	    else {
	      o_file<<"Case #"<<(i+1)<<": Possible"<<endl;
	    }
	  }
	}
    }
    i_file.close();
    o_file.close();
  return 0;
}
