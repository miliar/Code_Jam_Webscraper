#include <stdio.h>


int main(void){
	int n;
        scanf("%d",&n);
	int i =0;
        while(n--){
		int m;
		scanf("%d",&m);
		int B=0,O=0,lB=1,lO=1;
		i++;
		while(m--){
			char source;
			int pos;
			scanf(" %c %d",&source,&pos);
			if (source == 'B'){
				B += (lB>pos)?lB-pos:pos-lB;
				lB = pos;
				B = (B<=O)?O+1:B+1;
			}
			else{
				O += (lO>pos)?lO-pos:pos-lO;
				lO = pos;
				O = (O<=B)?B+1:O+1;
			}
		}
		printf("Case #%d: %d\n",i,((O>B)?O:B));
        }

}
