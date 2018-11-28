//Chazz Malott
//
//
//Magick
//

#include <iostream>
#include <vector>
#include <iostream>
using namespace std;

bool combotest(vector <char> &elementlist, char combos[][3], int combosize, int last){

  for(int i=0; i<combosize; i++){
    if(elementlist[last]==combos[i][0]){
      if(elementlist[last-1]==combos[i][1]){
	elementlist.pop_back();
	elementlist.pop_back();
	elementlist.push_back(combos[i][2]);

	return true;
      }
    }
    else if(elementlist[last]==combos[i][1]){
      if(elementlist[last-1]==combos[i][0]){
	elementlist.pop_back();
	elementlist.pop_back();
	elementlist.push_back(combos[i][2]);

	return true;
      }
    }
  }

  return false;
}


void opposetest(vector <char> &elementlist, char opposing[][2], int opsize, int last){

  for(int i=0; i<opsize; i++){
    if(elementlist[last]==opposing[i][0]){
      for(int j=0; j<last; j++){
	if(elementlist[j]==opposing[i][1]){
	  elementlist.clear();
	  return;
	}
      }
    }
    else if(elementlist[last]==opposing[i][1]){
      for(int j=0; j<last; j++){
	if(elementlist[j]==opposing[i][0]){
	  elementlist.clear();
	  return;
	}
      }
    }
  }

  return;
}


int main(){

  int cases = 0;
  cin>>cases;

  int combosize=0;
  int opsize=0;
  int elements=0;

  for(int i=0; i<cases; i++){

    cin>>combosize;
    char combos [combosize][3];
    char tempcombo[3];
    
    for(int j=0; j<combosize; j++){
      cin>>tempcombo;
      combos[j][0]=tempcombo[0];
      combos[j][1]=tempcombo[1];
      combos[j][2]=tempcombo[2];
    }

    cin>>opsize;
    char opposing [opsize][2];
    char tempop [2];

    for (int j=0; j<opsize; j++){
      cin>>tempop;
      opposing[j][0]=tempop[0];
      opposing[j][1]=tempop[1];
    }

    cin>>elements;

    vector <char> elementlist;
    char tempelement;
  

    for(int j=0; j<elements; j++){
      cin>>tempelement;
      elementlist.push_back(tempelement);
            if(elementlist.size()>1){
	if(!(combotest(elementlist, combos, combosize, elementlist.size()-1))){
	  opposetest(elementlist, opposing, opsize, elementlist.size()-1);
        }
      }
    }

    cout<<"Case #"<<i+1<<": [";
    if(!elementlist.empty()){
      for(int j=0; j<(elementlist.size()-1); j++){
         cout<<elementlist[j]<<", ";
      }
      cout<<elementlist[elementlist.size()-1];
    }
    cout<<"]"<<endl;
  }

  return 0;
}
