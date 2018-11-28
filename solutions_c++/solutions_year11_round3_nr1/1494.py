#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main(){
	int T; cin >> T;
	for(int t=0;t<T;t++){
		int R, C; cin >> R >> C;
		vector <string> pic;

		for(int i=0;i<R;i++){
			string temp; cin >> temp;
			pic.push_back(temp);
		}

		int blue = 0;
		for(int i=0;i<R;i++){
			for(int j=0;j<C;j++){
				if(pic[i][j]=='#')	blue++;
			}
		}
		if(blue%4!=0 || ((blue>0)&&(R==1) || (blue>0)&&(C==1))){
			printf("Case #%d:\nImpossible\n", t+1);
			continue;
		}
		if(blue==0){
			printf("Case #%d:\n", t+1);
			for(int i=0;i<R;i++)	cout << pic[i] << endl;
			continue;
		}

		//	1行目　R行目
		bool flag = true;
		for(int i=0;i<C-1;i++){
			if(pic[0][i]=='#'){
				if(pic[0][i+1]=='#' && pic[1][i]=='#' && pic[1][i+1]=='#'){
					pic[0][i] = pic[1][i+1] = '/';
					pic[0][i+1] = pic[1][i] = '\\';
				}else{
					flag = false;
				}
			}
			if(pic[R-1][i]=='#'){
				if(pic[R-1][i+1]=='#' && pic[R-2][i]=='#' && pic[R-2][i+1]=='#'){
					pic[R-2][i] = pic[R-1][i+1] = '/';
					pic[R-2][i+1] = pic[R-1][i] = '\\';
				}else{
					flag = false;
				}
			}
		}
		if(!flag){
			printf("Case #%d:\nImpossible\n", t+1);
			continue;
		}
		//	1列目　C列目
		for(int i=0;i<R-1;i++){
			if(pic[i][0]=='#'){
				if(pic[i+1][0]=='#' && pic[i][1]=='#' && pic[i+1][1]=='#'){
					pic[i][0] = pic[i+1][1] = '/';
					pic[i][1] = pic[i+1][0] = '\\';
				}else{
					flag = false;
				}
			}
			if(pic[i][C-1]=='#'){
				if(pic[i+1][C-1]=='#' && pic[i][C-2]=='#' && pic[i+1][C-2]=='#'){
					pic[i][C-2] = pic[i+1][C-1] = '/';
					pic[i][C-1] = pic[i+1][C-2] = '\\';
				}else{
					flag = false;
				}
			}
		}
		if(!flag){
			printf("Case #%d:\nImpossible\n", t+1);
			continue;
		}

		//	それ以外
		for(int i=0;i<R-1;i++){
			for(int j=0;j<C-1;j++){
				if(pic[i][j]=='#'){
					if(pic[i+1][j]=='#' && pic[i][j+1]=='#' && pic[i+1][j+1]=='#'){
						pic[i][j] = pic[i+1][j+1] = '/';
						pic[i][j+1] = pic[i+1][j] = '\\';
					}else{
						flag = false;
					}
				}
			}
		}
		if(!flag){
			printf("Case #%d:\nImpossible\n", t+1);
			continue;
		}

		printf("Case #%d:\n", t+1);
		for(int i=0;i<R;i++)	cout << pic[i] << endl;
	}
	return 0;
}