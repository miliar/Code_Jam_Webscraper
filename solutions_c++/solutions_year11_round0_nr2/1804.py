#include <iostream>

#define BASEN 8

using namespace std;

int main(){
	int t,c,d,n;
	int ansp;
	int c_flag[36];
	int d_flag[28];
	int old_d_flag[28];
	bool flag;
	
	char c_ch[36][3];
	char d_ch[28][2];
	char ans[100];
	char tmp;
	
	char base[BASEN] = {'Q','W','E','R','A','S','D','F'};
	
	cin >> t;
	
	for(int i = 0; i < t; i++){
		cin >> c;
		for(int j = 0; j < c; j++){
			cin >> c_ch[j][1] >> c_ch[j][2] >> c_ch[j][0];
		}
		
		cin >> d;
		for(int j = 0; j < d; j++){
			cin >> d_ch[j][0] >> d_ch[j][1];
		}
		
		for(int l = 0; l < c; l++) c_flag[l] = 0;
		for(int l = 0; l < d; l++) d_flag[l] = 0;
		ansp = 0;
		
		cin >> n;
		for(int j = 0; j < n; j++){
			cin >> tmp;
			flag = false;
			
			for(int k = 0; k < BASEN; k++){
				if(tmp == base[k]){
					flag = true;
					break;
				}
			}
			if(flag){
				flag = false;
				for(int k = 0; k < c; k++){
					if(c_flag[k] && tmp == c_ch[k][c_flag[k]]){
						ans[ansp-1] = c_ch[k][0];
						flag = true;
						for(int l = 0; l < c; l++) c_flag[l] = 0;
						for(int l = 0; l < d; l++) d_flag[l] = old_d_flag[l];
						break;
					}
					if(tmp == c_ch[k][1]){
						c_flag[k] = 2;
					}else if(tmp == c_ch[k][2]){
						c_flag[k] = 1;
					}else{
						c_flag[k] = 0;
					}
				}
				if(flag) continue;
				
				for(int k = 0; k < d; k++) old_d_flag[k] = d_flag[k];
				
				for(int k = 0; k < d; k++){
					if(d_flag[k]){
						if(tmp == d_ch[k][d_flag[k]-1]){
							ansp = 0;
							flag = true;
							for(int l = 0; l < c; l++) c_flag[l] = 0;
							for(int l = 0; l < d; l++) d_flag[l] = 0;
							break;
						}
					}else if(tmp == d_ch[k][0]){
						d_flag[k] = 2;
					}else if(tmp == d_ch[k][1]){
						d_flag[k] = 1;
					}else{
						d_flag[k] = 0;
					}
				}
				if(flag) continue;
			}
			
			ans[ansp++] = tmp;
		}
		
		cout << "Case #" << (i+1) << ": [";
		for(int j = 0; j < ansp - 1; j++) cout << ans[j] << ", ";
		if(ansp > 0) cout << ans[ansp-1];
		cout << "]" << endl;
	}
	
	return 0;
}