#include <iostream>
#include <cstdlib>
#include <fstream>
#include <bitset>

using namespace std;

int main() {
	ifstream inFile;
	ofstream outFile;
	inFile.open("data.txt");
	outFile.open("solution.txt");
	int z;
	int dif;
	int t;
	int n;
	int pos[2];
	int x[101];
	char a[101];
	int blue[101];
	inFile >> t;
	for (int i=0; i<t; ++i) {
		inFile >> n;
		z=0;
		pos[0]=1;
		pos[1]=1;
		for (int j=0; j<n; ++j) {
			inFile >> a[j];
			inFile >> x[j];
			if (a[j]=='B') blue[j]=1;
			else blue[j]=0;
		}
		for (int j=0; j<n; ++j) {
			dif=abs(pos[blue[j]]-x[j])+1;
			z+=dif;
			pos[blue[j]]=x[j];
			int u=j+1;
			while (blue[j]==blue[u]) ++u;
			if (u<n) {
				if (pos[blue[u]] > x[u]) {
					pos[blue[u]]-=dif;
					if (pos[blue[u]] < x[u]) pos[blue[u]] = x[u];
				}
				else {
					pos[blue[u]]+=dif;
					if (pos[blue[u]] > x[u]) pos[blue[u]] = x[u];
				}
				if (pos[blue[u]]<1) pos[blue[u]]=1;
				if (pos[blue[u]]>100) pos[blue[u]]=100;
			}
		}
		outFile << "Case #" << i+1 << ": " << z << endl;
	}
	system("pause");
	return 0;
}