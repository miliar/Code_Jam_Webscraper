#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
using namespace std;
int n;
int m;
int main() {
	ifstream fin("test.in");
	ofstream fout("test.out");
	fin >> n;

	for (int i = 0; i < n; i++) {
		int OR[300] = { 0 };
		int ALL[300] = { 0 };
		int allNum = -1;
		int orPos = 1;
		int blPos = 1;
		int pos;
		int orT=0;
		int T=0;
		char color;
		char hiscolor = 'N';
		int re = 0;
		fin >> m;
		for (int j = 0; j < m; j++) {
			fin >> color;
			fin >> pos;
			if (color != hiscolor) {
				
				if (color == 'O') {
					re += abs(pos - orPos)>T? abs(pos - orPos)-T+1:1;
					
					T=abs(pos - orPos)>T? abs(pos - orPos)-T+1:1;
					orPos=pos;
				}
				else
				{
					re+=abs(pos-blPos)>T? abs(pos-blPos)-T+1:1;
					
					T=abs(pos-blPos)>T? abs(pos-blPos)-T+1:1;
					blPos=pos;
				}
				
			}
			else
			{
				if (color == 'O') {
					T+=abs(pos - orPos)+1;
					re += abs(pos - orPos)+1;
					orPos=pos;
				}
				else
				{
					T+=abs(pos-blPos)+1;
					re+=abs(pos-blPos)+1;
					blPos=pos;
				}
			}
			hiscolor = color;
		}
		
	
	
		fout << "Case #" << i + 1 << ": " << re << endl;
		
	}
	
	
	//cin>>n;
	return 1;
}
