// Technique: Simple Simulation
//

#include <iostream>
#include <set>


#include <vector>
#include <cmath>
#include <map>
using namespace std;

string output(map<string,char> &invoke,
	      vector<string> &oppose,
	      string start) {

  string temp;
  temp+=start[0];
  for (int j=1;j<start.length();j++) {

    temp+=start[j];
    //cout << temp << endl;
    while ((temp.length()>1) && (invoke.count(temp.substr(temp.length()-2,2))>0)) {
      char c = invoke[temp.substr(temp.length()-2,2)];
      //cout << c << endl;
      temp=temp.substr(0,temp.length()-2)+c;
    }
    
    
    
    set<char> x;
    for (int i=0;i<temp.length();i++) {
      x.insert(temp[i]);
    }
    for (int j=0;j<oppose.size();j++) {
      if ((x.count(oppose[j][0])>0) && (x.count(oppose[j][1])>0)) {
	temp="";
      }
    }
  
  }
  string t1;
  t1 = "[";
  for (int j=0;j<temp.length();j++) {
    if (j>0) t1+=", ";
    t1+=temp[j];
  }
  t1+="]";
  return t1;

}



int main() {

  int T;

  cin >> T;

  for (int x1=0;x1<T;x1++) {
    int C;
    cin >> C;
    map<string,char> invoke;
    invoke.clear();
    for (int x2=0;x2<C;x2++) {
      string s;
      cin >> s;
      string s1=s.substr(0,2);
      string s2;
      s2 ="";
      s2+=s1[1];
      s2+=s1[0];
      
      invoke[s1]=s[2];
      invoke[s2]=s[2];
    }
    int D;
    cin >>D;
    vector<string> opposed;
    opposed.resize(0);
    for (int x2=0;x2<D;x2++) {
      string s;
      cin >> s;
      opposed.push_back(s);
    }
    int N;
    cin >> N;
    // Red herring?
    string full;
    cin >> full;

    string o;
    //cout << "Here!" << full << endl;
    o=output(invoke,opposed,full);

    


    cout << "Case #"<<x1+1<<": " <<o<< endl;
  }
}
