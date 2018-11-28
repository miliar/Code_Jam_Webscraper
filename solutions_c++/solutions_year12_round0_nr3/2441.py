#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream>
#include<iostream>

using namespace std;

int SIZE = 0;
int get_recycles(int, int);
int main(int argc, char** argv){
  if(argc != 2){
    cerr<<"Invalid input provided"<<endl;
    return -1;
  }
  int min, max;
  ifstream in(argv[1]);
  in>>SIZE;
  for(int i=1; i<=SIZE; i++){
    in>>min;
    in>>max;
    printf("Case #%d: %d\n", i, get_recycles(min, max));
  }     
}

int get_recycles(int min, int max){
  int m, n=min, count =0;
  char num[8*8+1];
  while(min <= n && n <= max){
    sprintf(num, "%d", n);
    //    printf("The string is: %s and it has length: %d\n", num, strlen(num));
    //Permute
    for(int j=0; j<strlen(num)-1; j++){
      char first = num[0];
      for(int i=1; i<strlen(num);i++)
	num[i-1] = num[i];
      num[strlen(num)-1] = first;
      m = atoi(num);
      //      printf("m is %d and num is %s at %d\n", m, num, j);
      if(m == n)
	break;
      if(m <= max && m >= min)
	count++;
    }
    n++;
  }
  return count/2;
}
