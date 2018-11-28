#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
#include<iostream>

using namespace std;

int SIZE = 0;
int get_max_players(int, int, int*, int);
int main(int argc, char** argv){
  if(argc != 2){
    cerr<<"Invalid input provided"<<endl;
    return -1;
  }
  int N, S, p;
  ifstream in(argv[1]);
  in>>SIZE;
  for(int i=1; i<=SIZE; i++){
    in>>N;
    in>>S;
    in>>p;
    int* scores = new int[sizeof(int)*N];
    for(int j=0; j<N; j++)
      in>>scores[j];
    printf("Case #%d: %d\n", i, get_max_players(S,p,scores, N));
    delete [] scores;
  }     
}

int get_max_players(int S, int p, int* scores, int size){
  int count = 0;
  int min = p*3-2;
  int max = p*3; 
  for(int i=0; i<size; i++){
    if(scores[i] == 0 && p!=0)
      continue;
    if(scores[i]>= min)
      count++;
    else if(scores[i] >= min-2 && S>0){
      count++;
      S--;
    }
  }
  return count;
}
