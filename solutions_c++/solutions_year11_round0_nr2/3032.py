#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>

using namespace std;

class StringPair {
public:
  StringPair() { m_char1 = m_char2 = '\0'; }
  
  StringPair(char p_char1, char p_char2) {
    if(p_char1 < p_char2)
      m_char1 = p_char1, m_char2 = p_char2;
    else
      m_char1 = p_char2, m_char2 = p_char1;
  }
  
  StringPair(const StringPair &p_sp) {
    m_char1 = p_sp.m_char1, m_char2 = p_sp.m_char2;
  }
  
  string toString() const { 
    string l_res = "12";
    
    l_res[0] = m_char1, l_res[1] = m_char2;
    
    return l_res; 
  }
  
  bool operator<(const StringPair &p_s) const {
    if(m_char1 < p_s.m_char1)
      return true;
    
    if(m_char1 > p_s.m_char1)
      return false;
    
    return m_char2 < p_s.m_char2;
  }
  
private:
  char m_char1, m_char2;
};

string stringAsArray(string p_str) {
  if(p_str == "")
    return "[]";
  
  string l_res = "[ ";
  
  l_res[l_res.size()-1] = p_str[0];
  
  for(unsigned int i = 1; i < p_str.size(); ++i)
    l_res += ",  ", l_res[l_res.size()-1] = p_str[i];
  
  return l_res + "]";
}

int main() {
  int l_test_cases;
  int l_charset['Z'-'A'+1];
  
  cin >> l_test_cases;
  
  for(int i = 0; i < l_test_cases; ++i) {
    map<StringPair, char> l_subst;
    set<StringPair> l_clear;
    set<char> l_clearset;
    int l_n, l_ns, l_no;
    string l_str;
    string l_invoked = "";
    
    memset(l_charset, 0, sizeof(l_charset));
    cin >> l_ns;

    for(int j = 0; j < l_ns; ++j)
      cin >> l_str, l_subst[StringPair(l_str[0], l_str[1])] = l_str[2];
    
    cin >> l_no;
    
    for(int j = 0; j < l_no; ++j) {
      cin >> l_str;
      
      l_clear.insert(StringPair(l_str[0], l_str[1]));
      l_clearset.insert(l_str[0]), l_clearset.insert(l_str[1]);
    }

    cin >> l_n >> l_str;
    
    cout << "Case #" << (i+1) << ": ";
    
    if(l_ns == 0 && l_no == 0) {
      cout << stringAsArray(l_str) << endl;

      continue;
    }
    
    for(unsigned int j = 0; j < l_str.size(); ++j) {
      int l_size = l_invoked.size();

      if(l_size < 1) {
        l_invoked += l_str[j];
        l_charset[l_str[j]-'A'] += 1;

        continue;
      }
      
      StringPair l_sp(l_invoked[l_size-1], l_str[j]);
      
      // substitution
      if(l_ns > 0 && (l_subst.find(l_sp) != l_subst.end())) {
        // decrease substituted char count
        l_charset[l_invoked[l_size-1]-'A'] -= 1;
        l_charset[l_str[j]-'A'] -= 1;
        // substitute
        l_invoked[l_size-1] = l_subst[l_sp];
        // increase substituting char count
        l_charset[l_invoked[l_size-1]-'A'] += 1;

        continue;
      }
        
      // maybe there are opposed pairs
      if((l_no > 0) && (l_clearset.find(l_str[j]) != l_clearset.end())) {
        // check for opposed pairs
        for(unsigned int k = 0; k < sizeof(l_charset)/sizeof(l_charset[0]); ++k) {
          char l_char = (char)(k+'A');
          
          // no character can be opposed to itself
          if(l_char == l_str[j])
            continue;
          
          // not on string or on opposed char list
          if(l_charset[k] < 1 || l_clearset.find(l_char) == l_clearset.end())
            continue;
          
          // clear
          if(l_clear.find(StringPair(l_char, l_str[j])) != l_clear.end()) {
            l_invoked = "";
            memset(l_charset, 0, sizeof(l_charset));
            
            break;
          }
        }
      }
      
      if(l_invoked != "") {
        l_invoked += l_str[j];
        l_charset[l_str[j]-'A'] += 1;
      }
    }
    
    cout << stringAsArray(l_invoked) << endl;
  }
  
  return 0;
}
