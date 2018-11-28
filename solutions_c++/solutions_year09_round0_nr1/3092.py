#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.in");
	fout.open("output.in");
	int l,d,n;
	fin>>l>>d>>n;
	char a[5000][16];
	string b[500];
	for(int i=0;i<d;i++){
		fin>>a[i];
	}
	for(int i=0;i<n;i++){
		fin>>b[i];
	}
	
	for(int i=0;i<n;i++){
		int tf[5000] = {0,};
		int sum=0;
		int c1 = 0;
		int c2 = 0;
		int com = 0;
		while(b[i][c1] != 0){
			if(b[i][c1] != '('){
				for(int j=0;j<d;j++){
					if(tf[j] == -1)continue;
					if(b[i][c1] == a[j][c2]) tf[j] = 1;
				}
				for(int j=0;j<d;j++){
					if(tf[j] != 1) tf[j] = -1;
				}
				c1++;
				c2++;
			}else{
				c1++;
				while(b[i][c1] != ')'){
					for(int j=0;j<d;j++){
						if(tf[j] == -1) continue;
						if(!tf[j]){
							if(b[i][c1] == a[j][c2]){
								 tf[j] = 1;
							}
						}
					}
					c1++;
				}
				for(int j=0;j<d;j++){
					if(tf[j] == 0) tf[j] = -1;
				}
				c1++;
				c2++;
			}
			for(int k=0;k<d;k++){
				if(tf[k] != -1 ) tf[k] = 0;
			}
		}
		for(int k=0;k<d;k++){
			if(tf[k]!=-1)sum++;
		}
		fout<<"Case #"<<i+1<<": "<<sum<<endl;;
	}

	return 0;
}
