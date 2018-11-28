#include<string>
#include<iostream>
#include<map>
#include<vector>
using namespace std;

map<pair<char,char>,char> combines;
map<pair<char,char>,bool> opposes;
vector<char> sequence;

int T, C, D, N;

void combine(char c1, char c2, char c3){
  combines[make_pair(c1,c2)] = c3;
  combines[make_pair(c2,c1)] = c3;
}
void oppose(char c1, char c2){
  // cout << " setting oppose " << c1 << " " << c2 << " to true" << endl;
  opposes[make_pair(c1,c2)] = true;
  opposes[make_pair(c2,c1)] = true;
}
bool canCombine(char c1, char c2){
  return combines.find( make_pair(c1,c2) ) != combines.end();
}
char getCombination(char c1, char c2){
  return combines.find( make_pair(c1,c2) )->second;
}
bool doesOppose(char c1, char c2){
  //cout << "opposes " << c1 << " " << c2 << " = " << (opposes.find(make_pair(c1,c2)) != opposes.end()) << endl;
  return opposes.find(make_pair(c1,c2)) != opposes.end();
}

int main(){
  cin >> T;
  for(int round=1;round<=T;round++){
    combines.clear();
    opposes.clear();
    sequence.clear();
    cin >> C;
    for(int c=0; c<C;c++){
      char c1, c2, c3;
      cin >> c1 >> c2 >> c3;
      combine(c1,c2,c3);
    }
    cin >> D;
    for(int d=0; d<D; d++){
      char c1, c2;
      cin >> c1 >> c2;
      oppose(c1,c2);
    }
    cin >> N;
    for(int n=0;n<N;n++){
      char c1, last;
      cin >> c1;
      bool combine = false;
      bool oppose = false;
      if( sequence.size() >= 1 ){
	last = sequence.back();
	if(canCombine(c1,last)){
	  combine = true;
	  sequence.pop_back();
	  sequence.push_back(getCombination(c1,last));
	}
      }
      if(!combine){
	for(unsigned int ch=0;ch<sequence.size();ch++){
	  if( doesOppose(sequence[ch], c1) ){
	    oppose = true;
	  }
	}
      }
      if(oppose){
	sequence.clear();
      } else if(!combine){
	sequence.push_back(c1);
      }
    }
    cout << "Case #" << round << ": [";
    if( !sequence.empty() ){
      cout << sequence.at(0);
      for(unsigned int ch=1; ch<sequence.size();ch++){
	cout << ", " << sequence.at(ch);
      }
    }
    cout << "]" << endl;
  }
}
