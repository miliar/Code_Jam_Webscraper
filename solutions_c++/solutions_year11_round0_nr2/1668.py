#include <iostream>
#include <string>
#include <algorithm>
const int C_MAX = 36;
const int D_MAX = 28;
const int N_MAX = 100;
int C, D, N, last;
std::string combined[C_MAX], opposed[D_MAX], invoked, elements_list;


bool check_combine(char e) {

  if ( last < 0 ) {
    last++;
    elements_list.push_back(e);
    return true;
  }

  for(int i = 0; i < C; i++) {
    if ( combined[i][0] == e && combined[i][1] == elements_list[last]  ) {
      elements_list.replace(last, 1, 1, combined[i][2]);
      return true;
    }
    else if ( combined[i][0] == elements_list[last] && combined[i][1] == e ) {
      elements_list.replace(last, 1, 1,  combined[i][2]);
      return true;
    }
  }
  
    return false;
}


void check_opposed(char e) {

  size_t found;
  for(int i = 0; i < D; i++) {
    if ( e == opposed[i][0] ) {
      found = elements_list.find(opposed[i][1], 0);
      if ( found != std::string::npos) {
	elements_list.clear();
	last = -1;
	return;
      }
    }
    else if ( e == opposed[i][1] ) {
      found = elements_list.find(opposed[i][0], 0);
      if ( found != std::string::npos) {
	elements_list.clear();
	last = -1;
	return;
      }
    }
  }

  last++;
  elements_list.push_back(e);

}

int main() {

  int T;
  std::cin>>T;
  for(int count = 1; count <= T; count++) {
    
    for(int i = 0; i < C_MAX; i++) {
      combined[i].clear();
    }
    for(int i = 0; i < D_MAX; i++) {
      opposed[i].clear();
    }
    invoked.clear();
    elements_list.clear();


    std::cin>>C;
    for(int i = 0; i < C; i++) 
      std::cin>>combined[i];

    std::cin>>D;
    for(int i = 0; i < D; i++) 
      std::cin >>opposed[i];

    std::cin>>N>>invoked;


    elements_list.push_back(invoked[0]); last = 0;
    for(int i = 1; i < N; i++) {
      if ( check_combine(invoked[i]) == false ) check_opposed(invoked[i]);
    }
    
    std::cout<<"Case #"<<count<<": "<<"[";
    for(int i = 0; i < (int)elements_list.length(); i++) {
      if ( i != 0 ) std::cout<<", ";
      std::cout<<elements_list.at(i);
    }
    std::cout<<"]"<<std::endl;
  }

  return 0;
}
