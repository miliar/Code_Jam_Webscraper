#include<iostream>
#include<map>
#include<string>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<sstream>

using namespace std;

int N,S,Q;

int readInt(){
  string s;
  getline(cin,s);
  return atoi(s.c_str());
}

int seen[500];

void flip_rest(int id,int engines_count){
   for(int i=1;i<=engines_count;i++){
      if(i!=id) seen[i]=0;
   }
}

int mark_visited(int id){
  if(seen[id]) return 0;
  return seen[id]=1;
}

int main(){
  string s;
  N=readInt();
  int kase=1;
  while(N--){
    memset(seen,0,sizeof(seen));
    S=readInt();
    map<string,int> word_map;
    int cnt=1;
    for(int i=0;i<S;i++){
    	string s;
	getline(cin,s);
        if(word_map.count(s)==0){
	  word_map[s]=cnt++;
	}
    }
    int search_engines=word_map.size();
    Q=readInt();
    int flip_count=0;
    cnt=0;
    for(int i=0;i<Q;i++){
    	string s;
	getline(cin,s);
	if(word_map.count(s)==0) continue;
	int id=word_map[s];
	cnt+=mark_visited(id);
	if(cnt==search_engines){
	  flip_count++;
	  flip_rest(id,search_engines);
	  cnt=1;
	}
    }
    cout<<"Case #"<<kase++<<": "<<flip_count<<endl;
  }
}
