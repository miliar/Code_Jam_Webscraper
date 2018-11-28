#include <stdio.h>
#include <math.h>

long int t[2000000],j,n,a,b,rs;
FILE *fi,*fo;

int len(long int k){
	int x=0;
	while (k>0){
		x++;k/=10;
	}
	return x;
}

void work(long int k){
	long int aux,tab[10],p=0,ii;
	for (ii=0; ii<10; ii++) tab[ii]=0;
	int control=1;
	t[k]=1;
	for (int i=1; i<len(k); i++){	
		aux=((k % int(pow(10,i)))*int(pow(10,len(k)-i))+k/int(pow(10,i)));
		if (k/int(pow(10,i-1)) % 10 !=0 && aux>=a && aux <= b && aux > k && t[aux]==0) {
			for (ii=0; ii<p; ii++)
				if (tab[ii]==aux) {control=0; break;}
			if (control){	
				rs++;
				tab[p]=aux; p++;
			}
		}
	}
}

void zero(){
	for (long int i=a; i<=b; i++) t[i]=0;
}

int main(){
	
	fi=fopen("C-large.in","r"); fo=fopen("output.out","w");
	
	fscanf(fi,"%ld",&n);
	
	for (int i=1; i<=n; i++){
		rs=0;
		zero();
		fscanf(fi,"%ld%ld",&a,&b);
		for (j=a; j<=b; j++){
			work(j);
		}
		fprintf(fo,"Case #%d: %ld\n",i,rs);
	}
	
	fclose(fi); fclose(fo); return 0;
}
