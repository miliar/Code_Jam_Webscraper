#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <sstream>

using namespace std;


int main() {
  
  int cases;
  int number=1;
  cin >> cases;
 
while(cases--){  
  
  int A, B;
  
  cin >> A >> B;
  
  map<string,int> mymap;
  map<string,int>::iterator it;
  
  for (int i=A; i<=B; i++){
    ostringstream conv;
    conv << i;
    mymap[conv.str()]=0;  
  }
  
  
  it=mymap.begin();
  
  while (it != mymap.end()){
    
    string currentstring=(*it).first;

    int pair_count=0;
    
    for (int i=0;i<(currentstring.size()-1);i++){
      
      rotate(currentstring.begin(),currentstring.begin()+1,currentstring.end());
      
      stringstream tocast;
      tocast << currentstring;
      int intcurrenstring;
      tocast >> intcurrenstring;
      
      if (mymap.find(currentstring)==mymap.end() && intcurrenstring==B) {
	pair_count++; 
	continue;
      };
      
      if(intcurrenstring>B || intcurrenstring<A) {
	continue;
      };

      if (mymap.find(currentstring)!=mymap.end() && mymap.find(currentstring)!=it){ 
	pair_count++;
	mymap.erase(currentstring);
      };
      
    }
    
      
    if (pair_count!=0){
      (it->second)=pair_count; 
    };
    
    
    if (pair_count==0){
      mymap.erase(it++);
    } else {
      ++it;
    }
    
  }
  
//   cout << mymap.size() << endl;
//   for ( it=mymap.begin() ; it != mymap.end(); it++ ) cout << it->first <<endl;
  
  int pairs=0;
  
  for ( it=mymap.begin() ; it != mymap.end(); it++ ){
    pairs+=((*it).second+1)*((*it).second)/2;
  }
  
  cout<< "Case #" << number <<": "<< pairs << endl;
  
  number++; 
}
  
  return 0;
}
 
