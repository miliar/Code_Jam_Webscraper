#include <iostream>
#include <cstring>
#include <cstdio>

const char *search = "welcome to code jam";

unsigned int rec(const char *where, const char *what) {
  if(!what[0]) return 1;

  const char *p = where;
  unsigned int sum = 0;
  
  while(p = strchr(p, what[0]))
    sum += rec(++p, what+1);

  return sum;
}

int main() {
  int cases;
  char buf[512];
  fgets(buf, 512, stdin);
  sscanf(buf, "%d", &cases);

  for(int i=0; i<cases; i++) {
    std::string sin;
    std::getline(std::cin, sin);
    
    printf("Case #%d: %0.4d\n", i+1, rec(sin.c_str(), search));
  }
}
