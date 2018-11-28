#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstring>
#include <cassert>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <cmath>
#include <limits>

using namespace std;

int str2int (const string &str) {
  stringstream ss(str);
  int n;
  ss >> n;
  return n;
}

struct node{
  char path[102];
  struct node *cnode[200];
  int cnum;
};

int main(int argc, char *argv[])
{
  assert(argc == 2);  //!!!!
  ifstream inFile(argv[1], ifstream::in);
  string line;
  bool isFirstLine = true;
  int T;
  int tcNo = 0;

  while(getline(inFile, line))
  {  
    if(isFirstLine){
      isFirstLine = false;
      T = str2int (line);  //T
      //cout << T << endl;
      continue;
    }    
    
    char * cstr, *p;
    cstr = new char [line.size()+1];
    strcpy(cstr, line.c_str());
    p = strtok(cstr, " "); 
    assert(p!=NULL);
    string tmp = p;
    int N = str2int(tmp);
    p = strtok(NULL, " "); 
    assert(p!=NULL);
    tmp = p;
    int M = str2int(tmp);
    delete[] cstr;
    
    struct node *root = (struct node *)malloc(sizeof(struct node));
    strcpy(root->path, ""); //????
    for(int i = 0; i < 200; i ++) root->cnode[i] = NULL;
    root->cnum = 0;
    struct node *curr = root;
    
    for(int i = 0; i < N; i ++){
      getline(inFile, line);
      cstr = new char [line.size()+1];
      strcpy(cstr, line.c_str());
      p = strtok(cstr, "/"); 
      curr = root;
      while(p){
        /*struct node *n = (struct node *)malloc(sizeof(struct node));
        strcpy(n->path, p);
        for(int i = 0; i < 200; i ++) n->cnode[i] = NULL;
        n->cnum = 0;
        curr->cnode[curr->cnum] = n;
        curr->cnum ++;
        curr = n;
        p = strtok(NULL, "/"); */
        int j = 0;
        //cout << curr->cnum << endl; 
        for(j = 0; j < curr->cnum; j ++){
          //cout << curr->cnode[j]->path << " " << p << endl;
          if(strcmp(p, curr->cnode[j]->path) == 0){
             //cout << "found" << endl; 
             curr = curr->cnode[j];
             goto l1; //break; //!!!!!!!!
           }
        }
        //cout << j << endl;
        if(j == curr->cnum) { 
          //cout << "Here 0" << endl; cout << p << endl; 
          struct node *n = (struct node *)malloc(sizeof(struct node));
          strcpy(n->path, p);
          for(int i = 0; i < 200; i ++) n->cnode[i] = NULL;
          n->cnum = 0;
          curr->cnode[curr->cnum] = n;
          curr->cnum ++;
          curr = n;
          //cout << root->cnum << " " << root->cnode[0]->path << endl; cin.ignore();
        }//if(j == curr->cnum)
l1:     p = strtok(NULL, "/"); 
      }
      
      delete[] cstr;
    }
    
    int mkdir = 0;
    for(int i = 0; i < M; i ++){
      getline(inFile, line);
      //cout << line << endl;
      cstr = new char [line.size()+1];
      strcpy(cstr, line.c_str());
      p = strtok(cstr, "/"); 
      curr = root; 
      while(p){
        int j = 0;
        //cout << curr->cnum << endl; cin.ignore();
        for(j = 0; j < curr->cnum; j ++){
          if(strcmp(p, curr->cnode[j]->path) == 0){
             //cout << "Here 0" << endl; cout << p << endl;
             curr = curr->cnode[j];
             goto l2; //break; //!!!!!!!!
           }
        }
        if(j == curr->cnum) { 
          //cout << "Here 1" << endl; cout << p << endl; cin.ignore();
          mkdir ++; 
          struct node *n = (struct node *)malloc(sizeof(struct node));
          strcpy(n->path, p);
          for(int i = 0; i < 200; i ++) n->cnode[i] = NULL;
          n->cnum = 0;
          curr->cnode[curr->cnum] = n;
          curr->cnum ++;
          curr = n;
        }//if(j == curr->cnum)
l2:     p = strtok(NULL, "/"); 
      }
      delete[] cstr;
    }
    
    tcNo ++;
    cout << "Case #" << tcNo << ": " << mkdir << endl;
    
 } //while(getline(inFile, line))  
    
  assert(tcNo == T);
  return 0;    
}
