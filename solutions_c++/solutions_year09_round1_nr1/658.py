#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define syso system("pause")

using namespace std;

// this function splits string s by pattern pat
vector <string> split(string s, string pat){
	vector <string> ret;
	ret.clear();
	int idx = 0, i = 0;
	while (idx < s.sz){
		i = s.find(pat, idx);
		if (i == -1)
			break;
		ret.pb(s.substr(idx, i - idx));
		idx = i + pat.sz;
	}
	if (idx < s.sz)
		ret.pb(s.substr(idx));
	return ret;
}


long long toBase(long long val, int base){
  long long st = 1, ret = 0;
  while (val){
    ret += (val % base) * st;
    st *= 10;
    val /= base;
  }
  
  return ret;
}

short int hn[100000][11];
map<int, bool> vis;

vector<int> todig(long long val){
  vector<int> ret;
  ret.clear();
  while (val){
    ret.pb(val % 10);
    val /= 10;
  }
  
  return ret;
}

short int rec(int val, int b){
  if (val == 1)
    return hn[val][b] = 1;
    
  if (vis[val])
    return hn[val][b] = 2;
  
  vis[val] = true;
  if (hn[val][b] != 0)
    return hn[val][b];
    
  long long v = toBase(val, b);
  
  vector<int> d = todig(v);
  int s = 0;
  FOR (i, d.sz)
    s += d[i] * d[i];
    
  return hn[val][b] = rec(s, b);
}

int main(){
  freopen("As.out","wt", stdout);
  freopen("As.in","r", stdin);
  SET(hn, 0);
  ffor (i, 1, 100000)
    ffor (j, 2, 11){
      vis.clear();
      hn[i][j] = rec(i, j);
    }
    
  int tests, b;
  scanf("%d\n", &tests);
  vector<int> bb;
  char str[100000];
  FOR (test, tests){
    gets(str);
    string s = string(str);
    vector<string> tmp = split(s, " ");
    bb.clear();
    FOR (i, tmp.sz)
      if (tmp[i].sz == 2)
        bb.pb(10);
      else
        bb.pb(tmp[i][0] - '0');
      
    int ret = 2;
    while (true){
      bool h = true;
      FOR (i, bb.sz)
        h &= (hn[ret][bb[i]] == 1);
        
      if (h)
        break;
        
      ret++;
    }
    
    cout << "Case #" << (test + 1) << ": " << ret << endl;
  }
  return 0;
}
