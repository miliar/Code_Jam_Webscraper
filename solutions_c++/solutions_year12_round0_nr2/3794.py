#include <stdio.h>
#include <string.h>
#include<ctype.h>


int main(int argc, char** args){
	FILE *out;
	int t[100][150];
	int i=0;
	int	j=0;
	int x=0;
	int jb=0,n=0;
	int a,b,c;
	scanf("%d", &argc);
	fflush(stdin);
	out = fopen("f.out", "w");
	while(j<argc){
		x=3;
		scanf("%d", &t[j][0]);	
		scanf("%d", &t[j][1]);
		scanf("%d", &t[j][2]);
		for(i=0; i<t[j][0]; i++){
			scanf("%d", &t[j][x+i]);
		}
		j++;
	}
	
	for(i=0; i<argc; i++){
		jb=0;
		for(j=0; j<t[i][0]; j++){
			//if(t[i][1]>0){
			if(t[i][1]>0){
				for(a=3; a<=4; a++){
					if(t[i][2]*3-a==t[i][j+3] && t[i][2]*2>2 ){
						t[i][j+3]=0;
						jb++;
						t[i][1]--;
						break;
					}
				}
			}
		}
		
		for(j=0; j<t[i][0]; j++){
			//if(t[i][1]>0){
			for(a=1; a<=2; a++){
				if(t[i][2]*3-a==t[i][j+3]){
					t[i][j+3]=0;
					jb++;
					break;
				}
			}
		}

		
		for(j=0; j<t[i][0]; j++){
			if(t[i][2]*3==t[i][j+3] || t[i][2]*3<t[i][j+3]){
				t[i][j+3]=0;
				jb++;
			}
		}
		
		printf("Case #%d: %d\n", i+1,jb);
		fprintf(out,"Case #%d: %d\n", i+1,jb);
		//printf("\nCase #%d: %d %d %d\n", i+1,t[i][0],t[i][1],t[i][2]);
		//for(j=0; j<t[i][0]; j++){
		//	printf("%d ", t[i][j+3]);
		//}
	}


	
	fflush(stdin);
	getchar();
	fclose(out);
	return 0;
}