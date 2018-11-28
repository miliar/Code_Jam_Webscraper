#include<iostream>
#include<set>
#include<vector>

using namespace std;

vector<string> a;
set<char> b[100];


int main(){
  int l,d,n;
  cin >> l >> d >> n;

  string s;
  for (int i = 0; i < d; i++){
  	cin >> s;
  	a.push_back(s);
  }

  for (int k = 0; k < n; k++){
  	cin >> s;
  	for (int i = 0; i < a[0].size(); i++)
  	  b[i].clear();
  	int p = -1;
  	bool ok = false;

  	for (int i = 0; i < s.size(); i++){
  		if (s[i] != '(' &&  s[i] != ')'){
  			if (ok == false){
  				p++;
  				b[p].insert(s[i]);
  			}
  			else{
  				b[p].insert(s[i]);
  			}

  		}
  		
  		if (s[i] == '('){
  			p++;
  			ok = true;
  		}
  		if (s[i] == ')'){
  			ok = false;
  		}

  	}

  	int rez = 0;

  	for (int i = 0; i < a.size(); i++){
  		s = a[i];
  		bool ok = true;
  		for (int j = 0; j < s.size(); j++)
  			if (b[j].find(s[j]) == b[j].end())
  				ok = false;
  		if (ok)
  			rez++;
  	}

  	cout << "Case #" << k+1 << ": " << rez << endl;




  }

  return 0;
}
