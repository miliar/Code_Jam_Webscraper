#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
  const char filein[] = "C-large.in";
  const char fileout[] = "C-large.out";
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
	  int N;
	  i_file>>N;
	  int *values = new int[N];
	  i_file>>values[0];
	  int min = values[0];
	  int min_pointer = 0;
	  int total = values[0];
	  for(int j=1; j<N; j++) {
	    i_file>>values[j];
	    total = total^values[j];
	    if(min > values[j]) {
	      min = values[j];
	      min_pointer = j;
	    }
	  }
	  if(total != 0)o_file<<"Case #"<<(i+1)<<": NO"<<endl;
	  else {
	    int total_value = 0;
	    for(int j=0; j<N; j++) {
	      if(j != min_pointer)total_value += values[j];
	    }
	    o_file<<"Case #"<<(i+1)<<": "<<total_value<<endl;
	  }
	  delete values;
	}
      i_file.close();
      o_file.close();
    }
  return 0;
}
