#include<fstream>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
using namespace std;

int main(int argc, char *argv[]){
  int i,j,n,s,p,count,score;
  char *filename=argv[1];
  ifstream infile; 
  istringstream iss; 
  vector<string> vec;
  string ss;
  infile.open(filename); 
 
  while(infile.good()){
    getline(infile,ss);
    vec.push_back(ss);
  }
  infile.close();
  
   
  i=1;
  while(i<vec.size()){
    count=0;
    ss=vec[i];
    iss.clear();
    iss.str(ss);
    iss>>n;
    iss>>s;
    iss>>p;
    
    while(iss>>score){    
     
      if(score>=3*p)
	count++;
      else if(3*p-score<=2)
        count++;
      else if((3*p-score<=4)&&(s>=1)&&(score>0)){
        count++;
        s--;
      }
      j++;
    }
    cout<<"Case #"<<i<<": "<<count<<endl;
    count=0;
    i++;
    }
  return 0;
}

