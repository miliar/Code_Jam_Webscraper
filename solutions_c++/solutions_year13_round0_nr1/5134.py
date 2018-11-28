#include <fstream>
using namespace std;

ifstream fi("in.in");
ofstream fo("out.out");

char a[5][5]; long k,j,i,n;

void check(){
	long x1,x2,d1,d2;
	for (long i=1; i<5; i++){
		x1=x2=d1=d2=0;
		for (long j=1; j<5; j++){
			if (a[i][j]!='.') x1+=(int)a[i][j]; else x1++;
			if (a[j][i]!='.') x2+=(int)a[j][i]; else x2++;
			if (a[j][j]!='.') d1+=(int)a[j][j]; else d1++;
			if (a[j][5-j]!='.') d2+=(int)a[j][5-j]; else d2++;
		}
		//fo << x1 << " " << x2 << " " << d1 << " " << d2 << "\n";
		if (!(x1 % 79) || !((x1-84) % 79) || !(x2 % 79) || !((x2-84) % 79) || 
			!(d1 % 79) || !((d1-84) % 79) || !(d2 % 79) || !((d2-84) % 79)) {fo << "Case #" << (k-n) << ": O won\n"; return ;}
		if (!(x1 % 88) || !((x1-84) % 88) || !(x2 % 88) || !((x2-84) % 88) || 
			!(d1 % 88) || !((d1-84) % 88) || !(d2 % 88) || !((d2-84) % 88)) {fo << "Case #" << (k-n) << ": X won\n"; return ;}
	}
	for (long i=1; i<5; i++)for (long j=1; j<5; j++)if (a[i][j]=='.') {fo << "Case #" << (k-n) << ": Game has not completed\n"; return ;}
	fo << "Case #" << (k-n) << ": Draw\n";
}


int main(){
	
	// O-79; X-88; T:84; .:46;
	
	fi >> n;
	k=n;
	while (n--){
		for (i=1; i<5; i++)for (j=1; j<5; j++)fi >> a[i][j];
		check();
	}
	
	return 0;
}
