#include<cstdio>
#include<iostream>
#include<list>
#include<map>
#include<string>
#include<set>

using namespace std;

void combine(list<char>& ans, map<char,int>& obase,map<char,set<char> >& c_table, map<pair<char,char>,char>& cm_table);
bool opposed(list<char>& ans, map<char,int>& obase,map<char,set<char> >& d_table);
int main(){
  int T;
  cin >> T;
  for(int test=1;test<=T;test++){
    int C,D,N;
    map<char,set<char> > c_table;
    map<pair<char,char>,char> cm_table;
    map<char,set<char> > d_table;
    cin >> C;
    for(int i=0;i<C;i++){
      string tmp;
      cin >> tmp;
      c_table[tmp[0]].insert(tmp[1]);
      c_table[tmp[1]].insert(tmp[0]);
      cm_table[make_pair(min(tmp[0],tmp[1]),max(tmp[0],tmp[1]))]=tmp[2];
    }
    cin >> D;
    for(int i=0;i<D;i++){
      string tmp;
      cin >> tmp;
      d_table[tmp[0]].insert(tmp[1]);
      d_table[tmp[1]].insert(tmp[0]);
    }
    cin >> N;
    string ivk;
    cin >> ivk;

    map<char,int> obase;
    list<char> ans;
    for(int i=0;i<N;i++){
      ans.push_back(ivk[i]);
      obase[ivk[i]]++;
      combine(ans,obase,c_table,cm_table);
      opposed(ans,obase,d_table);
    }

    cout << "Case #" << test <<": [";
    for(list<char>::iterator itr=ans.begin();itr!=ans.end();){
      cout << *itr;
      itr++;
      if(itr!=ans.end()){
	cout << ", ";
      }else{
	break;
      }
    }
    cout << "]"<<endl;
  }
  return 0;
}

void combine(list<char>& ans, map<char,int>& obase,map<char,set<char> >& c_table, map<pair<char,char>,char>& cm_table){
  if(ans.size()<2) return;
  list<char>::iterator itr=ans.end();
  itr--;
  list<char>::iterator itr2=itr;
  itr2--;
  if(c_table[*itr].find(*itr2)!=c_table[*itr].end()){
    char a=min(*itr,*itr2);
    char b=max(*itr,*itr2);
    ans.erase(itr);
    ans.erase(itr2);
    ans.push_back(cm_table[make_pair(a,b)]);
    obase[a]--;
    obase[b]--;
    obase[cm_table[make_pair(a,b)]]++;
    combine(ans,obase,c_table,cm_table);
  }  
  return;
}

bool opposed(list<char>& ans, map<char,int>& obase,map<char,set<char> >& d_table){
  if(ans.size()<2) return false;
  list<char>::iterator itr=ans.end();
  itr--;
  list<char>::iterator itr2=itr;
  itr2--;
  for(;;){
    if(d_table[*itr].find(*itr2)!=d_table[*itr].end()){
      obase.clear();
      ans.clear();
      return true;
    }
    if(itr2!=ans.begin())itr2--;
    else break;
  }
  return false;
}
