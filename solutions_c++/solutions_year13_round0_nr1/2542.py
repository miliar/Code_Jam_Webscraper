#include <iostream>
#include <string>
#include <set>
#include <utility>
#include <vector>
using namespace std;

int judge(char (&b)[4][4]){
  char c = b[0][0]; bool w=true;
  if( c != '.' ){
    for(int i=0; i<4; i++){
      if( b[i][i] != c && b[i][i] != 'T')
	w=false;
    }
  }else
    w=false;
  if(w){
    if( c=='X' ){
      return 0;
    }else
      return 1;
  }

  c = b[0][3]; w = true;
  if( c != '.' ){
    for(int i=0; i<4; i++){
      if( b[i][3-i] != c && b[i][3-i] != 'T')
	w=false;
    }
  }else
    w=false;
  if(w){
    if( c=='X' ){
      return 0;
    }else
      return 1;
  }


  for(int i=0; i<4; i++){
    c=b[i][0]; w=true;
    if(c!='.'){
      for(int j=0; j<4; j++){
	if( b[i][j] != c && b[i][j] != 'T')
	  w=false;
      }
    }else
      w=false;
    if(w){
      if( c=='X' ){
	return 0;
      }else
	return 1;
    }
  }


  for(int i=0; i<4; i++){
    c=b[0][i];  w=true;
    if(c!='.'){
      for(int j=0; j<4; j++){
	if( b[j][i] != c && b[j][i] != 'T')
	  w=false;
      }
    }else
      w=false;
    if(w){
      if( c=='X' ){
	return 0;
      }else
	return 1;
    }
  }

  int r=2;
  for(int i=0; i<4; i++){
     for(int j=0; j<4; j++){
       if( b[i][j] == '.' )
	 r=3;
     } 
  }
  return r;
}

int main(){
  int t;
  cin>>t;
  for(int i=0; i<t; i++){
    char b[4][4];
    for(int j=0; j<4; j++){
      for(int k=0;k<4; k++){
	cin>>b[j][k];
      }
    }
    int ans=judge(b);
    cout << "Case #" << (i+1)<<": ";
    switch( ans ){
    case 0:
      cout<<"X won";
      break;
    case 1:
      cout<<"O won";
      break;
    case 2:
      cout<<"Draw";

      break;
    case 3:
      cout<<"Game has not completed";
    }
    cout<<endl;
  }



  return 0;
}
