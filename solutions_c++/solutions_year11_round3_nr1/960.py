#include <iostream>
#include <vector>
using namespace std;

int main(){
	int n, a, b;
	char temp;
	bool isPossible;
	cin >> n;
	for(int i=1; i<=n ;i++){
		cin >> a >> b;
		vector<vector<char> > map;
		for(int j=0; j<a; j++){
			vector<char> row;
			for(int k=0; k<b; k++){
				cin >> temp;
				row.push_back(temp);
			}
			map.push_back(row);
		}
		isPossible = true;
		for(int j=0; j<a; j++){
			for(int k=0; k<b; k++){
				if(j==a-1 || k==b-1){
          if(map[j][k]=='#'){
            isPossible = false;
					}
					continue;
				}
				if(map[j][k]=='#'){
					if(map[j][k+1]!='#'
					|| map[j+1][k]!='#'
					|| map[j+1][k+1]!='#'){
            isPossible = false;
					}else{
            map[j][k] = '/';
            map[j+1][k+1] = '/';
            map[j+1][k] = '\\';
            map[j][k+1] = '\\';
					}
				}
			}
		}
		cout << "Case #" << i <<":" << endl;
		if(!isPossible){
			cout << "Impossible" << endl;
		}else{
      for(int j=0; j<a; j++){
				for(int k=0; k<b; k++){
					cout << map[j][k];
				}
				cout << endl;
			}
		}
	}
	
//	system("pause");
}
