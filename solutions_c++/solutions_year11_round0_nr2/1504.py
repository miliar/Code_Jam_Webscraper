#include<stdio.h>

int c,d,n;
char cTable[30][30];
char oTable[30][30];
char word[100];

int main(void){
	int T;
	char x,y,z;
	FILE *fin=fopen("input.txt","r");
	FILE *fout=fopen("output.txt","w");
	fscanf(fin,"%d",&T);
	for(int i=0;i<T;i++){
		for(int j=0;j<30;j++){
			for(int l=0;l<30;l++){
				cTable[j][l] = NULL;
				oTable[j][l] = NULL;
			}
		}

		fscanf(fin,"%d ",&c);
		for(int j=0;j<c;j++){
			fscanf(fin,"%c%c%c ",&x,&y,&z);
			cTable[x - 'A'][y - 'A'] = z;
			cTable[y - 'A'][x - 'A'] = z;
		}
		fscanf(fin,"%d ",&d);
		for(int j=0;j<d;j++){
			fscanf(fin,"%c%c ",&x,&y);
			oTable[x - 'A'][y - 'A'] = '-';
			oTable[y - 'A'][x - 'A'] = '-';
		}
		fscanf(fin,"%d",&n);
		fscanf(fin,"%s",word);

		char ans[100];
		int len = 0;
		for(int j=0;j<n;j++){
			if(len == 0){
				ans[len++] = word[j];
			} else{
				if( cTable[word[j] - 'A'][ans[len-1] - 'A'] >= 'A' && cTable[word[j] - 'A'][ans[len-1] - 'A'] <= 'Z' ){
					ans[len-1] = cTable[word[j] - 'A'][ans[len-1] - 'A'];
				} else if( cTable[ans[len-1] - 'A'][word[j] - 'A'] >= 'A' && cTable[ans[len-1] - 'A'][word[j] - 'A'] <= 'Z' ){
					ans[len-1] = cTable[ans[len-1] - 'A'][word[j] - 'A'];
				} else{
					for(int l=0;l<len;l++){
						if( oTable[word[j] - 'A'][ans[l] - 'A'] == '-' || oTable[ans[l] - 'A'][word[j] - 'A'] == '-' ){
							len = 0;
						}
					}
					if(len != 0){
						ans[len++] = word[j];
					}
				}
			}
		}
		fprintf(fout,"Case #%d: [",i+1);
		for(int j=0;j<len;j++){
			if(j == 0) fprintf(fout,"%c",ans[j]);
			else fprintf(fout,", %c",ans[j]);
		}
		fprintf(fout,"]\n");
	}
	fcloseall();
	return 0;
}