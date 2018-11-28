#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>

using namespace std;


int process(vector<pair<char, int> >& vec, vector<int>& orange, vector<int>& blue)
{
  int res = 0;
  int pos_o = 0;
  int pos_b = 0;
  int idx_o = 0;
  int idx_b = 0;
  
  for(int i = 0; i < vec.size(); i++){
    if (vec[i].first == 'O'){ // ORANGE Turn
      int dur = abs(orange[idx_o] - pos_o) + 1;
      // fprintf(stderr, "dur = %d\n", dur);

      pos_o = orange[idx_o];

      res += dur;
      fprintf(stderr, "%d %d, res = %d\n", pos_o, pos_b, res);
      idx_o++;

      if (blue.size() == 0) continue;
      
      if (blue[idx_b] >= pos_b){
        pos_b = min(blue[idx_b], pos_b + dur);
      }
      else{
        pos_b = max(blue[idx_b], pos_b - dur);
      }

    }else{ // BLUE Turn
      int dur = abs(blue[idx_b] - pos_b) + 1;
      // fprintf(stderr, "dur = %d\n", dur);

      pos_b = blue[idx_b];


      res += dur;
      fprintf(stderr, "%d %d, res = %d\n", pos_o, pos_b, res);
      idx_b++;

      if (orange.size() == 0) continue;
      
      if (orange[idx_o] >= pos_o){
        pos_o = min(orange[idx_o], pos_o + dur);
      }
      else{
        pos_o = max(orange[idx_o], pos_o - dur);
      }

    }
  }
  return res;
}



int main(int argc, char *argv[]){
  int t;
  
  // “ü—Í•”
  ifstream ifs(argv[1]);
  string line;
  
  int num_line = 0;
  while( getline(ifs,line) ) {
    vector<pair<char, int> > vec;
    vector<int> orange;
    vector<int> blue;
    
    if ( line.size() == 0 ) break;

    stringstream ss(line);
    if (num_line == 0) {
      ss >> t;
      fprintf(stderr, "T = %d\n", t);
    }
    else {
      int n;
      ss >> n;

      for (int i = 0; i < n; i++){
        char ch;
        int k;
        ss >> ch >> k;
        vec.push_back(make_pair(ch, k - 1));
        if ( ch == 'O'){
          orange.push_back(k - 1);
        }
        else{
          blue.push_back(k - 1);
        }
      }

      
      
      for(int i = 0; i < n; i++){
        fprintf(stderr, "%c%d ", vec[i].first, vec[i].second);
      }
      fprintf(stderr, "\n");
#if 0
      fprintf(stderr, "ORANGE: ");
      for(int i = 0; i < orange.size(); i++){
        fprintf(stderr, "%d ", orange[i]);
      }
      fprintf(stderr, "\n");

      fprintf(stderr, "BLUE: ");
      for(int i = 0; i < blue.size(); i++){
        fprintf(stderr, "%d ", blue[i]);
      }
      fprintf(stderr, "\n");
#endif
      // “ü—ÍI—¹
      fprintf(stderr, "process...\n");
      int res = process(vec, orange, blue);
      printf("Case #%d: %d\r\n", num_line, res);
    }
    
    num_line++;
  }
  fprintf(stderr, "done.\n");


  
  return 0;
  
}