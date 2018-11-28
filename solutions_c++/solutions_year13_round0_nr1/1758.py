#include<iostream>
#include<algorithm>
#include<string>
#include<vector>
#include<fstream>
#include<numeric>
#define loop(v,i,s) for(int i=s; i<v.size(); i++)
#define loopn(n,i,s) for(int i=s; i<n; i++)
#define loopback(v,i,s) for(int i=v.size()-1; i>=s; i--)
#define loopnback(n,i,s) for(int i=n-1; i>=s; i--)
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
}

string winner(vector<string> v)
{
  string ss, d1, d2;
  for(int i=0; i<4; i++){
    d1.push_back(v[i][i]);
    if(v[i].find("XXXX")!=-1 || v[i].find("XXXT")!=-1|| v[i].find("TXXX")!=-1) return "X won";
    else if(v[i].find("OOOO")!=-1 || v[i].find("OOOT")!=-1|| v[i].find("TOOO")!=-1) return "O won";
  }
  rotate90(v,4);
  for(int i=0; i<4; i++){
    d2.push_back(v[i][i]);
    if(v[i].find("XXXX")!=-1 || v[i].find("XXXT")!=-1|| v[i].find("TXXX")!=-1) return "X won";
    else if(v[i].find("OOOO")!=-1 || v[i].find("OOOT")!=-1|| v[i].find("TOOO")!=-1) return "O won";
  }
  if(d1.find("XXXX")!=-1 || d1.find("XXXT")!=-1|| d1.find("TXXX")!=-1) return "X won";
  else if(d1.find("OOOO")!=-1 || d1.find("OOOT")!=-1|| d1.find("TOOO")!=-1) return "O won";
  else if(d2.find("XXXX")!=-1 || d2.find("XXXT")!=-1|| d2.find("TXXX")!=-1) return "X won";
  else if(d2.find("OOOO")!=-1 || d2.find("OOOT")!=-1|| d2.find("TOOO")!=-1) return "O won";
  else if(accumulate(v.begin(), v.end(), string("")).find('.')!=-1) return "Game has not completed";
  else return "Draw";
}


int main(){
  ifstream infile("input.in");
  ofstream outfile("output.out");
  int a,b,c,d,e,k;
   string s;
  infile>>a; getline(infile,s);
  loopn(a,i,0){
    vector<string> v;
    for(int i=0; i<4; i++){
      getline(infile,s);
      v.push_back(s);
    }
    outfile<<"Case #"<<i+1<<": "<<winner(v)<<endl;
     getline(infile,s);
  }
}
