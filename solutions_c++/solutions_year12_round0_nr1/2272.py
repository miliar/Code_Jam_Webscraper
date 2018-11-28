#include <cstdio>
#include <iostream>

int main() {
  int tests;
  char sub[255];
  //for(int i=97; i<=122; i++) printf("%d - %c\n", i, char(i));
  for(int i=0; i<255; i++) sub[i] = char(i);
  sub[97] = 'y'; //a
  sub[98] = 'h'; //b
  sub[99] = 'e'; //c
  sub[100] = 's'; //d
  sub[101] = 'o'; //e
  sub[102] = 'c'; //f
  sub[103] = 'v'; //g
  sub[104] = 'x'; //h
  sub[105] = 'd'; //i
  sub[106] = 'u'; //j
  sub[107] = 'i'; //k
  sub[108] = 'g'; //l
  sub[109] = 'l'; //m
  sub[110] = 'b'; //n
  sub[111] = 'k'; //o
  sub[112] = 'r'; //p
  sub[113] = 'z'; //q ??
  sub[114] = 't'; //r
  sub[115] = 'n'; //s
  sub[116] = 'w'; //t
  sub[117] = 'j'; //u
  sub[118] = 'p'; //v
  sub[119] = 'f'; //w
  sub[120] = 'm'; //x
  sub[121] = 'a'; //y
  sub[122] = 'q'; //z
  std::string data;
  scanf("%d\n", &tests);
  for(int z=0; z < tests; z++) {
    std::getline(std::cin, data);
    for(int i=0; i<data.size(); i++) data[i] = sub[int(data[i])];
    std::cout << "Case #" << z+1 << ": " << data << "\n";
  }
}
