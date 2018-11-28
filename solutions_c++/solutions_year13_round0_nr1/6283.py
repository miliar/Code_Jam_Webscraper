#include <stdio.h>
#include <stdlib.h>

// s:
//   0 - not complete
//   1 - draw
//   2 - x won
//   3 - o won

inline short int v(char c){
	return c=='X'?1:(c=='O'?-1:(c=='T'?0:-100));
}


int main(void){
	unsigned short int T,i=0,j,s;
	short int *t;
	char dt[4];

	scanf("%d\n",&T);
	for(;i<T;i++){
		t = new short int[10]{0,0,0,0,0,0,0,0,0,0};
		for(j=0,s=1;j<4;j++){
			scanf("%c%c%c%c\n",&dt[0],&dt[1],&dt[2],&dt[3]);
			t[j]=v(dt[0])+v(dt[1])+v(dt[2])+v(dt[3]);
			t[4]+=v(dt[0]);t[5]+=v(dt[1]);
			t[6]+=v(dt[2]);t[7]+=v(dt[3]);
			t[8]+=v(dt[j]);t[9]+=v(dt[3-j]);
		}
		for(j=0;j<10;j++)
			if(abs(t[j])>2&&abs(t[j])<5) s=t[j]>0?2:3;
			else if(s==1&&abs(t[j])>5) s=0;
		printf("Case #%d: %s\n",i+1,s==0?"Game has not completed":(s==1?"Draw":(s==2?"X won":"O won")));
		delete[] t;
	}

}