#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string out;

bool combina(vector<string> combine, string c) {
  string s1 = out[out.size() - 1] + c;
  string s2 = c + out[out.size() - 1];
  string combinacao, substituicao;
  for (int i = 0; i < combine.size(); i++) {
    combinacao = combine[i].substr(0, 2);
    substituicao = combine[i].substr(2, 1);
    if (combinacao == s1 || combinacao == s2) {
      out = out.substr(0, out.size() - 1) + substituicao;  
      return true;
    }
  }
  return false;   
}

bool limpa(vector<string> oposite, string c) {
  string s1, s2;
  for (int i = 0; i < out.size(); i++) {
    s1 = out.substr(i, 1) + c;
    s2 = c + out.substr(i, 1);
    for (int j = 0; j < oposite.size(); j++) {
      if (oposite[j] == s1 || oposite[j] == s2) {
        out = "";
        return true;
      }
    }
  }
  return false;
}

int main() {
  int n, m;
  cin >> n;
  vector<string> combine;
  vector<string> oposite;
  string aux, input;
  for (int i = 1; i <= n; i++)  {
    out = input = "";
    combine.clear();
    oposite.clear();
    cin >> m;
    while (m > 0) {
      cin >> aux;
      combine.push_back(aux);
      m--;
    }
    cin >> m;
    while (m > 0) {
      cin >> aux;
      oposite.push_back(aux);
      m--;
    }
    cin >> m;
    cin >> input;
    out = input.substr(0, 1);
    for (int j = 1; j < input.size(); j++) {
      if (!combina(combine, input.substr(j, 1)))
        if (!limpa(oposite, input.substr(j, 1)))
          out += input.substr(j, 1);
    }

    cout << "Case #" << i << ": [";
    for (int k = 0; k < out.size(); k++) {
      cout << out[k];
      if (k + 1 < out.size()) 
        cout << ", ";
    }
    cout << "]" << endl;
  }
}
