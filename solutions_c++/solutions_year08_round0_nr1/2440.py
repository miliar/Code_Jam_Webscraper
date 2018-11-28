#include <limits>
#include <iostream>
#include <map>
#include <string>
using namespace std;

const int Max_SString=103;


char sea[1002][Max_SString];

int univ() {
  int se=0; 			// search engines 
  map<string, int> smap;

  scanf("%d\n", &se);

  for (int i=0; i<se; i++) {
    fgets(sea[i], Max_SString, stdin);
    sea[i][strlen(sea[i])-1]='\0';
    smap[string(sea[i])]=0;
  }

  int ss, swth=0, cnt=0;
  scanf("%d\n", &ss);
  if (ss==0) return swth;
  for (int i=0; i<ss; i++) {
    fgets(sea[i], Max_SString, stdin);
    sea[i][strlen(sea[i])-1]='\0';
    if (smap[string(sea[i])] == 0) {
      smap[string(sea[i])] = 1;
      cnt++;
    }
    if (cnt == se) {
      swth+=1;
      cnt=0;
      map<string, int>::iterator it;
      for (it=smap.begin(); it!=smap.end(); it++)
	(*it).second = 0;
      smap[string(sea[i])] = 1;
      cnt=1;
    }
  }
  return swth;
}

int main() {
  int cnt;
  scanf("%d\n", &cnt);
  for (int i=0; i<cnt; i++) {
    printf("Case #%d: %d\n", i+1, univ());
  }
  
  return 0;
}
