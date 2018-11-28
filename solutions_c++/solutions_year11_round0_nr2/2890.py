#include<iostream>
#include<fstream>
using namespace std;
int key(char a)
{
	return a - 'A';
}
int main()
{
	ifstream fin("date.txt");
	ofstream fout("out.out");
	char a[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};
	char aux[500],echiv[41][6],oppos[41][41],aaa,bbb;
	int n,test,d,i,k,j,fr[50],c,noppos[41],naux;
	fin>>test;
	for(k = 1; k <= test; k++) {
		naux = 0;
		memset(fr,0,sizeof(int[45]));
		memset(noppos,0,sizeof(int[39]));
		fin>>c;
		for(i = 0; i < c; i++) {
			fin>>echiv[i][0]>>echiv[i][1]>>echiv[i][2];
		}
		fin>>d;
		for(i = 0; i < d; i++) {
			fin>>aaa>>bbb;
			oppos[key(aaa)][noppos[key(aaa)]++] = bbb;
			oppos[key(bbb)][noppos[key(bbb)]++] = aaa;
		}
		fin>>n;
		for(i = 0 ; i < n; i++) {
			fin>>aux[naux++];
			fr[key(aux[naux - 1])]++;
			for(j = 0; j < c; j++) {
				if(echiv[j][0] == aux[naux-1] && echiv[j][1] == aux[naux-2]) {
					fr[key(aux[naux-1])]--;
					fr[key(aux[naux-2])]--;
					aux[naux-2] = echiv[j][2];
					naux = naux - 1;
					goto forend;
				}
				if(echiv[j][0] == aux[naux-2] && echiv[j][1] == aux[naux-1]) {
					fr[key(aux[naux-1])]--;
					fr[key(aux[naux-2])]--;
					aux[naux-2] = echiv[j][2];
					naux = naux - 1;
					goto forend;
				}
			}
			for(j = 0; j < noppos[key(aux[naux - 1])]; j++) {
				if( fr[key(oppos[key(aux[naux - 1])][j])] > 0 ) {
					naux = 0;
					memset(fr,0,sizeof(int[45]));
					goto forend;
				}
			}
			forend:;
		}
		fout<<"Case #"<<k<<": [";
		for(i = 0; i < naux - 1; i++) {
			fout<<aux[i]<<", ";
		}
		if(i == naux - 1)
			fout<<aux[i];
		fout<<"]\n";
	}
}