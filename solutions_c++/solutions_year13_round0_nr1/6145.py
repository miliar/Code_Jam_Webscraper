#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;



int main(){
	FILE *in = fopen("A.txt", "r");
	FILE *out = fopen("AA.txt", "w");
	int T;
	fscanf(in, "%d", &T);
	int rows[4];
	int columns[4];
	int d1;
	int d2;
	int Ti;
	int Tj;
	char c;
	int dots;
	for(int t=1;t<=T;t++){
		memset(rows, 0, sizeof(int)*4);
		memset(columns, 0, sizeof(int)*4);
		d1=d2=dots=0;
		
		for(int i=0;i<4;i++){
			fscanf(in, "%c", &c);
			for(int j=0;j<4;j++){
				fscanf(in, "%c", &c);
				if(c=='X'){
					rows[i]++;
					columns[j]++;
					if(i==j)d1++;
					if(i+j==3) d2++;
				}
				else if(c=='O'){
					rows[i]--;
					columns[j]--;
					if(i==j)d1--;
					if(i+j==3)d2--;
				}
				else if(c=='T'){
					Ti=i;
					Tj=j;
				}
				else{
					dots++;
				}
			}
		}
		bool found=false;
		for(int i=0;i<4&&!found;i++){
			if(rows[i]==4||(rows[i]==3&&Ti==i)){
				fprintf(out, "Case #%d: X won\n", t);
				found=true;
			}
			else if(rows[i]==-4||(rows[i]==-3&&Ti==i)){
				fprintf(out, "Case #%d: O won\n", t);
				found=true;
			}
			else if(columns[i]==4||(columns[i]==3&&Tj==i)){
				fprintf(out, "Case #%d: X won\n", t);
				found=true;
			}
			else if(columns[i]==-4||(columns[i]==-3&&Tj==i)){
				fprintf(out, "Case #%d: O won\n", t);
				found=true;
			}
			//printf("%d %d\n", rows[i], columns[i]);
		}
		//printf("\n%d %d\n\n", d1, d2);
		if(!found){
			if(d1==4||(d1==3&&Ti==Tj)){
				fprintf(out, "Case #%d: X won\n", t);
			}
			else if(d2==4||(d2==3&&(Ti+Tj==3))){
				fprintf(out, "Case #%d: X won\n", t);
			}
			else if(d1==-4||(d1==-3&&Ti==Tj)){
				fprintf(out, "Case #%d: O won\n", t);
			}
			else if(d2==-4||(d2==-3&&(Ti+Tj==3))){
				fprintf(out, "Case #%d: O won\n", t);
			}
			else if(dots==0){
				fprintf(out, "Case #%d: Draw\n", t);
			}
			else{
				fprintf(out, "Case #%d: Game has not completed\n", t);
			}
		}
		
		fscanf(in, "%c", &c);
	}
	
	return 0;
}