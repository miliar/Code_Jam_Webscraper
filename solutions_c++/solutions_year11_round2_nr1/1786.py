#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>
#include <numeric>

using namespace std;

vector<double> solve(int n, const vector<string>&);

int main(){
  int num_cases;
  cin >> num_cases;
  for(int i = 0; i < num_cases; i++){
    int n;
    cin >> n;
    vector<string> table;
    for(int j = 0; j < n; j++){
      string s;
      cin >> s;
      table.push_back(s);
    }
    vector<double> r = solve(n, table);
    cout.setf(ios::fixed, ios::floatfield);
    cout << "Case #" << i+1 << ":" << endl;
    for(int j = 0; j < n; j++)
      cout << r[j] << endl;
  }
}

double calc_owp(int current, int n,
		const vector<int>& win, const vector<int>& lose,
		const vector<string>& table){
  vector<double> owpvec;
  for(int i = 0; i < n; i++){
    if(table[i][current] == '.') continue;
    else if(table[i][current] == '1') {
      owpvec.push_back(static_cast<double>(win[i]-1)/
		       static_cast<double>(win[i]-1 + lose[i]));
    } else if(table[i][current] == '0') {
      owpvec.push_back(static_cast<double>(win[i])/
		       static_cast<double>(win[i] + lose[i]-1));
    }
  }
  double sum = accumulate(owpvec.begin(),owpvec.end(),0.0);
  return sum/static_cast<double>(owpvec.size());
}

double get_oowp(int current, int n, const vector<double>& owp,
		const vector<string>& table){
  vector<double> oowp;
  for(int i = 0; i < n; i++){
    if(table[current][i] != '.') oowp.push_back(owp[i]);
  }
  double sum = accumulate(oowp.begin(),oowp.end(),0.0);
  return sum/static_cast<double>(oowp.size());
}

vector<double> solve(int n, const vector<string>& table){
  vector<double> owp(n), rpi(n);
  vector<int> win(n),lose(n);
  for(int i = 0; i < n; i++){
    win[i] = static_cast<int>(count(table[i].begin(),table[i].end(),'1'));
    lose[i] = static_cast<int>(count(table[i].begin(),table[i].end(),'0'));
  }
  for(int i = 0; i < n; i++){
    owp[i] = calc_owp(i,n,win,lose,table);
  }
  for(int i = 0; i < n; i++){
    rpi[i] = (static_cast<double>(win[i])/static_cast<double>(win[i]+lose[i]))
      * 0.25 + owp[i] * 0.50 + get_oowp(i,n,owp,table) * 0.25;
  }
  return rpi;
}
