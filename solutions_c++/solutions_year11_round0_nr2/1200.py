#include <iostream>
#include <vector>
#include <string>

using namespace std;
ostream& operator<< (ostream& _cout, const vector<char>& out)
{
    _cout << '[';
    int i = 0;    
    for (i = 0; i+1 < out.size(); i++)
    {
      _cout << out[i] << ", ";
    }
    if (i < out.size()) _cout << out[i];
    _cout << ']';
    return _cout;
}
struct combine
{
  char a,b;
  char c;
  combine() {}
  combine(char A, char B, char C) { a = A; b = B; c = C; }
  combine(istream& o)
  {
    o >> ws >> a >> b >> c;
  }
  bool match(vector<char>& v)
  {    
    if (v.size() > 1)
    if ((v[v.size()-1] == a && v[v.size()-2] == b) || (v[v.size()-1] == b && v[v.size()-2] ==a))
    {
      v.pop_back();
      v.pop_back();
      v.push_back(c);
      return true;
    }
    else return false;
  }
  
};

struct oppose
{
  char a,b;
  int i_a, i_b;
  bool matching_a, matching_b;
  oppose() {}
  oppose(char A, char B) { a = A; b = B; 
   i_a = 0; i_b = 0; matching_a = false; matching_b = false;
  }
  oppose(istream& o)
  {
    o >> ws >> a >> b;
    i_a = 0; i_b = 0; matching_a = false; matching_b = false;
  }
  bool match(vector<char>& v)
  {    
    if (matching_a)
    { //check to see if still valid
      if (i_a >= v.size()) { i_a = 0; matching_a = false;}
      else if (v[i_a] != a) { i_a = 0; matching_a = false;}
      else //we're still valid
      {
        if (v[v.size()-1] == b)
        {
          v.clear();
          i_a = 0; i_b = 0; matching_a = false; matching_b = false;
          return true;
        }        
      }
    }
    else
    {
      if (v[v.size()-1] == a)
      {
        i_a = v.size()-1;
        matching_a = true;
      }
    }
    
    //now for b
    if (matching_b)
    { //check to see if still valid
      if (i_b >= v.size()) { i_b = 0; matching_b = false;}
      else if (v[i_b] != b) { i_b = 0; matching_b = false;}
      else //we're still valid
      {
        if (v[v.size()-1] == a)
        {
          v.clear();
          i_a = 0; i_b = 0; matching_a = false; matching_b = false;
          return true;
        }        
      }
    }
    else
    {
      if (v[v.size()-1] == b)
      {
        i_b = v.size()-1;
        matching_b = true;
      }
    }
  return false;
  }
  
};


int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++)
  {
    int c,d,n;
    vector<combine> cs;
    vector<oppose> os;
    vector<char> out;
    cin >> c;

    for (int i = 0; i < c; i++) 
    {
      combine c(cin);
      cs.push_back(c);
    }
    cin >> d;
    for (int i = 0; i < d; i++)
    {
      oppose c(cin);
      os.push_back(c);
    }
    cin >> n;
    bool skip = false;
    for (int i = 0; i < n; i++)
    {  
        char c_; cin >> c_;
        out.push_back(c_);
        //cout << out << endl;      
      
      bool matched = true;
      while (matched){
        matched = false;
        for (int j = 0; j < c && !matched; j++) 
        {
          matched = cs[j].match(out);          
        }
      }
      for (int j = 0; j < d && !matched; j++) 
      {
        matched = os[j].match(out);          
      }
      
      
    }
    cout << "Case #" << t << ": " << out << endl;
  }
}