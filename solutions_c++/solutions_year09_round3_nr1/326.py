#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

unsigned long long convert(short *tab, int len, short base){
	unsigned long long result = 0;
	unsigned long long pow = 1;
	for(int i = len - 1; i >= 0; --i){
		result += tab[i]*pow;
		pow *= base;
	}
	return result;
}

int main(){
  int C;
  scanf("%d", &C);
  char buf[100];
  short num[100];
  for(int c = 1; c <= C; ++c){
	scanf("%s", buf);
//	if(strlen(buf) == 1){
//		printf("%s\n", buf);
//		printf("Case #%d: 0\n", c);
//		continue;
//	}
	map<char, short> symbol_map;
	short current_digit = 1;
	for(int i = 0; i < strlen(buf); ++i){
		if(symbol_map.find(buf[i]) == symbol_map.end()){
			symbol_map[buf[i]] = current_digit;
			if(current_digit == 1)
				current_digit = 0;
			else if(current_digit == 0)
				current_digit = 2;
			else
				++current_digit;
		}
		num[i] = symbol_map[buf[i]];
	}
//	printf("%s\n", buf);
//	for(int i = 0; i < strlen(buf); ++i)
//		printf("%hd ", num[i]);
//	printf("()\n");
    printf("Case #%d: %lld\n", c, convert(num, strlen(buf), current_digit == 0 ? 2: current_digit));
  }
  return 0;
}
