#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int l,d,n;
vector<string> dict;
string W;

int ans(string s,int pos,int wpos) {
  if (wpos>l) {
    vector<string>::iterator low = lower_bound(dict.begin(),dict.end(),W);
    if (low!=dict.end() && *low==W)
      return 1;
    return 0;
  }
  // check whether this permutation has a chance
  vector<string>::iterator low = lower_bound(dict.begin(),dict.end(),W);
  if (low==dict.end())
    return 0;
  string X = *low;
  for(int temp=0;temp<wpos;temp++) {
    if (X[temp]!=W[temp])
      return 0;
  }
  if (s[pos]=='(') {
    int all = 0;
    int i = 0;
    vector<char> letters;
    for(i=pos;s[i]!=')';i++) {
      letters.push_back(s[i]);
    }
    int n = i+1;
    for(i=0;i<letters.size();i++) {
      W[wpos] = letters[i];
      all += ans(s,n,wpos+1);
    }
    W[wpos] = '0';
    return all;
  } else {
    W[wpos] = s[pos];
    int AA = ans(s,pos+1,wpos+1);
    W[wpos] = '0';
    return AA;
  }
  W[wpos] = '0';
  return 0;
}

int main() {
  string s;
	cin >> l >> d >> n;
	for(int i=0;i<d;i++) {
	  cin >> s;
	  dict.push_back(s);
	}
	for(int i=0;i<l;i++)
	  W.push_back('0');
	sort(dict.begin(),dict.end());
	for(int i=1;i<=n;i++) {
	  cin >> s;
		cout << "Case #" << i << ": " << ans(s,0,0) << endl;
	}
	return 0;
}
