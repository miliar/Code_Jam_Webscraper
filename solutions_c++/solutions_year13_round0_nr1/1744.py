#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<fstream>
#include<numeric>
using namespace std;

vector<string> rotate90(vector<string> &v, int n){
  for(int i=0; i<n/2; i++){
    int  last = n-1-i;
    for(int j=i; j<last; j++){
      int offset = j- i;
      char top = v[i][j];
      v[i][j]=v[last - offset][i];
      v[last-offset][i]= v[last][last - offset];
      v[last][last - offset] = v[j][last];
      v[j][last] = top;
    }
  }
  return v;
} //rotates to work on row instead of columns -- tedious

int count(string s, char c){
  int cunt=0;
  for(int i=0; i<4; i++)
    if(s[i]==c)
      cunt++;
  return cunt;
}




string winner(vector<string> v)
{
  string ss, d1, d2;
  for(int i=0; i<4; i++){
    d1.push_back(v[i][i]);
    if(count(v[i],'X')==4 || ( count(v[i],'X')==3 && count(v[i],'T')==1)) return "X won";
    else if(count(v[i],'O')==4 || ( count(v[i],'O')==3 && count(v[i],'T')==1)) return "O won";
  }
  rotate90(v,4);
  for(int i=0; i<4; i++){
    d2.push_back(v[i][i]);
    if(count(v[i],'X')==4 || ( count(v[i],'X')==3 && count(v[i],'T')==1)) return "X won";
    else if(count(v[i],'O')==4 || ( count(v[i],'O')==3 && count(v[i],'T')==1)) return "O won";
  }
  if(count(d1,'X')==4 || ( count(d1,'X')==3 && count(d1,'T')==1)) return "X won";
  else if(count(d1,'O')==4 || ( count(d1,'O')==3 && count(d1,'T')==1)) return "O won";
  else if(count(d2,'X')==4 || ( count(d2,'X')==3 && count(d2,'T')==1)) return "X won";
  else if(count(d2,'O')==4 || ( count(d2,'O')==3 && count(d2,'T')==1)) return "O won";
  else if(accumulate(v.begin(), v.end(), string("")).find('.')!=-1) return "Game has not completed";
  else return "Draw";
} // this generates the winner


int main(){
  ifstream infile("input.in");
  ofstream outfile("output.out");
  int a;
   string s;
  infile>>a; getline(infile,s);
  for(int i=0; i<a; i++){
    vector<string> v;
    for(int i=0; i<4; i++){
      getline(infile,s);
      v.push_back(s);
    }
    outfile<<"Case #"<<i+1<<": "<<winner(v)<<endl;
     getline(infile,s);
  }
}
