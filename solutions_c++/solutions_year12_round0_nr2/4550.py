#include <stdio.h>
#include <stdlib.h>

int main(void){
	int num, ppl, s, p;
	int s_count, p_count;
	int array;
	//	int array[110];
	scanf("%d", &num);
	for(int i=0; i<num; i++){
		s_count = 0;
		p_count = 0;
		scanf("%d", &ppl);
		scanf("%d %d", &s, &p);
		//printf("-%d %d %d\n", ppl, s, p);
		for(int j=0; j<ppl; j++){
			scanf("%d", &array);
			//printf("--num:%d s_count:%d p_count:%d\n", array, s_count, p_count);
			if( ((3*p-2) > array) && (array>=(3*p-4))){
				if(((p!=0)&&(array!=0)) || (p == 0)){
					if((s_count < s)){
						s_count += 1;
						p_count += 1;
						//printf("---in suprise\n");
					}
				}
			}else if(array >= (3*p - 2)){
				p_count +=1;
				//printf("---over the top\n");
			}
		}

		printf("Case #%d: %d\n", i+1, p_count);
	}

	return 0;
}
