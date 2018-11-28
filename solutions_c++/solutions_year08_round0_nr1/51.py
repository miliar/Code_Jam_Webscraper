#ifndef V_UTILITIES_H_
#define V_UTILITIES_H_

#include <string>
#include <vector>

#ifndef max
#define max(a,b) (((a) > (b))? (a) : (b))
#define min(a,b) (((a) < (b))? (a) : (b))
#endif


int powInt(int base,int pow);

int IsStringConsistOf(char* string ,char c);

int IsStringConsistOfAndSplit(char* string ,char c,int &num);

int findEOS(char* string,int max);

int CNR(int num,int den);

void StringSplit(std::string *s,char token,std::vector<std::string> *list);

template <class myType>
void printFunction (myType i) {
  cout << i << " ";
}


#endif