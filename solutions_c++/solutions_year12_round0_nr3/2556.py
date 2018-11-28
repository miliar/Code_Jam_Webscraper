#include<fstream>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<utility>

using namespace std;

int main(int argc, char *argv[]){
  long int i,j,count,a,b,n,m,len;
  string strn;
  string strtemp;
  ifstream infile;
  stringstream nstream;
  istringstream iss; 
  vector<string> vec;
  string ss;
  pair<long int, long int> intpair;
  set< pair<long int, long int> > pairset;
  bool ispair=false;
  char *filename=argv[1];
  infile.open(filename); 
 
  while(infile.good()){
    getline(infile,ss);
    vec.push_back(ss);
  }
  infile.close();
  
   
  i=1;

  while(i<vec.size()-1){
    count=0;
    ss=vec[i];
    iss.clear();
    iss.str(ss);
    iss>>a;
    iss>>b;

      for(n=a;n<b;++n){
      nstream.str("");
      nstream<<n;
      strn=nstream.str();
      ss=strn+strn;
      len=strn.length();
     
 for(j=0;j<len;++j){
 strtemp=ss.substr(j,len);
 istringstream(strtemp)>>m;
 if(m<=b&&m>n){
   intpair=make_pair(n,m); 
   pairset.insert(intpair);
 }
 }} 
      cout<<"Case #"<<i<<": "<<pairset.size()<<endl;
      pairset.clear();
    i++;
    }
  return 0;
}
