#include <stdio.h> 

int main(){
	FILE *fp;
	char fileName[] = "A-small-attempt3.in",outputfileName[]="A-small-attempt0.out";
	int i,j,inc,t,k,status[1001];
	char a[4],b[4],c,d,win;
	if((fp=fopen(fileName, "r")) == NULL){
		printf("Can't read file");
		return -1;
   }

	fscanf(fp, "%d ",&t);
for(k=1;k<=t;++k){
	win=0;inc=0;
	for(i=0;i<4;++i){
		fscanf(fp, " %c %c %c %c", &a[0], &a[1], &a[2], &a[3]);
		//printf(" %c %c %c %c", a[0], a[1], a[2], a[3]);
	if(win == 0){
		if( (a[0] != '.') && (a[1]==a[0] || a[1]=='T') && (a[2]==a[0]  || a[2]=='T') && (a[3]==a[0] || a[3]=='T') ){
				win = a[0];
		}
	}
	//printf(" %c %c %c %c %d", a[0], a[1], a[2], a[3], win);
	if(win == 0){
		if(i==0){
			for(j=0;j<4;++j){
				b[j] = a[j];
				if(a[j] == '.'){
					inc=1;
				}
			}
			c=a[0];
			d=a[3];
		}else{
			for(j=0;j<4;++j){
				if(a[j] == '.'){
					inc=1;
				}
				if(b[j] != 0){
					if(b[j] == 'T'){
						b[j] = a[j];
					}else if(b[j] != a[j] && a[j] != 'T'){
						b[j] = 0;
					}
				}
				
				if(j==i){
					if(c == 'T'){
						c = a[j];
					}else if(c != a[j] && a[j] != 'T'){
						c = 0;
					}
				}
				if(j==(3-i)){
					if(d == 'T'){
						d = a[j];
					}else if(d != a[j] && a[j] != 'T'){
						d = 0;
					}
				}
			}
		}
		//printf(" %c %c %c %c", b[0], b[1], b[2], b[3]);
	}
	}
	if(win == 0){
		for(j=0;j<4;++j){
			if(b[j]!=0 && b[j] != '.'){
				win = b[j];break;	
			}
		}
		if(d != 0 && d!='.'){
			win = d;
		}else if(c != 0 && c!='.'){
			win = c;
		}
	}
	if(win == 'X'){
		//printf("Case #%d: %c won", k, win);
		status[k] = 1;
	}else if(win == 'O'){
		//printf("Case #%d: %c won", k, win);
		status[k] = 2;
	}else if(inc == 0){
		//printf("Case #%d: Draw", k);
		status[k] = 3;
	}else{
	    //printf("Case #%d: Game has not completed", k);
		status[k] = 4;
	}
}
fclose(fp);

	if((fp=fopen(outputfileName, "w")) == NULL){
		printf("Can't write file");
		return -1;
    }

for(k=1;k<=t;++k){
	if(status[k] == 1){
		fprintf(fp,"Case #%d: X won\n", k);
	}else if(status[k] == 2){
		fprintf(fp,"Case #%d: O won\n", k);
	}else if(status[k] == 3){
		fprintf(fp,"Case #%d: Draw\n", k);
	}else if(status[k] == 4){
		fprintf(fp,"Case #%d: Game has not completed\n", k);
	}
}
	fclose(fp);
	return 1;
}
