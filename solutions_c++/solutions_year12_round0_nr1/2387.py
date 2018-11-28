#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>

using namespace std;


int main() {
  
  int cases;
  int number=1;
  cin >> cases;
  cin.get();//remove \n character
  //cout << numeric_limits<streamsize>::max() << endl;
  map<char,char> decipher;
  
  decipher['a']='y';
  decipher['b']='h';
  decipher['c']='e';
  decipher['d']='s';
  decipher['e']='o';
  decipher['f']='c';
  decipher['g']='v';
  decipher['h']='x';
  decipher['i']='d';
  decipher['j']='u';
  decipher['k']='i';
  decipher['l']='g';
  decipher['m']='l';
  decipher['n']='b';
  decipher['o']='k';
  decipher['p']='r';
  decipher['q']='z';
  decipher['r']='t';
  decipher['s']='n';
  decipher['t']='w';
  decipher['u']='j';
  decipher['v']='p';
  decipher['w']='f';
  decipher['x']='m';
  decipher['y']='a';
  decipher['z']='q';
  
  
while(cases--){  
  
  string sentence;
 // cin.ignore(90100000,'\n');
  char letters[800];
  
  cin.getline(letters,800,'\n');
  
  sentence=string(letters);
  
  for (int i=0;i<sentence.size();i++){
    if (sentence[i]!=' '){
      sentence[i]=decipher[sentence[i]];
    }
  }
  
  cout<< "Case #" << number <<": "<< sentence << endl;

/*  for (revit=vec2.rbegin(); revit!=vec2.rend(); ++revit)
    cout << " " << *revit;
  cout << endl; */   
  
//   for (int j=0;j<listitems;j++){
//       
//       for (int k=j+1;k<listitems;k++){
// 	
// 	if ((list[j]+list[k])==cache){
// 	  cout<< "Case #" << number <<": "<< j+1 << " " << k+1 << endl;
// 	}
//     
//       }
//   
//   }
  
 number++; 
}
  
  return 0;
}
 
