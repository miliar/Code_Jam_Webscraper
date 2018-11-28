#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <fstream>

using namespace std;

int main()
{
	int t,n;
	char s[4];
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>t;
	for(int j=0; j<t; j++){
		fin>>n;
		int p[120];
		int pi=0;
		int o[120], b[120];
		int oi=0, bi=0;
		int op=0, bp=0;
		int oc=1, bc=1;
		for(int k=0; k<n; k++){
			fin>>s;
			if(strcmp(s,"O") == 0){
				p[pi++] = 0;
				fin>>s;
				o[oi++] = atoi(s);
			}
			else{
				p[pi++] = 1;
				fin>>s;
				b[bi++] = atoi(s);
			}
		}

		int t=0;
		int cp=0;
		int ido, idb;
		int of=0, bf=0;
		while(cp < pi){
			of=bf=0;
			if(o[op] != oc){
				if(o[op] - oc > 0){
					oc++;
				}
				else if(o[op] - oc < 0){
					oc--;	
				}
				of=1;
			}

			if(b[bp] != bc){
				if(b[bp] - bc > 0){
					bc++;
				}
				else if(b[bp] - bc < 0){
					bc--;
				}
				bf=1;
			}
			
			if(p[cp] == 0){
				if(o[op] == oc && of == 0){
					if(op < oi-1){
						op++;
					}
					cp++;
				}
				// O's Turn
			}
			else{
				if(b[bp] == bc && bf == 0){
					if(bp < bi-1){
						bp++;
					}
					cp++;
				}
				//B's Turn
			}
			t++;
		}
		fout<<"Case #"<<j+1<<": "<<t<<endl;
	}

	fin.close();
	fout.close();

	return 0;
}