#include <stdio.h>


int main(){
int cases;
int a,b,n,e,k,l,m,q;
int counter;
int i,j;
int num[7],num1[7];
int out;
int reserve[7];
FILE *input;
FILE *output;
input = fopen("C-small-attempt0.in","r");
output = fopen("output1.txt", "w");
fscanf(input, "%d", &cases);
for(i=0;i<cases;i++){
	counter=0;
	fscanf(input, "%d %d", &a, &b);
	for(n=a;n<b+1;n++){
		num[0]=n%10;
		j=1;
		if(n>9){
			num[1]=(n%100-num[0])/10;
			j++;
			if(n>99){
				num[2]=(n%1000-num[1]*10)/100;
				j++;
				if(n>999){
					num[3]=(n%10000-num[2]*100)/1000;
					j++;
					if(n>9999){
						num[4]=(n%100000-num[3]*1000)/10000;
						j++;
						if(n>99999){
							num[5]=(n%1000000-num[4]*10000)/100000;
							j++;
							if(n>999999){
								num[6]=(n%10000000-num[5]*100000)/1000000;
								j++;
							}
						}
					}
				}
			}
		}
		q=0;
		for(k=0;k<j;k++){
			
			out=0;
			e=1;
			for(l=0;l<j;l++){
				num1[l]=num[(k+l)%j];
			}
			for(m=0;m<j;m++){
				out=out+num1[m]*e;
				e=e*10;
			}
			if(out<=b && out>n && out>=a){
				reserve[q]=out;
				counter++;
				q++;
			}
			/*for(m=q-2;m>-1;m--){
				if(reserve[m]==reserve[q-1]){
					counter--;
				}
			}*/
		}
		for(m=0;m<q;m++){
			for(k=m+1;k<q;k++){
				if(reserve[k]==reserve[m]){
					counter--;
				}
			}
		}
		
	}
		fprintf(output,"Case #%d: %d\n",i+1,counter);
}




//fprintf(output, "%d %d %d %d", cases,number,sup,points);
fclose(input);
fclose(output);

	return 0;
}