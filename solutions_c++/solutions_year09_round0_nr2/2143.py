#include <fstream>
using namespace std;
#define ALL(c) c.begin(), c.end()
#define pb push_back
#define sz size
int label;
char map[103][103];
int H,W;
int v[103][103] = {{0}};
int ff(int x, int y) {
	if(map[x][y]=='*') { 
		map[x][y] = '#';
		int N = v[x-1][y];
		int O = v[x][y-1];
		int E = v[x][y+1];
		int S = v[x+1][y];
		if(N<v[x][y] || O<v[x][y] || E<v[x][y] || S<v[x][y]) { // Comprueba que no sea un basin.
			if(N<=O && N<=E && N<=S) return ff(x-1,y);
			else if(O<=E && O<=S) return ff(x,y-1);
			else if(E<=S) return ff(x,y+1);
			else return ff(x+1,y);
		}
		else {
			// Nuevo Basin:
			label++;
			return 'a'+label;	
		}
	}
	else {
		return map[x][y]; // El label de la celda.	
	}
}
main () {
	// Declaracion de Variables:
	int T;
	int t,i,j,i1,j1,temp;
	// Apertura de archivos:
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	// Lectura de datos:
	fin>>T;
	for(t=1;t<=T;t++) {
		label = 0;
		fin>>H>>W;
		for(i=1;i<=H;i++)
			for(j=1;j<=W;j++) fin>>v[i][j];	
		
		// Crear borde:
		for(i=0;i<=H+1;i++) v[i][0] = v[i][W+1] = 99999;
		for(j=0;j<=W+1;j++) v[0][j] = v[H+1][j] = 99999;
		for(i=1;i<=H;i++) 
			for(j=1;j<=W;j++) map[i][j] = '*';
		// Label:
		label = -1;
		for(i=1;i<=H;i++) {
			for(j=1;j<=W;j++) {
				// Buscar Basin:
				if(map[i][j]=='*') {
					temp = ff(i,j);
					for(i1=1;i1<=H;i1++) 
						for(j1=1;j1<=W;j1++)
							if(map[i1][j1]=='#') map[i1][j1] = (char)temp;	
				}
			}
		}
		fout<<"Case #"<<t<<":"<<endl;
		for(i=1;i<=H;i++) {
			for(j=1;j<W;j++) fout<<map[i][j]<<" ";
			fout<<map[i][W]<<endl;
		}
	}
	// Cierro archivos:
	fin.close();
	fout.close();
return 0;	
}
