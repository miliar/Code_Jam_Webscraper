#include <iostream>
#include <map>
#include <string>

using namespace std;

#define DEBUG 0
#define last2chars(s) \
  s.size() >= 2 ? s.substr(s.size() - 2, 2) : string("")
#define lastchar(s) \
  s[s.size() - 1]
#define replace_last2chars(s1, s2) \
  do { \
    current[s1[s1.size() - 2]] = current[s1[s1.size() - 2]] - 1; \
    current[s1[s1.size() - 1]] = current[s1[s1.size() - 1]] - 1; \
    s1.replace(s1.size() - 2, 2, 1, s2); \
  } while(0)

map<string, char> combined;
map<char, char> opposed;
map<char, int> current;
int c, d, n;
string input;
string result;

int t;

static inline void read_input()
{
  cin >> c;
  for (int i = 0; i < c; ++i) {
    char c_comb[4];
    cin >> c_comb;
    combined[string(c_comb, 2)] = c_comb[2];
    char tmp = c_comb[0];
    c_comb[0] = c_comb[1];
    c_comb[1] = tmp;
    combined[string(c_comb, 2)] = c_comb[2];
  }
  cin >> d;
  for (int i = 0; i < d; ++i) {
    string op;
    cin >> op;
    opposed[op[0]] = op[1];
    opposed[op[1]] = op[0];
  }
  cin >> n;
  for (int i = 0; i < n; ++i) {
    char chr;
    cin >> chr;
    input.append(1, chr);
  }
}

static inline void reset()
{
  combined.clear();
  opposed.clear();
  current.clear();
  input.clear();
  result.clear();
  read_input();
}

static inline void play()
{
  int sz = input.size();
  for (int i = 0; i < sz; ++i) {
    result.append(1, input[i]);
    current[input[i]] = current[input[i]] + 1;

    map<string, char>::iterator comb_it;
    string last = last2chars(result);
    if ((comb_it = combined.find(last)) != combined.end()) {
#if DEBUG == 1
      cout << "Replacing: " << result << " -> " << string(1, comb_it->second) << endl;
#endif      
      replace_last2chars(result, comb_it->second);
    }

    map<char, char>::iterator op_it;
    if ((op_it = opposed.find(lastchar(result))) != opposed.end()) {
#if DEBUG == 1
      cout << "Found possible opposed: " << lastchar(result) << endl;
#endif
      map<char, int>::iterator cur_it;
      if ((cur_it = current.find(op_it->second)) != current.end() && cur_it->second) {
#if DEBUG == 1
      cout << "Found opposed: " << cur_it->second << endl;
#endif
        result.clear();
        current.clear();
      }
    }
#if DEBUG == 1
    cout << "Result = " << result << endl;
#endif
  } 
}

static inline void display()
{
  int sz = result.size();
  cout <<"[";
  for (int i = 0; i < sz; ++i) {
    cout << result[i];
    if (i < sz - 1)
      cout << ", ";
  }
  cout <<"]";
}

int main()
{
  cin >> t;
  for (int i = 0; i < t; ++i) {
    reset();
    play();
    cout << "Case #" << i + 1 << ": ";
    display();
    cout << endl;
  } 
  return 0;
}
