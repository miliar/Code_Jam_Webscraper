#include<iostream>
#include<vector>

using namespace std;

char mapa[26] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

string tranforma(string&);

int main(){
  vector<string> res;
  string val;
  int casos;
  
  x.open("arch.txt", ios::out);
  
  cin >> casos;
  cin.ignore();
  
  for (int i = 0; i<casos; i++){
    getline(cin, val);
    res.push_back(tranforma(val));
  }
  
  for (int i = 0; i<casos; i++){
    cout << "Case #" << (i+1) << ": " << res[i] << endl;
  }
  
  return 0;
}

string tranforma(string &val){
  string nvo = "";
  
  for(int i = 0, max = val.size(); i<max; i++)
    nvo += (val.at(i)==' '?' ':mapa[val.at(i)-97]);
  
  return nvo;
}
