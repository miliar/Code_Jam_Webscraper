#include <iostream>
#include <string>
#include <vector>
using namespace std;

const char str[] = {
    'y', 'h', 'e', 's', 'o',
    'c', 'v', 'x', 'd', 'u',
    'i', 'g', 'l', 'b', 'k',
    'r', 'z', 't', 'n', 'w',
    'j', 'p', 'f', 'm', 'a', 
    'q'  
};

string convert(string input){
   string test = "";
   for (int i = 0; i < input.size(); i++){
       if (input[i] >= 'a' && input[i] <= 'z'){
          test.push_back( str[ input[i] - 'a' ]);
       }  else if (input[i] == ' '){
          test.push_back(input[i]);
       }   
   }
   return test;         
}

void test_convert(){
     string a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
     string b = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
     string c = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
     cout << convert(a) << endl;    
     cout << convert(b) << endl;
     cout << convert(c) << endl;    
     
}


int main(){
  int num;
  cin >> num;
  vector<string> vec(num);
  string tmp = "";
  cin.ignore(); // getline will read \n so quit it
  for (int i = 0; i < num; i++){
      getline(cin, tmp, '\n'); // release the return value using \n
      vec[i] = convert(tmp);
      tmp = "";
  }
  for (int i  = 0; i < num; i++){
      cout << "Case #";
      cout << (i + 1) ;
      cout << ": " + vec[i] << endl;  
  }
  while(true){};
 return 0;   
}
