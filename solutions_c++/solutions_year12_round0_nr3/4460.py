#include <vector>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

bool is_recycled(string a, string b) {

  int split_point = 1;

  string c; 

  for (split_point = 1; split_point < a.size(); split_point++) {
    c = a.substr(split_point);
    c.append(a.substr(0, split_point));
  
    if (c.compare(b) == 0 && c[0] != '0') {
//      cout << a << " " << b << endl;
      return true;
    }
  }
  
  return false;
}

int main()
{
  int T;
  cin >> T;
  int a, b;
  int cases = 0;

  while (T) {
    T--;
    cin >> a >> b;
    string i_str, j_str;

    stringstream str_out;

    int counter = 0;
    for (int i = a; i <= b; i++) {
      for (int j = i+1; j <= b; j++) {
        str_out.str("");
        str_out << i;
        i_str = str_out.str();
       
        str_out.str("");
        str_out << j;
        j_str = str_out.str();

        if (is_recycled(i_str, j_str))
          counter++;

        //   cout << i_str <<  " " << j_str; 
      }
    }    
    cout << "Case #" << ++cases << ": " << counter << endl;
  }

  return 0;
}
