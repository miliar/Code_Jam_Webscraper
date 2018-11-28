#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main(){
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int t;
	bool flag;
	string s;
	int r,c;
	int i,j,k;
	int count;
	char map[58][58];
	cin >> t;
	for(i=1;i<=t;i++){
		cout << "Case #" << i << ":" << endl;
		flag=false;
		cin >> r >> c;
		count=0;
		for(j=0;j<r;j++){
			getline(cin,s);
			for(k=0;k<c;k++){
				cin.get(map[j][k]);
				if(map[j][k]=='#'){
					count++;
				}
			}
		}
		if(count%4!=0){
			cout << "Impossible" << endl;
			continue;
		}
		for(j=0;j<r-1;j++){
			for(k=0;k<c-1;k++){
				if(map[j][k]=='#'){
					if(map[j+1][k]=='#' && map[j][k+1]=='#' && map[j+1][k+1]=='#'){
						map[j][k]='/';
						map[j+1][k]='\\';
						map[j][k+1]='\\';
						map[j+1][k+1]='/';
					}else{
						flag=true;
						break;
					}
				}
			}
			if(flag) break;
		}
		if(flag){
			cout << "Impossible" << endl;
		}else{
			for(j=0;j<r;j++){
				for(k=0;k<c;k++){
					cout << map[j][k];
				}
				cout << endl;
			}
		}

	}
	return 0;
}