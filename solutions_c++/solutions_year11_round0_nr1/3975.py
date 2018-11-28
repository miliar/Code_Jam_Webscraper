//Chazz Malott
//
//
//Bot Trust: A Trust of Bots
//

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;



int main(){


  int cases=0;
  int n = 0;
  int turns=0;
  cin>>cases;
 
  char *robot;
  vector <int> obuttons, bbuttons;
  int onbutton=0;
  int opos=0;
  int bpos=0;
  int button=0;

  for(int i=0; i<cases; i++){
    onbutton=0;
    turns=0;
    cin>>n;

    robot = new char[n];
    obuttons.clear();
    bbuttons.clear();
    for(int j=0; j<n; j++){
      cin>>robot[j];
      cin>>button;

      if(robot[j]=='O'){
	obuttons.push_back(button);
      }
      else if(robot[j]=='B'){
	bbuttons.push_back(button);
      }
    }
    opos=1;
    bpos=1;


    while(onbutton<n){

      if(robot[onbutton]=='O'){

	if(!(bbuttons.empty())){
	  if(bpos<bbuttons[0]){
	    bpos++;
	  }
	  else if(bpos>bbuttons[0]){
	    bpos--;
	  }
	}

	if(!(obuttons.empty())){
	  if(opos<obuttons[0]){
	    opos++;
	  }
	  else if(opos>obuttons[0]){
	    opos--;
	  }
	  else if(opos==obuttons[0]){
	    obuttons.erase(obuttons.begin());
	    onbutton++;
	  }
	}

      }
      else if(robot[onbutton]=='B'){
	
	if(!(obuttons.empty())){
	  if(opos<obuttons[0]){
	    opos++;
	  }
  	  else if(opos>obuttons[0]){
	    opos--;
	  }
	}

	if(!(bbuttons.empty())){
	  if(bpos<bbuttons[0]){
	    bpos++;
	  }
	  else if(bpos>bbuttons[0]){
	    bpos--;
	  }
	  else if(bpos==bbuttons[0]){
	    bbuttons.erase(bbuttons.begin());
	    onbutton++;
	  }
	}

      }
      turns++;
    }


    cout<<"Case #"<<i+1<<": "<<turns<<endl;
    //    delete buttons;
    delete robot;

  }




  return 0;
}
