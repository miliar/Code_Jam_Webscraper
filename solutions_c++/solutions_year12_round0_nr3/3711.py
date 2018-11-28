#include<iostream>
#include<stdio.h>
#include<fstream>
#include<string>
#include<map>
#include<cstdlib>
#include<sstream>
using namespace std;
map<string, int> pairs_dict;
map<string, int>:: iterator it;

int get_num_recycled(int A, int B){
  for (int i=A;i<=B;i++){
    stringstream ss;
    ss<<i;
    string num_str = ss.str();
    for (int j=0; j< num_str.length();j++){
      int offset = num_str.length()-1-j;
      string new_str = num_str.substr(offset, num_str.length()-offset)+num_str.substr(0,offset);
      int m=atoi(new_str.c_str());
      if (i<m && (i>A || i==A) && (m<B || m==B)){ 
        stringstream ss1,ss2;
        ss1<<i; ss2<<m;
        string key = ss1.str()+","+ss2.str();
        if (pairs_dict.find(key)!=pairs_dict.end()){
          pairs_dict[key]+=1;
        }else{
          pairs_dict[key]=1;
        }
      }
    } 
  }
  return pairs_dict.size();
}

int main(int argc, char* argv[]){
  string line;
  int num_cases, A, B;
  ifstream in_file;
  in_file.open(argv[1]);
  if (in_file.is_open()){
    getline(in_file, line);
    num_cases = atoi(line.c_str());
  }
  //cout<<num_cases<<endl; 
  for (int c=1;c<=num_cases;c++){
    getline(in_file, line);
    int found = line.find(' ');
    pairs_dict.clear();
    //cout<<found<<endl;
    A=atoi(line.substr(0,found).c_str());
    B=atoi(line.substr(found+1, line.length()).c_str());
    cout<<"Case #"<<c<<": "<<get_num_recycled(A,B)<<endl; 
  }

  return 0;
}
