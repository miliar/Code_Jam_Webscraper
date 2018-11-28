#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>

using namespace std;

int main(){
  int t,k;
  char c,map[26], pal[200];
   
  map[0] = 'y';
  map[1] = 'h';
  map[2] = 'e';
  map[3] = 's';
  map[4] = 'o';
  map[5] = 'c';
  map[6] = 'v';
  map[7] = 'x';
  map[8] = 'd';
  map[9] = 'u';
  map[10] = 'i';
  map[11] = 'g';
  map[12] = 'l';
  map[13] = 'b';
  map[14] = 'k';
  map[15] = 'r';
  map[16] = 'z';
  map[17] = 't';
  map[18] = 'n';
  map[19] = 'w';
  map[20] = 'j';
  map[21] = 'p';
  map[22] = 'f';
  map[23] = 'm';
  map[24] = 'a';
  map[25] = 'q';
  
  scanf("%d ", &t);  
  
  for(int j=0;j<t;j++){
    int i = 0;
    do{
      c = getchar();
      if(c == ' '){
	pal[i++] = ' ';
	continue;
      }
      k = c - 97;
      pal[i++] = map[k]; 
    }while(c != '\n');
    printf("Case #%d: %s\n",j+1,pal);
  }
}