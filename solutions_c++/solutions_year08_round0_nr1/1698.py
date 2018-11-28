#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;

int getBest(int que, int ne, string *engs, int nq, string *ques) {
 int bs=0;
 for(int i=0; i<ne;i++) {
   int j = que;
   int r=0;
   while(r==0) {
    if (j==nq) {
       r=1;
    } else if (0!=engs[i].compare(ques[j])) {
      j++;
    } else {
      r=1;
    }
   }
   if (bs<(j-que)) {
      bs=j-que;
   }
 } 
 que+=bs;
 if (que==nq) {
  return 0;
 } else {
  return 1+getBest(que, ne, engs, nq, ques);
 }
}

int work(int no, ifstream *infile, ofstream *outfile) {

   string in;
   getline(*infile,in);
   if(in.length()==0)
       return 1;
   int ne;
   sscanf (in.data(),"%i",&ne);

   string engs[ne];
   for (int i=0; i<ne;i++) {
	getline(*infile,in);
        engs[i]=in.data();
   }
   
   getline(*infile,in);
   int nq;
   sscanf (in.data(),"%i",&nq);

   string ques[nq];
   for (int i=0; i<nq;i++) {
	getline(*infile,in);
        ques[i]=in.data();
   }

   if (ne == 0) {
    char buffer [50];
    int n;
    sprintf (buffer, "Case #%i: 0\n",no);
    string out = buffer;
    (*outfile) <<  out ;
    return 0;
   }
   if (nq == 0) {
    char buffer [50];
    int n;
    sprintf (buffer, "Case #%i: 0\n",no);
    string out = buffer;
    (*outfile) <<  out ;
    return 0;
   }
  
  
  int res = getBest(0, ne, engs, nq, ques);

  char buffer [50];
  int n;
  sprintf (buffer, "Case #%i: %i\n",no,res);
  string out = buffer;
   (*outfile) <<  out ;

   return 0;
}

int main() {
   string in;
   ifstream infile;
   ofstream outfile;
   infile.open("A-large.in");
   outfile.open ("A-large.out");
   int i=0;
   getline(infile,in);
   int r=0;
   while(r==0){
       i++;
       r=work(i, &infile, &outfile);      
   }
   infile.close();
   outfile.close();
   return 0;
}
