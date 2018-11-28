#include<iostream>
#include<fstream>

using namespace std;


char** rotate(char** matrica, int n) {
char** rotiranaMatrica;
int brojPraznihMesta;
	
	rotiranaMatrica=new char*[n];
	for(int k=0; k<n; k++) rotiranaMatrica[k]=new char[n];
	for(int i=0; i<n; i++) {
		
		brojPraznihMesta=0;
		for(int j=0; j<n; j++) {
			
			if(matrica[n-i-1][n-j-1]!='.') rotiranaMatrica[n-j+brojPraznihMesta-1][i]=matrica[n-i-1][n-j-1];
			else brojPraznihMesta++;
		}
		for(int k=0; k<brojPraznihMesta; k++) rotiranaMatrica[k][i]='.';
	}
	return rotiranaMatrica;
}

void ispisiMatricu(char** matrica, int n) {
	
	for(int i=0; i<n; i++) {
		for(int j=0; j<n; j++)
			cout<<matrica[i][j]<<' ';
		cout<<endl;
	}
}

bool proveriResenje(char** matrica, int x, int y, int n, int k) {
bool dobro=true;
int xx=x, yy=y, brojDobrih=0;

	while(true) {
		if(xx<0||yy<0) {
			dobro=false;
			break;
		}
		else if (matrica[xx][yy]==matrica[x][y]) {if (++brojDobrih==k) {dobro=true; break;}}
		else {dobro=false; break;}
		xx--;yy--;
	}
	xx=x;yy=y;
	brojDobrih=0;
	while(!dobro) {
		if(xx<0) {
			dobro=false;
			break;
		}
		else if (matrica[xx][yy]==matrica[x][y]) {if (++brojDobrih==k) {dobro=true; break;}}
		else {dobro=false; break;}
		xx--;
	}
	xx=x;yy=y;
	brojDobrih=0;
	while(!dobro) {
		if(yy<0) {
			dobro=false;
			break;
		}
		else if (matrica[xx][yy]==matrica[x][y]) {if (++brojDobrih==k) {dobro=true; break;}}
		else {dobro=false; break;}
		yy--;
	}
	return dobro;
}

int main() {
ifstream ulaz("ulaz.txt");
ofstream izlaz("output.txt");
int t, n, k;
char **matrica1, **matrica2;
bool red, blue;

	ulaz>>t;
	for(int i=1; i<=t; i++) {
		ulaz>>n>>k;
		
		matrica1=new char* [n];
		for(int j=0; j<n; j++) {
			
			matrica1[j]=new char[n];
			for(int k=0; k<n; k++) ulaz>>matrica1[j][k];

		}
		matrica2=rotate(matrica1, n);
		red=blue=false;
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				if(matrica2[i][j]=='R'&&(!red)) red=proveriResenje(matrica2, i, j, n, k);
				else if(matrica2[i][j]=='B'&&(!blue)) blue=proveriResenje(matrica2, i, j, n, k);
			}
		}
		izlaz<<"Case #"<<i<<": ";
		if(red&&blue) izlaz<<"Both\n";
		else if (red) izlaz<<"Red\n";
		else if (blue) izlaz<<"Blue\n";
		else izlaz<<"Neither\n";
	}

	
}