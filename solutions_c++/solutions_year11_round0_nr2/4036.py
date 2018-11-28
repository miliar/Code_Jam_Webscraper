#include<iostream>
#include<algorithm>
#include<list>
#include<map>

using namespace std;

  void input_comb(map< pair<char,char>, char > &combine);
  void input_opp(map<char, char> &opposite);
  int input_and_action(list<char> &elem_list, map< pair<char,char>, char > &combine, map<char, char> &opposite, char elem);
  void output(list<char> &elem_list, int k);

int main(int argc, char* argv[]){
  list<char> elem_list;
  map< pair<char,char>, char >combine;
  map<char, char> opposite;
  int c, d, n;
  int t,t2;
  char elem;
  
  cin>>t;
  t2=t;
  while(t--){
    cin>>c;
    while(c--)
      input_comb(combine);
    cin>>d;
    while(d--)
      input_opp(opposite);
    cin>>n;
    cin>>elem;
    ////cerr<<elem<<endl;
    elem_list.push_back(elem);
    //cerr<<elem<<endl;
    n--;
    while(n--){
      cin>>elem;
      input_and_action(elem_list, combine, opposite, elem);
    }
    output(elem_list, t2-t);
    combine.clear();
    opposite.clear();
    elem_list.clear();
    if(t != 0)
      cout<<endl;
    
  }
    
    return 0;
}
  
  
  void input_comb(map< pair<char,char>, char > &combine){
    char base1, base2, nonbase, space;
    cin>>base1>>base2>>nonbase;
    
    
    
    combine.insert( pair<pair<char,char>, char>(pair<char, char>(base1,base2),nonbase));
    combine.insert( pair<pair<char,char>, char>(pair<char, char>(base2,base1),nonbase));    
    //cin>>space;
    //cerr<<base1<<base2<<nonbase<<endl;
  }
  
  void input_opp(map<char, char> &opposite){
    char base1,base2,space;
    cin>>base1>>base2;
    
    
    
    opposite.insert(pair<char,char>(base1,base2));
    opposite.insert(pair<char,char>(base2,base1));
    //cin>>space;
    
    //cerr<<base1<<base2<<endl;
    
  }
  
  int input_and_action(list<char> &elem_list, map< pair<char,char>, char > &combine, map<char, char> &opposite, char elem){
   
    //cerr<<elem<<endl;
    
    if (elem_list.empty()){
      elem_list.push_back(elem);
      return 0;
    }
      
    
    map< pair<char,char>, char >::iterator comb_it;
    map<char, char>::iterator opp_it;
    list<char>::iterator list_it = elem_list.end();
    
    comb_it = combine.find(pair<char,char>(*(--list_it), elem));
    if (comb_it != combine.end()){
      elem_list.pop_back();
      elem_list.push_back(comb_it->second);
      //cerr<<"  "<<comb_it->second<<endl;
      return 0;
    }    
    
    bool flag = false;
    opp_it = opposite.find(elem);
    if (opp_it != opposite.end()){
      for(list_it = elem_list.begin(); list_it != elem_list.end(); list_it++){
	if(*list_it == opp_it->second){
	  //cerr<<" "<<opp_it->second<<endl;
	  elem_list.clear();
	  flag = true;
	}
	if(flag == true)
	  break;
      }
      if(!elem_list.empty()){
	//cerr<<elem<<endl;
	elem_list.push_back(elem);
      }
     // //cerr<<elem;
      return 0;
    }
    
    elem_list.push_back(elem);
    //find(pair<char,char>(*(--it),elem));
  }
  
  void output(list<char> &elem_list, int k){
    cout<<"Case #"<<k<<": [";
    if(!elem_list.empty()){
    cout<<*(elem_list.begin());
    list<char>::iterator it = elem_list.begin();
    for(++it ; it != elem_list.end(); it++)
      cout<<", "<<*it;
    }
    cout<<"]";
  }
  