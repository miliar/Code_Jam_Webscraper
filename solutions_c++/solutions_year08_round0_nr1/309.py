#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <sstream>

using namespace std;

int main(){
  int N;
  string tmp;
  getline(cin,tmp);
  stringstream ss0(tmp);
  ss0 >> N;
  for(int i=1;i<=N;i++){
    int S;
    getline(cin,tmp);
    stringstream ss(tmp);
    ss >> S;
    vector<string> engines;
    map<string,int> m;
    for(int j=0;j<S;j++){
      string line;
      getline(cin,line);
      engines.push_back(line);
      m[line]=j;
    }
    int Q;  
    vector<string> queries;
    getline(cin,tmp);
    stringstream ss1(tmp);
    ss1 >> Q;
    for(int j=0;j<Q;j++){
      string query;
      getline(cin,query);
      queries.push_back(query);
    }
    bool used[100];
    int left=S;
    int j=0,k;
    int switches=0;
    while(j!=Q){
      fill(used,used+100,false);
      left=S;
      for(;j<Q;j++){
	k=m[queries[j]];
	if(!used[k]){
	  used[k]=true;
	  if(--left==0){
	    switches++;
	    break;
	  }
	}
      }
    }
    cout << "Case #" << i << ": " << switches << "\n";
  }
  

}
