#include <stdio.h>
#include <stdlib.h>

FILE *fi= fopen("A-large.in","r");
FILE *fo= fopen("A-large.out","w");	


int main(){


int i,j,t,o=0,x=0,k,draw=0,p=0,l;
char a[20];
	fscanf(fi,"%d\n",&t);

	for(j=1;j<=t;j++){
		p=0;
		for(i=0;i<16;i++){
			if(i%4==0)
				fscanf(fi,"\n");
			fscanf(fi,"%c",&a[i]);}
		o=0;
		x=0;
		draw=0;
		for(k=0;k<=15;k+=5){
			if(a[k]=='.')
				draw++;
			if(a[k]=='O')
				o++;
			if(a[k]=='X')
				x++;
			if(a[k]=='T'){
				o++;
				x++;
			}
			
			if(o==4){
				fprintf(fo,"Case #%d: O won\n",j);
				p=1;
			}
			if(x==4){
				fprintf(fo,"Case #%d: X won\n",j);
				p=1;
			}
		}
		o=0;
		x=0;
		for(k=3;k<=12;k+=3){
			if(a[k]=='.')
				draw++;
			if(a[k]=='O')
				o++;
			if(a[k]=='X')
				x++;
			if(a[k]=='T'){
				o++;
				x++;
			}
			
			if(o==4){
				fprintf(fo,"Case #%d: O won\n",j);
				p=1;
			}
			if(x==4){
				fprintf(fo,"Case #%d: X won\n",j);
				p=1;
			}
		}
		o=0;
		x=0;
		for(l=0;l<=3;l++){
			o=0;
			x=0;
		for(k=0;k<=3&&p==0;k++){
			if(a[k+4*l]=='.')
			draw++;
			if(a[k+4*l]=='O')
			o++;
			if(a[k+4*l]=='X')
			x++;
			if(a[k+4*l]=='T'){
				o++;
				x++;
				
			}
			
			if(o==4){
				fprintf(fo,"Case #%d: O won\n",j);
				p=1;
			}
			if(x==4){
				fprintf(fo,"Case #%d: X won\n",j);
				p=1;
			}
		}
		}

		
		for(l=0;l<=3;l++){
			o=0;
			x=0;
		for(k=0;k<=15&&p==0;k+=4){
			if(a[k+l]=='.')
			draw++;
			if(a[k+l]=='O')
			o++;
			if(a[k+l]=='X')
			x++;
			if(a[k+l]=='T'){
				o++;
				x++;
				
			}
			
			if(o==4){
				fprintf(fo,"Case #%d: O won\n",j);
				p=1;
			}
			if(x==4){
				fprintf(fo,"Case #%d: X won\n",j);
				p=1;
			}
		}
		}
		if(p==0&&draw==0){
			fprintf(fo,"Case #%d: Draw\n",j);
			p=1;}
			
		else if(p==0)
			fprintf(fo,"Case #%d: Game has not completed\n",j);
				

		fscanf(fi,"\n");
	
	}
	
//system("pause");
return 0;
}