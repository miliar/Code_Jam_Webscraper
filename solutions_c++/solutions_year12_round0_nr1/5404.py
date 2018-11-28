#include <vector>
#include <string>
#include <iostream>

using namespace std;

char g_e[30];
char e_g[30];

int main()
{
  vector <string> data_g;
  data_g.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
  data_g.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  data_g.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");
 
  vector <string> data_e;
  data_e.push_back("our language is impossible to understand");
  data_e.push_back("there are twenty six factorial possibilities");
  data_e.push_back("so it is okay if you want to just give upi");
  
 
  vector <string>::iterator it;
  vector <string>::iterator it_e;
 
  for(it = data_g.begin(), it_e = data_e.begin();
      it != data_g.end(); 
      it++, it_e++) {
    
    const char * t_d_e;
    const char * t_d_g;

    t_d_g = it->c_str();
    t_d_e = it_e->c_str();

    for(int i = 0; i <  it->size(); i++) {
      g_e[*(t_d_g + i) - 'a'] = *(t_d_e + i);
      //e_g[*(t_d_e + i) - 'a'] = *(t_d_g + i);
    }
  }

  // patch it
  g_e['z'-'a'] = 'q';
  g_e['q'-'a'] = 'z';

  string line;
  int cases = 1;
  getline(cin, line);

  while (getline(cin, line)) {
    cout << "Case #" << cases++ << ": "; 

    const char * data_buffer = line.c_str();

    for (int i = 0; i < line.size(); i++) {
      if (*(data_buffer + i) == ' ')
        cout << ' ';
      else
        cout << g_e[*(data_buffer + i) -'a'];
    }
    
    cout << endl;
  }
  return 0;
}
