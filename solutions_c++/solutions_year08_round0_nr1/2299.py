#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
using namespace std;

int main()
{
int tc;
cin>>tc;

int count=0;
while(tc--){
  int strings;
  int queries;
  int i, ans =0;
  cin>>strings; cin.ignore();
  map<string,int> myMap;
  for(i=0; i<strings; i++){
    string tempstr;
    getline(cin, tempstr);
    myMap[tempstr] =0;
 }
  map<string,int> tpMap;
  cin>>queries; cin.ignore();

  while(queries--){
    string tempstr;
    getline(cin, tempstr);
    if(myMap.count(tempstr)){
      if(!tpMap.count(tempstr))
	  tpMap[tempstr]=1;
	if(tpMap.size()==strings){
	  ans++;
	  tpMap.clear();
	  tpMap[tempstr]=1;
	}
    }
  }
cout<<"Case #"
    <<++count
    <<": "
    <<ans
    <<"\n";
}
return 0;
}
