#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int count(int s, int seq[]) {
  int i;
  int c = 0;
  for (i=0; i<s; i++) c += seq[i];
  return c;
};

void sign(int s, string se[], int seq[], string qe) {
  int i;
  for (i=0; i<s; i++) {
    if (se[i] == qe) {
      seq[i] = 1;
      break;
    };
  };
};


int main(int argc, char *argv[])
{
  ifstream inFile;      
  ofstream outFile;      
  int n,s,q;
  int in,is,iq;
  string str;
  string se[100];
  int seq[100];
  int r;
  string qe;
  
  inFile.open("A-large.in");  
  outFile.open("results.txt");  

  if (!inFile) {
    cerr << "Unable to open file datafile.txt";
    exit(1);   
  };  
  if (!outFile) {
    cerr << "Unable to open file results.txt";
    exit(1);   
  };  
  
  getline(inFile, str);   
  n = atoi(str.c_str());
  for (in=0; in<n; in++) {
    r = 0; 
    getline(inFile, str);   
    s = atoi(str.c_str());
    for (is=0; is<s; is++) {
      getline(inFile, se[is]);
      seq[is]=0;   
    }
    getline(inFile, str);   
    q = atoi(str.c_str());
    for (iq=0; iq<q; iq++) {
      getline(inFile, qe);
      sign(s, se, seq, qe);   
      if (count(s,seq) == s ) {
        r++;               
        for (is=0; is<s; is++) seq[is] = 0;
        sign(s, se, seq, qe);   
      };
    }
    outFile << "Case #" << in+1  << ": " << r << endl;
  }
 
  inFile.close();    
  outFile.close();    
  
  return EXIT_SUCCESS;
}
