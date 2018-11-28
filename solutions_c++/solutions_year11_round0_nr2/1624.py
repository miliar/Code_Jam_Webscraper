#include<iostream>
#include<vector>
#include<list>
#include<map>
#include<algorithm>
using namespace std;

#define REP(i,i0,in) for(int i=(i0); i<(in); i++)
#define EACH(it,c) for(__typeof((c).begin()) it=(c).begin(); it!=(c).end(); it++)

char Com[26][26];
bool Opp[26][26];

void compound(list<char> &lst){
  if (lst.size() < 2) return;
  
  list<char>::iterator it;
  char e = lst.back(); lst.pop_back();
  char s = lst.back(); lst.pop_back();
  char c = Com[s-'A'][e-'A'];
  if (c == '\0') {
    lst.push_back(s);
    lst.push_back(e);
  } else {
    lst.push_back(c);
  }
}
void oppose(list<char> &lst){
  int N = lst.size();
  if (N < 2) return;
  
  char e = lst.back();
  list<char>::iterator b = lst.begin();
  REP(i,0,N-1){
    if (Opp[*b-'A'][e-'A']) {
      lst.clear();
      break;
    }
    b++;
  }
}

list<char> compute(list<char> &lst){
  list<char> ans;
  EACH(it,lst){
    ans.push_back(*it);
    compound(ans);
    oppose(ans);
  }
  return ans;
}

int main(){
  int T;
  cin >> T;
  REP(t,0,T){
    // init
    REP(i,0,26){
      fill(Com[i],Com[i]+26,'\0');
      fill(Opp[i],Opp[i]+26,false);
    }
    // read
    int C, D, N;
    cin >> C;
    REP(ci,0,C){
      char a,b,c;
      cin >> a >> b >> c;
      Com[a-'A'][b-'A'] = c;
      Com[b-'A'][a-'A'] = c;
    }
    cin >> D;
    REP(d,0,D){
      char a,b;
      cin >> a >> b;
      Opp[a-'A'][b-'A'] = true;
      Opp[b-'A'][a-'A'] = true;
    }
    list<char> Lst;
    char ch;
    cin >> N;
    REP(i,0,N){
      cin >> ch, Lst.push_back(ch);
    }
    
    list<char> ans = compute(Lst);
    cout << "Case #" << (t+1) << ": [";
    EACH(it,ans){
      cout << *it;
      if (it != --ans.end()) {
	cout << ", ";
      }
    }
    cout << "]" << endl;
  }
  return 0;
}
