#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main(){
  const char filein[] = "B-small.in";
  const char fileout[] = "B-small.out";
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
	  int C;
	  i_file>>C;
	  char **combination = new char*[3];
	  for(int j=0; j<C; j++) {
	    combination[j] = new char[3];
	    i_file>>combination[j][0];
	    i_file>>combination[j][1];
	    i_file>>combination[j][2];
	  }
	  int D;
	  i_file>>D;
	  char ** opposed = new char*[2];
	  for(int j=0; j<D; j++) {
	    opposed[j] = new char[2];
	    i_file>>opposed[j][0];
	    i_file>>opposed[j][1];
	  }
	  int N;
	  i_file>>N;
	  vector<char> result;
	  for(int j=0; j<N; j++) {
	    char current;
	    i_file>>current;
	    if(result.size() > 0) {
	      bool flag = false;
	      for(int k=0; k<C; k++) {
		if(result.back() == combination[k][0] && current == combination[k][1]
		   || result.back() == combination[k][1] && current == combination[k][0]) {
		  result.pop_back();
		  result.push_back(combination[k][2]);
		  flag = true;
		  break;
		}
	      }
	      if(!flag) {
		vector<char>::iterator it;
		for(int k=0; k<D; k++) {
		  if(current == opposed[k][0]) {
		    for(it=result.begin(); it<result.end(); it++) {
		      if(*it == opposed[k][1]) {
			result.clear();
			flag = true;
			break;
		      }
		    }
		  }
		  else if(current == opposed[k][1]) {
		    for(it=result.begin(); it<result.end(); it++) {
		      if(*it == opposed[k][0]) {
			result.clear();
			flag = true;
			break;
		      }
		    }
		  }
		}
	      }
	      if(!flag) result.push_back(current);
	    }
	    else result.push_back(current);
	  }
	  o_file<<"Case #"<<(i+1)<<": [";
	  vector<char>::iterator it;
	  if(result.size() == 0)o_file<<"]"<<endl;
	  else {
	    for(it=result.begin(); it<result.end()-1; it++) {
	      o_file<<*it<<", ";
	    }
	    o_file<<*it<<"]"<<endl;
	  }
	  for(int j=0; j<C; j++) {
	    delete combination[j];
	  }
	  delete combination;
	  for(int j=0; j<D; j++) {
	    delete opposed[j];
	  }
	  delete opposed;
	}
      i_file.close();
      o_file.close();
    }
  return 0;
}
