#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <set>
#include <list>
#include <string>

using namespace std;

int main(int argc, const char** argv)
{
  int n;//number of cases
  int s;//number of search engines
  int q;//number of queries
  ifstream is;
  is.open("small.in");
  vector<string> engines;
  vector<string> queries;
  vector<string> result;//containes the search engines in the proper order
  set<string> temp;//temporary found engines
  string en;//engine to use
  string stmp;
  int snum;
  ofstream os;
  os.open("small.out");
  if(os.fail()){
    cout << "output open failed!";
    return -2;
  }
  if(is.fail()){
    cout << "input open failed!";
    return -1;
  }

  //is >> n;
  getline(is,stmp);
  n = atoi(stmp.c_str());
  for(int i = 0; i < n; ++i){
    //fill engines names
    //is >> s;
    getline(is,stmp);
    s = atoi(stmp.c_str());
    //cout << "s: " << s<< endl;
    engines.clear();
    for(int j = 0; j < s; ++j){
      stmp.clear();
      //is >> stmp;
      getline(is,stmp);
      //cout << stmp << " one" << endl;
      engines.push_back(stmp);
    }
    //fill quieries
    //is >> q;
    getline(is,stmp);
    q = atoi(stmp.c_str());
    //cout << "q: " << q<< endl;
    queries.clear();
    for(int j = 0; j < q; ++j){
      stmp.clear();
     // is >> stmp;
      getline(is,stmp);
      queries.push_back(stmp);
    }

    //start search
    //en.clear();
    result.clear();
    temp.clear();
    //cout << "Start..";
    snum = 0;
    for(int j = 0; j < q; ++j){
      temp.insert(queries[j]);
      //cout<<"ifelott: "<<queries[j]<<endl;
      if(temp.size() == s){
	//cout<<"ifben"<<endl;
        //result.push_back(queries[j]);
	++snum;
	temp.clear();
	temp.insert(queries[j]);
      }
    }
    //cout<<"end"<<endl;

    //if(result.size() == 0){
    //  for(int k = 0; k < s; ++k){
    //    if(temp.insert(engines[k]).second == true){
    //    result.push_back(engines[k]);
    //    break;
    //    }
    //  }
    //}
    //check result
    //if(result.size() == 0){
    //  cout << "Hiba! 0 a megoldas merete!"<<endl;
    //  continue;
    //}

    //write result
    os << "Case #" << (i+1) << ": " << /*(result.size() - 1)*/snum << endl;
  }

  return 0;
}
