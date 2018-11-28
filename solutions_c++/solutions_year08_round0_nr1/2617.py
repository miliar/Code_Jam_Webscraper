//qualA.cpp
//Solution for problem A, 'Saving the Universe'
//cl qualA.cpp /FequalA.exe /EHsc
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct Case{
  Case(int n): switches(0), engines(0), queries(0), id(n) {}
  ~Case(){
    delete[] engines;
    delete[] queries;
  }
  friend ostream& operator<<(ostream& o, Case& c);
  int id;
  int switches;
  string* engines;
  string* queries;
};
ostream& operator<<(ostream& o, Case* c){
  o << "Case #" << c->id << ": " << c->switches;
  return o;
}

int main(int argc, char* argv[]){
  if(argc != 2)
    return 1;
  ifstream fin(argv[1]);
  if(!fin)
    return 1;
  int ncases;
  fin >> ncases;
  Case* c;
  for(int i=0; i < ncases; ++i){
    c = new Case(i+1);
    int nengines, nqueries;
    fin >> nengines;
    fin.ignore(2,'\n');
    c->engines = new string[nengines];
    char line[100];
    for(int j=0; j < nengines; ++j){
      fin.getline(line, 100);
      c->engines[j] = line;
    }
    fin >> nqueries;
    fin.ignore(2,'\n');
    c->queries = new string[nqueries];
    for(int j=0; j < nqueries; ++j){
      fin.getline(line, 100);
      c->queries[j] = line;
    }
    char* seen = new char[nengines]; //keep track of already seen engines
    int j = 0;
    while(1){
      memset(seen, 0, nengines);// I hain't seen nuthing gov
      int count = 0;
      for(; j < nqueries; ++j){ //run through queries until all engines has been seen
	for(int k=0; k < nengines; ++k){
	  if(c->engines[k] == c->queries[j]){
	    if(seen[k])
	      break;
	    seen[k] = 1;
	    count++;
	    break;
	  }
	}
	if(count == nengines)
	  break;
      }
      if(count == nengines)
	c->switches++;
      else
	break;
    }
    cout << c << endl;
    delete c;
  }
  return 0;
}
