#include <stdio.h>
#include <math.h>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
int n;
int data[202][2];
int ous;
void input()
{
	int i;
	char c[100];
	fscanf(fin,"%d",&n);
	for (i=0;i<n;i++){
		fscanf(fin,"%s %d",&c,&data[i][1]);
		if (c[0] == 'O' || c[0] == 'o'){
			data[i][0] = 1;
		}else{
			data[i][0] = 2;
		}
	}
}
void pro()
{
	int time,term;;
	int opos, bpos,i,j;
	time=0;
	opos=bpos = 1;
	for (i=0;i<n;i++){
		if (data[i][0] == 1){ // Orange
			if (opos != data[i][1]){
				term = abs(opos-data[i][1]) + 1;
				time += term;
				opos = data[i][1];
				for (j=i+1;j<n;j++){
					if (data[j][0] == 2){
						if (data[j][1] > bpos){
							if (abs(bpos-data[j][1]) >= term){
								bpos += term;
							}else{
								bpos = data[j][1];
							}
						}else if (data[j][1] < bpos){
							if (abs(bpos-data[j][1]) >= term){
								bpos -= term;
							}else{
								bpos = data[j][1];
							}
						
						}
						break;
					}
				}
			}else{ // same
				time ++;	
				for (j=i+1;j<n;j++){
					if (data[j][0] == 2){
						if (data[j][1] > bpos){
							bpos++;
						}else if (data[j][1] < bpos){
							bpos--;
						}
						break;
					}
				}
			}
		}else{ // Blue
			if (bpos != data[i][1]){
				term = abs(bpos-data[i][1]) + 1;
				time += term;
				bpos = data[i][1];
				for (j=i+1;j<n;j++){
					if (data[j][0] == 1){
						if (data[j][1] > opos){
							if (abs(opos-data[j][1]) >= term){
								opos += term;
							}else{
								opos = data[j][1];
							}
						}else if (data[j][1] < opos){
							if (abs(opos-data[j][1]) >= term){
								opos -= term;
							}else{
								opos = data[j][1];
							}
						}
						break;
					}
				}
			}else{
				time ++;	
				for (j=i+1;j<n;j++){
					if (data[j][0] == 1){
						if (data[j][1] > opos){
							opos++;
						}else if (data[j][1] < opos){
							opos--;
						}
						break;
					}
				}
			}
		}
	}
	ous = time;
}
int main()
{
	int t,i;
	fscanf(fin,"%d",&t);
	for (i=0;i<t;i++){
		input();
		pro();
		fprintf(fout,"Case #%d: %d\n",i+1,ous);
	}
	return 0;
}