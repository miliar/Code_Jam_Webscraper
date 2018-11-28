#include <iostream>
#include <set>
#include <iterator>

using namespace std;

set<pair<string,string> > data;

bool
judge(string a, string b, string s, int start, int end)
{
  int i = start;
  int j = 0;

  if(s[i] < a[0] || s[i] > b[0]) return false;

  string ss = "";
  while(i != end){
    
    ss += s[i];

    i++;
    j++;
    if(i >= s.size()) i = 0;
  }
  
  ss += s[i];
  if(s >= a && s <= b && ss >= a && ss <= b && ss != s){
    data.insert(make_pair(s, ss));
    return true;
  }

  return false;
}

void
judge_loop(string a, string b, string s)
{
  for(int i = 0; i < s.size()-1; i++){

    judge(a, b, s, s.size()-1-i, s.size()-2-i);
  }
}

void
calc(string a, string b, int c, string s)
{
  if(a.size() <= s.size()){
    if(s.size() == 1) return;
    return judge_loop(a, b, s);
  }

  for(int i = 0; i < 10; i++){ 
    //    if(c == 0 && i > b[s.size()-1]-'0') break;
    calc(a, b, (b[s.size()-1]-'0') - i, s+(char)('0'+i));
  }

}

int
main()
{
  int t; cin>>t;

  for(int i = 0; i < t; i++){
    string a, b;
    cin>>a>>b;

    int r = 0;
    data.clear();

    for(char j = a[0]; j <= b[0]; j++){
      calc(a, b, b[0]-j, string("")+(char)j);
    }

    cout<<"Case #"<<i+1<<": "<<data.size()/2<<endl;
    //    if(i == 2) break;
  }
}
