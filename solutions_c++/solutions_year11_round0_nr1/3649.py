#include <cstdio>
#include <cmath>
using namespace std;

int test;

int main(){
  int k,last0,last1,p0,p1,p,now;
  char ch;
  FILE* f;
  f = fopen("out.txt","w");
  scanf("%d",&test);

  for(int i = 0;i<test;i++){
    scanf("%d ",&k);
    last0 = last1 = now = 0;
    p0 = p1 = 1;
    for(int j = 0;j<k ;j++){
      scanf("%c %d",&ch,&p);
      if(j != k -1) scanf(" ");
      if(ch == 'O'){
	if(fabs(p - p0)  > now - last0){
	  now = last0 + fabs(p-p0);
	}; 
	now++;
	last0 = now;
	p0 = p;
      } else if (ch == 'B'){
	if(fabs(p-p1)> now-last1){
	  now = last1+fabs(p-p1);
	};
	now++;
	last1 = now;
	p1 =p;
      };
    };
    fprintf(f,"Case #%d: %d\n",i+1,now);
  };
  return 0;
};
