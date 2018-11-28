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
    
  int matrix_size=4;  
  int K=4;
  bool dot=false;
    
  char manip[matrix_size][matrix_size];
  
  for (int i=0;i<matrix_size;i++){
    for (int k=0;k<matrix_size;k++){
      char curr;
      cin >> curr;
      manip[i][k]=curr;
      if (curr=='.') dot=true;
    }
  }
  
  bool XWin=false;
  bool OWin=false;
  
  for (int i=0;i<matrix_size;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=0;k<matrix_size;k++){
      char element=manip[i][k];
      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   
  
  for (int i=0;i<matrix_size;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=0;k<matrix_size;k++){
      char element=manip[k][i];
      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   
    
  for (int i=K-1;i<matrix_size;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=0;k<i+1;k++){
      char element=manip[i-k][k];

      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   
  
  for (int i=1;i<matrix_size-K+1;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=i;k<matrix_size;k++){
      char element=manip[matrix_size+i-k-1][k];

      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   

  for (int i=0;i<matrix_size-K+1;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=0;k<matrix_size-i;k++){
      char element=manip[k+i][k];
     
      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   
  
  for (int i=1;i<matrix_size-K+1;i++){
    int Xcount=0;
    int Ocount=0;
    for (int k=0;k<matrix_size-i;k++){
      char element=manip[k][k+i];
      if (element=='O'){
	Ocount++;
	Xcount=0;
      } else if (element=='X'){
	Xcount++;
	Ocount=0;
      } else if (element=='T'){
	Xcount++;
	Ocount++;	
      } else {
	Xcount=0;
	Ocount=0;
      } 
      if (Xcount==K){
	XWin=true;
      }
      
      if (Ocount==K){
	OWin=true;
      }      
    }
  }   
 
//  }
  
  string count;
  
  if (XWin){
    count="X won";
  } else if (OWin){
    count="O won";
  } else if (dot) {
    count="Game has not completed";
  } else {
    count="Draw";
  }
  
  cout<< "Case #" << number <<": "<< count << endl;
  
  number++; 
}
  
  return 0;
}
 
