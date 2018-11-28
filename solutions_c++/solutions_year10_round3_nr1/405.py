#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]){
	int n[31];
	int i;
	n[0] = 1;	
	for (i = 1;i<31;i++){
		n[i] = n[i-1]*2;
	}
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int T,N,count,j,k;
	int line[1000][2];
	in>>T;
	for (i=0;i<T;i++){
		count = 0;
		in>>N;
		for (j=0;j<N;j++){
			in>>line[j][0]>>line[j][1];
		}
		for(j=0;j<N;j++){
			for(k=j+1;k<N;k++){
				if ((line[j][0]<line[k][0]) && (line[j][1]>line[k][1]))
					count++;
				else if ((line[j][0]>line[k][0]) && (line[j][1]<line[k][1]))
					count++;
			}
		}
		out<<"Case #"<<i+1<<": "<<count<<endl;		
	}

}