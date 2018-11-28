#include<iostream>
#include<cstring>

using namespace std;

int main(){
	int test, c, d, n, k, flag;
	char combine[256][256];
	char oppose[256][256];
	char x, y, w;
	char str[110];
	char ans[110];
	
	cin >> test;
	for(int t=1;t<=test;t++){
		memset(combine, 0, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));
		
		cin >> c;
		for(int i=0;i<c;i++){
			cin >> x >> y >> w;
			combine[x][y] = w;
			combine[y][x] = w;
		}
		
		cin >> d;
		for(int i=0;i<d;i++){
			cin >> x >> y;
			oppose[x][y] = 1;
			oppose[y][x] = 1;
		}
		
		cin >> n;
		cin >> str;
		
		k = -1;
		for(int i=0; i < n ; i++){
			//cout << "ans: " << ans << "   str["<<i<<"]: "<< str[i] << endl;
			
			if(k < 0){
				ans[++k] = str[i];
				continue;
			}
			
			if(combine[str[i]][ans[k]] != 0){
				ans[k] = combine[str[i]][ans[k]];
			}
			else{
				
				ans[++k] = str[i];
			
				for(int j=0;j<k;j++){
					if(oppose[ans[j]][str[i]] == 1){
						k = -1;
					}
				}
				
			}
		}
		
		cout << "Case #" << t << ": " << "[";
		for(int i=0;i<k;i++){
			cout << ans[i] << ", ";
		}
		if(k >= 0) cout << ans[k] << "]\n";
		else  cout << "]\n";
	}
	
	return 0;
}
