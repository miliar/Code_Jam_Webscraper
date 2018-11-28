#include<vector>
#include<string>
#include<fstream>
#include<iostream>
#include<map>
using namespace std;

int main(int argc, char *argv[]){
  map<char,char> mymap;
  string str, ss;
  int i,j;
  char *filename=argv[1];
  ifstream infile; 
  vector<string> vec;  
  vector<string> vecout;
  
  ss="abcdefghijklmnopqrstuvwxyz";
  str="ynficwlbkuomxsevzpdrjgthaq";
 
  for(i=0;i<26;++i)
    {mymap.insert( pair<char,char>(str[i],ss[i]));}

  infile.open(filename);
  while(infile.good()){
    getline(infile,str);
    vec.push_back(str);
  }
  infile.close();
  i=1;
  while(i<vec.size()-1){
    str=vec[i];
    ss=str;
    cout<<"Case #"<<i<<": ";
    for(j=0;j<str.length();++j){
      if((str[j]!=' ')&&(mymap.find(str[j])!=mymap.end()))
	ss[j]=mymap.find(str[j])->second;
      cout<<ss[j];
    }
    cout<<endl;
    ++i;  
}

  return 0;
}

