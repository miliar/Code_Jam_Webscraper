#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){

	int cc[11][31];
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int T,L,P,C,i,j,k,x;	
	int max[11];
	max[2]=30;
	max[3]=19;
	max[4]=15;
	max[5]=13;
	max[6]=12;
	max[7]=11;
	max[8]=10;
	max[9]=10;
	max[10]=9;


	for (i = 2;i<11;i++){
		cc[i][0] = 1;
	}
	for (j=1;j<31;j++) {
		for (i = 2;i<11;i++){
			if(cc[i][j-1] > 1000000000)
				continue;
			cc[i][j] = cc[i][j-1]*i;
		}
	}
	in>>T;
	for (i=0;i<T;i++){
		in>>L>>P>>C;
		x = P/L;
		if (P%L > 0)
			x++;
		for(j=0;j<max[C];j++){
			if (x<=cc[C][j])
				break;
		}
		for(k=0;k<max[2];k++){
			if (j<=cc[2][k])
				break;
		}	

		out<<"Case #"<<i+1<<": "<<k<<endl;		
	}

}