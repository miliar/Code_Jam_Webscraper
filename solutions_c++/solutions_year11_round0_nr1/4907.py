#include<stdio.h>
#include<math.h>
#define maxn 110
FILE *fr = fopen("INPUT.TXT","r"),*fw = fopen("OUTPUT.TXT","w");

bool ord[maxn];
int sol,Odata[maxn],Bdata[maxn],Oc,Bc,On,Bn;

void in(){
	char k;
	int i,n;

	fscanf(fr,"%d",&n);

	for( i = 0 ; i < n ; ++ i ){

		fscanf(fr," %c",&k);

		if( k == 'O' ){
			fscanf(fr,"%d",&Odata[Oc++]);
			ord[i] = 0;
		}
		else{
			fscanf(fr,"%d",&Bdata[Bc++]);
			ord[i] = 1;
		}
	}

	On = Oc;
	Bn = Bc;
}

void ch( int a , int &b , int c , int &d ){

	if( a == b ){

		++ sol;

		if( c < d ){
			-- d;
		}
		else if( c > d ){
			++ d;
		}
	}
	else{

		sol += abs( a - b ) + 1;

		if( abs( a - b ) + 1 > abs( c - d ) ){
			d = c;
		}
		else{

			if( c < d ){
				d -= abs( a - b ) + 1 ;
			}
			else{
				d += abs( a - b ) + 1 ;
			}
		}

		b = a;
	}
}

void pro(){
	int i,Ox = 1,Bx = 1;
	Oc = Bc = 0;

	for( i = 0 ; i < On + Bn ; ++ i ){

		if( ord[i] == 0 ){
			ch( Odata[Oc] , Ox , Bdata[Bc] , Bx );
			++ Oc;
		}
		else{
			ch( Bdata[Bc] , Bx , Odata[Oc] , Ox );
			++ Bc;
		}
	}
}

void out( int i ){
	fprintf(fw,"Case #%d: %d\n",i,sol);
}

int main(void){
	int i,t;

	fscanf(fr,"%d",&t);

	for( i = 0 ; i < t ; ++ i ){
		sol = Oc = Bc = 0;

		in();
		pro();
		out(i+1);
	}

	return 0;
}