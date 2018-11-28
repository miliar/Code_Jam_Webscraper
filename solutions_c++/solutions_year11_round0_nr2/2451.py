
#include <cstdlib>
#include <iostream>
#include <ctime>
#include <queue>
#include <cstdio>
#include <cstdarg>
#include <fstream>
#include <map>
#include <cstring>
#include <set>
#include <list>

using namespace std;

int main(int argc, char** argv){
  ifstream cin("in.txt");
  ofstream cout("out.txt");

  int nCase;

  cin >> nCase;
  for(int i = 0; i < nCase; i++){

    list<char> el_list;

    typedef pair<char,char> ch_ch;

    map<char,int> op_in_el_list;
    set<char> op_chars;
    set<ch_ch> op_pairs;
    map<ch_ch,char> combine;

    int nC, nO;
    string str;

    cin >> nC;
    for(int j = 0; j < nC; j++){
      cin >> str;
      combine[ch_ch(str[0],str[1])] = str[2];
      combine[ch_ch(str[1],str[0])] = str[2];
    }

    cin >> nO;
    for(int j = 0; j < nO; j++){
      cin >> str;
      op_chars.insert(str[0]);
      op_chars.insert(str[1]);
      op_pairs.insert(ch_ch(str[0],str[1]));
      op_pairs.insert(ch_ch(str[1],str[0]));
    }

    int govno;
    cin >> govno >> str;
    for(int j = 0; j < str.length(); j++){
      if(!el_list.empty()){
        map<ch_ch,char>::iterator iC;
        // if combine !!!
        char back = el_list.back();
        if((iC = combine.find(ch_ch(back,str[j]))) != combine.end()){
          // must decrement 'op_in_el_list'
          if(op_in_el_list.find(back) != op_in_el_list.end()){
            if(op_in_el_list[back] == 1) op_in_el_list.erase(back);
            else op_in_el_list[back]--;
          }
          el_list.pop_back();
          el_list.push_back(iC->second);
          continue;
        }
      }
      // may be oposite ???
      if(op_chars.find(str[j]) != op_chars.end()){
        bool clear = 0;
        for(map<char,int>::iterator it = op_in_el_list.begin(); it != op_in_el_list.end(); it++){
          // if pair is finded clear list !!!
          if(op_pairs.find(ch_ch(str[j],it->first)) != op_pairs.end()){
            el_list.clear();
            op_in_el_list.clear();
            clear = 1;
            break;
          }
        }
        if(clear) continue;

        if(op_in_el_list.find(str[j]) != op_in_el_list.end()) op_in_el_list[str[j]]++;
        else op_in_el_list[str[j]] = 1;
      }
      
      el_list.push_back(str[j]);
    }


    cout << "Case #" << i+1 << ": [";

    for(list<char>::iterator it = el_list.begin(); it != el_list.end();){
      cout << *it;
      it++;
      cout << (it != el_list.end() ? ", " : "");
    }

    cout << "]\n";
  }

  return 0;
}

