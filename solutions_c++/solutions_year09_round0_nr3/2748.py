#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

void process_line(string line);
int process(string str, string substr);
void output(int count);

int main(int argc, char** argv){
  if(argc != 2) return 1;
  
  string filename = argv[1];
  
  ifstream file;
  file.open(filename.c_str(), ios::in);
  
  int num = 0, i = 0;
  file >> num;
  
  char ln[500];
  file.getline(ln, 500);
  
  string line;
  for(i = 0; i < num; i++) {
    file.getline(ln, 500);
    line = ln;
    process_line(line);
  }
  
  return 0;
}


void process_line(string line){
  string search = "welcome to code jam";
  int count = 0;
  string cropped = "";
  
  int i = 0;
  for(i = 0; i < line.size(); i++){
    int j = 0;
    bool found = false;
    for(j = 0; j < search.size(); j++){
      if(search[j] == line[i]){
	found = true; 
	break;
      }
    }
    if(found) cropped += line[i];
  }
  //~ cout << cropped << endl;
  count = process(cropped, search);
  
  
  output(count);
}

int process(string str, string substr) {
  if(substr.size() == 0) return 1;
  
  int i = 0;
  int count = 0;
  for(i = 0; i < str.size(); i++){
    if(str[i] == substr[0]) count += process(str.substr(i, str.size()-i), substr.substr(1, substr.size()-1)); 
  }
  
  //~ cerr << "Size: " << str.size() << endl;
  
  return count;
}

void output(int count){
  static int case_num = 1;
  int i = 0;
  ostringstream st;

  st << count%10000;
  string pad = "";
  for(i = 0; i < 4-st.str().size(); i++) {
    pad += "0";
  }
  
  cout << "Case #" << case_num << ": " << pad << st.str() << endl;
  
  case_num++;
}