#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
void moveClose(int &spot,int dest){
  if(dest==spot)
    return;
  if(dest>spot)
    spot++;
  else
    spot--;
  return;
}

int main(){
  int cases,k;
  cin >> cases;
  for(int p=0;p<cases;p++){
    int size;
    cin >> size;
    vector<int> b,o;
    char grab;
    int take;
    vector<char> seq;
    for(int i=0;i<size;i++){
      cin >> grab >> take;
      seq.push_back(grab);
      if(grab=='O')
	o.push_back(take);
      else
	b.push_back(take);
    }
    o.push_back(100000000);
    b.push_back(100000000);
    bool notDone=true;
    int org=1,blu=1,i=0,j=0;
    for(k=0;notDone;k++){
      if(seq[i+j]=='B'&&blu==b[j]){
	if(i+j==seq.size()-1){
	  k++;
	  break;
	}
	j++;
	moveClose(org,o[i]);
      } else if(seq[i+j]=='O'&&org==o[i]){
	if(i+j==seq.size()-1){
	  k++;
	  break;
	}
	i++;
	moveClose(blu,b[j]);
      } else{
	moveClose(blu,b[j]);
	moveClose(org,o[i]);
      }
    }
    cout << "Case #" << p+1 << ": " << k << endl;
  }
}
