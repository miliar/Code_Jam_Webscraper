#include <cstdio>
using namespace std;
char combin[37][3];
char op[30][2];
char s[101];
int c,d,n,now;


int main(){
  int test;
  char ch;
  FILE* f;
  bool ok;

  f = fopen("out.txt","w");
  scanf("%d",&test);
  for(int i = 0;i<test;i++){
    scanf("%d ",&c);
    for(int j = 0;j<c;j++)
      scanf("%c%c%c ",&combin[j][0],&combin[j][1],&combin[j][2]);
    scanf("%d ",&d);
    for(int j =0 ;j<d;j++)
      scanf("%c%c ",&op[j][0],&op[j][1]);
    now = 0;
    scanf("%d ",&n);
    for(int j=0;j<n;j++){
      scanf("%c",&ch);
      s[now++] = ch;
      ok = false;
      while(now >=2 && !ok){
	ok = true;
	for(int k = 0;k<c;k++){
	  if(s[now - 2] == combin[k][0] && s[now-1] == combin[k][1] || s[now -2 ] == combin[k][1] && s[now-1] == combin[k][0]){
	    now--;
	    s[now-1] = combin[k][2];
	    ok =false;
	    break;
	  };
	};
	if(now>=2 && ok){
	  for(int k =0;k<d;k++){
	    if(s[now-1] == op[k][0]){
	      for(int l =0;l<now-1;l++){
		if(s[l] == op[k][1]){	        
                  now = 0;
	          ok = false;
	          break;
		};
	      };
	    };
	    if(!ok) break;
	    if(s[now-1] == op[k][1]){
	      for(int l =0;l<now-1;l++){
		if(s[l] == op[k][0]){	        
                  now = 0;
	          ok = false;
	          break;
		};
	      };
	    };
	    if(!ok) break;
	  };
	};
      };
    };
    fprintf(f,"Case #%d: [",i+1);
    for(int j = 0;j<now;j++){
      if(j== 0) fprintf(f,"%c",s[j]);
      else fprintf(f,", %c",s[j]);
    };
    fprintf(f,"]\n");
  };
  return 0;
};
