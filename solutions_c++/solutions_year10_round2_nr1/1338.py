#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;


typedef struct No_t No;
struct No_t {	
	int num;
	char s[101];
	No *v;
};

No ar;

int main(void)
{
	int teste=1, T, n, m,i, ndir,j,k;
	char aux[102], aux2[101]; 
	No *no = &ar;
		
	scanf("%d",&T);
	for(teste=1;teste<=T;teste++){
		scanf("%d %d ",&n,&m);
		memset(&ar,0,sizeof(&ar));
		while(n--){
			scanf("%s",aux);
			no = &ar; j = 0;
			for(i=1;aux[i]!=0;i++) {
				if(aux[i]=='/') {
					aux2[j] = 0;
					for(k=0;k<no->num;k++) if(strcmp(no->v[k].s,aux2)==0) break;
					if(k==no->num) {
						if(no->num == 0) no->v = (No*)calloc(101,101*sizeof(No));
						strcpy(no->v[no->num++].s,aux2);
					}
					no = &no->v[k]; j = 0;
				}else{
					aux2[j++] = aux[i];
				}
			}
			aux2[j] = 0;
			for(k=0;k<no->num;k++) if(strcmp(no->v[k].s,aux2)==0) break;
			if(no->num == 0) no->v = (No*)calloc(101,101*sizeof(No));
			if(k==no->num) strcpy(no->v[no->num++].s,aux2);
		}
		
		ndir = 0;
		while(m--){
			scanf("%s",aux);
			no = &ar; j = 0;
			for(i=1;aux[i]!=0;i++) {
				if(aux[i]=='/') {
					aux2[j] = 0;
					for(k=0;k<no->num;k++) if(strcmp(no->v[k].s,aux2)==0) break;
					if(k==no->num){
						if(no->num == 0) no->v = (No*)calloc(101,101*sizeof(No));
						strcpy(no->v[no->num++].s,aux2);
						ndir++;
					}
					no = &no->v[k]; j = 0;
				}else{
					aux2[j++] = aux[i];
				}
			}
			aux2[j] = 0;
			for(k=0;k<no->num;k++) if(strcmp(no->v[k].s,aux2)==0) break;
			if(no->num == 0) no->v = (No*)	calloc(101,101*sizeof(No));
			if(k==no->num){
				strcpy(no->v[no->num++].s,aux2);
				ndir++;
			}
		}
		
		printf("Case #%d: %d\n",teste ,ndir);
	}
	
	return 0;
}