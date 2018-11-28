#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

struct trip
{
  char from;     
  int d;
  int at;
  struct trip* next;  
};

void insert_trip(struct trip* p, struct trip* tt)
{
  struct trip* q;
  q = tt;
  while (q->next != NULL) {
    if (p->d < q->next->d) {
      p->next = q->next;
      q->next = p;
      break;       
    }    
    q = q->next;
  }   
  if (q->next == NULL) {
    p->next = NULL;
    q->next = p;
  }
}

int main(int argc, char *argv[])
{
  ifstream inFile;      
  ofstream outFile; 
       
  int n, t, na, nb;
  int ta0, tb0, ta, tb;
  int in, i;
  string str;
  
  struct trip* tt;
  struct trip* on_trip;
  struct trip* p;
  struct trip* q;
  
  inFile.open("B-large.in");  
  outFile.open("results.txt");  

  if (!inFile) {
    cerr << "Unable to open file datafile.txt";
    exit(1);   
  };  
  if (!outFile) {
    cerr << "Unable to open file results.txt";
    exit(1);   
  };  

  // heads
  tt = new struct trip;
  tt->next = NULL;
  on_trip = new struct trip;
  on_trip->next = NULL;
  
  getline(inFile, str);   
  n = atoi(str.c_str());
  for (in=0; in<n; in++) {
    getline(inFile, str);   
    t = atoi(str.c_str());
    ta0 = tb0 = ta = tb = 0;
    // free
    while (tt->next != NULL) {
      p = tt->next;
      tt->next = tt->next->next;
      delete p;
    }   
    while (on_trip->next != NULL) {
      p = on_trip->next;
      on_trip->next = on_trip->next->next;
      delete p;
    }   
    // load data
    getline(inFile, str, ' ');   
    na = atoi(str.c_str());
    getline(inFile, str);   
    nb = atoi(str.c_str());
    for (i=0; i<na; i++) {
      p = new struct trip;  
      p->from = 'a';
      getline(inFile, str, ':');
      p->d = atoi(str.c_str())*60;
      getline(inFile, str, ' ');
      p->d += atoi(str.c_str());
      getline(inFile, str, ':');
      p->at = atoi(str.c_str())*60;
      getline(inFile, str);
      p->at += atoi(str.c_str());
      p->at += t;
      insert_trip(p,tt);
    };
    for (i=0; i<nb; i++) {
      p = new struct trip;  
      p->from = 'b';
      getline(inFile, str, ':');
      p->d = atoi(str.c_str())*60;
      getline(inFile, str, ' ');
      p->d += atoi(str.c_str());
      getline(inFile, str, ':');
      p->at = atoi(str.c_str())*60;
      getline(inFile, str);
      p->at += atoi(str.c_str());
      p->at += t;
      insert_trip(p,tt);
    };
 
    while (tt->next != NULL) {
      // arrived and ready to go
      p = on_trip;
      while (p->next != NULL) {
        if (tt->next->d >= p->next->at) {
          if (p->next->from == 'a') tb++;
          else ta++;
          q = p->next;
          p->next = p->next->next;
          delete q;
        }                    
        else p = p->next;
      }   
      // start train
      p = tt->next;
      tt->next = tt->next->next;
      if (p->from == 'a') {
        if (ta == 0) {
          ta0++;     
          ta++;
        };
        ta--;
      }
      else {
        if (tb == 0) {
          tb0++;     
          tb++;
        };
        tb--;
      };
      insert_trip(p,on_trip);
    };
    outFile << "Case #" << in+1  << ": " << ta0 << " " << tb0 << endl;
  }
 
  inFile.close();    
  outFile.close();    
  
  return EXIT_SUCCESS;
}
