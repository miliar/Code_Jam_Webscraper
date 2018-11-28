#include <string>
#include <vector>
#include <set>
#include <algorithm>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

unsigned int sum(vector<int>& d)
{
  unsigned int sum = 0; 
  for(int i = 0; i < d.size(); i++){
    sum += d[i];
  }
  return sum;
}

int xorsum(vector<int>& p){
  int sum = p[0];
  for(int i = 1; i < p.size(); i++){
    sum ^= p[i];
  }
  return sum;
}

int main()
{
  FILE* fin = fopen("small.in","r");
  FILE* fout = fopen("small.out","w");

  int t;
  fscanf(fin, "%d\n", &t);
  for(int j = 0; j < t; j++){  
    int n;
    fscanf(fin, "%d\n", &n);
    vector<int> list;
    vector<int> pile1;
    vector<int> pile2;
    for(int i = 0; i < n; i++){
      int v;
      fscanf(fin, "%d ", &v);
      list.push_back(v);
    }
    pile1.push_back(list[0]);
    int index = 1;
    vector<int> dicision;
    for(int i = 0; i < n -1; i++){
      dicision.push_back(0);
    }

    unsigned int result = 0;
    bool isSet = false;

    while(sum(dicision) != dicision.size()){
      //divide as dicision
      for(int i = 0; i < dicision.size(); i++){
	if(dicision[i] == 0){
	  pile2.push_back(list[i+1]);
	}else{
	  pile1.push_back(list[i+1]);
	}
      }

      //calc each side
      unsigned int sum1 = sum(pile1);
      unsigned int sum2 = sum(pile2);
      if(xorsum(pile1) == xorsum(pile2)){
	sum1 = sum1>sum2?sum1:sum2;
	result = result>sum1?result:sum1;
	isSet = true;
      }

      //change dicision
      for(int i = 0; i < dicision.size(); i++){
	if(dicision[i] == 0){
	  dicision[i] = 1;
	  break;
	}else{
	  dicision[i] = 0;
	}
      }

      pile1.clear();
      pile2.clear();
      pile1.push_back(list[0]);
    }   

    if(isSet)
      fprintf(fout, "Case #%d: %d\n", j+1, result); 
    else
      fprintf(fout, "Case #%d: NO\n", j+1);
  }

  fclose(fin);
  fclose(fout);

  return 0;
}
