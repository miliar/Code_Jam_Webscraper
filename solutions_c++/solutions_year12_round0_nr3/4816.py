// Created on Apr 14, 2012 3:17:46 PM

#include <iostream>
# include <map>
# include <fstream>
# include <string>
# include <sstream>
# include <vector>
using namespace std;

int getNumofCases(ifstream &input){
  int num; string line;
  getline(input,line);
  stringstream convert(line);
  convert >> num;
  return num;
}

void getNumbers(string line, int &A, int&B){
  stringstream tonum(line) ;
  tonum>>A;
  tonum>>B;
  
  
}

string rotate(string s, int k){
  //  cout << s.substr(k)+ s.substr(0,k)<<endl;
  return s.substr(k)+ s.substr(0,k);
}


string tostr(int num){
  stringstream convert;
  convert<<num;
  return convert.str();
  
}



int tonum(string s){
  int result;
  stringstream convert(s);
  convert >> result;
  return result;
}

void print(map<string,string> &wordList){
  
  map<string, string>::iterator pos;
  for(pos = wordList.begin(); pos != wordList.end(); ++pos)
  {
    cout << "Key: " << pos->first << endl;
    cout << "Value:" << pos->second << endl;
  }
  
}

bool noLeadingZeros(string s){
  if (s[0] == '0') 
  return false;
  else return true;
}

int main(int argc, char *argv[])
{
  
  
  ifstream input("A-small-practice.in");
  ofstream output("output.txt");
  int numOfCases;
  if(input.is_open() && input.good()){
    numOfCases = getNumofCases(input); //get cases first
  }
  
  
  for (int i =1 ; i<=numOfCases; i ++) {
    int A; int B;  int answer = 0;
    string m,n;  string line;
    map<string,string> found_pairs;
    output<<"Case #"<<i<<": ";
    
    if(input.good() ) getline(input, line);
    else { cout<< "Uh oh .. faulty input .. case numbers != num of lines"; return 0; }
      
    getNumbers(line,A,B);
    
    string rotated_num;
    
    for(int i = A;i <= B; i++){
      
      m = tostr(i);
      int iterations = m.size();
      rotated_num = m;
     
      for (int j=1;j<= iterations;j++){ //starting with one rotation
       if(i == 2221) {
      //   cout<<"rots"<<rotated_num<<endl; 
        }
        n =  rotate(rotated_num,1);
        if ((tonum(n)>=A) && (tonum(n)<=B) && (n!=m) && (n[0]!='0') ){// m is anyway in bounds
          
           if(! found_pairs.count(n)) {// key does not exist
            answer++;	
            found_pairs.insert( pair<string,string>( m,n));           
          }
        }
        
        rotated_num = n;	//take the onerotated n so that only one rotation is required
        
        
      } //iterate over a particular number
      
      
      
    } // over all numbers between A and B do this
    
  //  cout<<answer<<endl;
    output<<answer<<endl;
    
  //  print(found_pairs);
    
  }
  
  
//  cout<<"hello";
  return 0;
}
