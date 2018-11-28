#include "cstdio"


int tab[10000];

int gcd(int a, int b){  
	int c = a % b;  
	while(c != 0){   
		a = b;    
		b = c;    
		c = a % b;  
	}  
	return b;
}



int NWW(int a, int b){
	return (a*b)/gcd(a,b);
}



FILE *in=fopen("C-small-attempt0.in","r");
FILE *out=fopen("outsmall0","w");

int main(){

	int t;
	int N,L,H,j;
	bool flag;
	fscanf(in,"%d",&t);

	for(int k=1;k<=t;k++){
		flag=false;
		fscanf(in,"%d%d%d",&N,&L,&H);
		for(int i=0;i<N;i++)
			fscanf(in,"%d",&(tab[i]));

		if(L==1) fprintf(out,"Case #%d: 1\n",k);
		else{
			for(int i=L;i<=H;i++){
				for(j=0;j<N;j++){
					if(tab[j]%i!=0 && i%tab[j]!=0) break;
				}
				if(j==N){ 
					fprintf(out,"Case #%d: %d\n",k,i);
					flag=true;
				}
				if(flag) break;
			}
			if(flag==false)
			fprintf(out,"Case #%d: NO\n",k);
		}
	}

	return 0;
}