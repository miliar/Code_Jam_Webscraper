#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<cmath>
using namespace std;
int solve(string s);

int main(int argc, char* argv[]){
  string s;
  ifstream in;
  if(argc == 2)
    in.open(argv[1]);
  else
    in.open("test.txt");

  getline(in,s);
  istringstream is(s);
  int n;
  is >> n ;

  ofstream out("output.txt");
  for(int i = 0; i < n; i++){
    
    getline(in,s);
    cout << s;
    out << "Case #" << i+1 << ": " << solve(s) << endl;
  } 
  cout << " end" << endl;
  in.close();   
}

int solve(string s){
  istringstream is(s);
  int steps;
  is >> steps;
  char robut;
  int button;
  int po = 1;
  int pb = 1;
  int sinceo = 0;
  int sinceb = 0;
  int step = 0;
  for(int i = 0; i < steps; i++){
    is >> robut;
    is >> button;
    //if next is O
    if( robut == 'O'){
      //update step
      if(abs(button-po)<= sinceo){
	step = step + 1;
        sinceb = sinceb + 1;
      } 
      else{
        step = step + 1 + abs(button-po)-sinceo;
        sinceb = sinceb + 1 + abs(button-po)-sinceo;
      }
      //update po and bo
      po = button;
      //update sinceo and sinceb
      sinceo = 0;
    }
    
    if(robut == 'B'){
      if(abs(button-pb)<= sinceb){
	step = step + 1;
        sinceo = sinceo + 1;
      }
      else{
        step = step + 1 + abs(button-pb)-sinceb;
        sinceo = sinceo + 1 + abs(button-pb) - sinceb;
      }
      pb = button;
      sinceb = 0;
    }
  }
  
  return step;
}
     
     
