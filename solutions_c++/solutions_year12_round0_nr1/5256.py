#include<stdio.h>

int main(){
  char data[26];
  int n;
  int i;
  char c;
  data['a'-'a'] =  'y';
  data['b'-'a'] =  'h';
  data['c'-'a'] =  'e';
  data['d'-'a'] =  's';
  data['e'-'a'] =  'o';
  data['f'-'a'] =  'c';
  data['g'-'a'] =  'v';
  data['h'-'a'] =  'x';
  data['i'-'a'] =  'd';
  data['j'-'a'] =  'u';
  data['k'-'a'] =  'i';
  data['l'-'a'] =  'g';
  data['m'-'a'] =  'l';
  data['n'-'a'] =  'b';
  data['o'-'a'] =  'k';
  data['p'-'a'] =  'r';
  data['q'-'a'] =  'z';
  data['r'-'a'] =  't';
  data['s'-'a'] =  'n';
  data['t'-'a'] =  'w';
  data['u'-'a'] =  'j';
  data['v'-'a'] =  'p';
  data['w'-'a'] =  'f';
  data['x'-'a'] =  'm';
  data['y'-'a'] =  'a';
  data['z'-'a'] =  'q';
  scanf("%d\n", &n);
  for(i=0 ; i<n; i++){
    printf("Case #%d: ", i+1);
    while(1){
      scanf("%c", &c);
      if(c == '\n'){
	printf("\n");
	break;
      }else{
	if(c >= 'a' && c <= 'z'){
	  printf("%c", data[c-'a']);
	  //printf("%c", c);
	}else{
	  printf("%c", c);
	}
      }
    }
  }
  return 0;
}
