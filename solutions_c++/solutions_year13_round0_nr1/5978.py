#include<iostream>
#include<fstream>
#include <stdio.h>
#include <math.h>
#include<string>
#include<sstream>
using namespace std;
const string status[] = {"X won","O won","Draw","Game has not completed"};
int func1(char array[4][4],int j){
  char c = array[0][j];
  if(c == 'T')
      c = array[1][j];
  for(int i=0 ; i<4 ; ++i){
    if(array[i][j] == 'T')
		continue;
      if(array[i][j] != c || array[i][j] == '.')
			return -1;
  }
  return ((c == 'O') ? 1 : 0);
}
int func2(char array[4][4],int i){
  char c = array[i][0];
  if(c == 'T')
      c = array[i][1];
  for(int j=0 ; j<4 ; ++j){
    if(array[i][j] == 'T')
		continue;
      if(array[i][j] != c || array[i][j] == '.')
		return -1;
  }
  return ((c == 'O') ? 1 : 0);
}
int func3(char array[4][4]){
  char c = array[0][0];
  if(c == 'T')
      c = array[1][1];
  for(int i=0 ; i<4 ; ++i){
    if(array[i][i] == 'T')
		continue;
      if(array[i][i] != c || array[i][i] == '.')
		return -1;
  }
  return ((c == 'O') ? 1 : 0);
}
int func4(char array[4][4]){
  char c = array[0][3];
  if(c == 'T')
      c = array[1][2];
  int j = 3;
  for(int i=0 ; i<4 ; ++i,--j){
      if(array[i][j] == 'T')
		continue;
      if(array[i][j] != c || array[i][j] == '.')
		return -1;
  }
  return ((c == 'O') ? 1 : 0);
}
int main(){
  int t;
  ifstream in("A-large.in");
  ofstream out("outtt.txt");
  in >> t;
  char arr[4][4];
  for(int aa=1; aa<=t ; aa++){
    int win = 0;
    bool done = false;
    for(int i=0 ; i<4 ; ++i)
      for(int j=0 ; j<4 ; ++j)
		in >> arr[i][j];
    for(int i=0 ; i<4 ; ++i){
      int a = func2(arr,i);
      if(a != -1){
	  	out << "Case #" << aa << ": " << status[a] << endl;
	  	done = true;
	 	 break;
      }
      a = func1(arr,i);
      if(a != -1){
	  	out << "Case #" << aa << ": " << status[a] << endl;
	  	done = true;
	  	break;
      }
    }
    if(done)
      continue;
    int a = func3(arr);
    if(a != -1){
		out << "Case #" << aa << ": " << status[a] << endl;
		continue;
    }
    a = func4(arr);
    if(a != -1){
		out << "Case #" << aa << ": " << status[a] << endl;
		continue;
    }
    a = 0;
    for(int i=0 ; i<4 ; ++i){
      for(int j=0 ; j<4 ; ++j){
	if(arr[i][j] == '.'){
	  a = 1;
	  break;
	}
      }
    }
    if(a)
      out << "Case #" << aa << ": " << status[3] << endl;
    else
      out << "Case #" << aa << ": " << status[2] << endl;
  }
  return 0;
}
