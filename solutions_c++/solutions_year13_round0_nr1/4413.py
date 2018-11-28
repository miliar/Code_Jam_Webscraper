#include <iostream>
#include <algorithm>

using namespace std;

int checker(char temp[], int n){
	int flag = 0, i, j;
	char a;
	if(temp[3] == 'z'){
		flag = 1;//not complete
	}else if(temp[3] == 'T'){
		cout << "Case #" << n << ": " << temp[2] << " won" << endl;
		flag = 2;
		return flag;
	}else if(temp[0] == 'T' && temp[3] != 'z'){
		cout << "Case #" << n << ": " << temp[2] << " won" << endl;
		flag = 2;
		return flag;
	}else{
		for(j = 0; j < 3; j++){
			if(temp[j] != temp[j+1]){
				flag = 3;
				return flag;
			}
			else{
				a = temp[j];
				flag = 2;
			}
		}
		if(flag == 2){
			cout << "Case #" << n << ": " << a << " won" << endl;
			return flag;
		}
	}
	return flag;
}

int main(){
	int t, i, j, n = 1, flag = 0, flag1 = 0, k;
	char tic[4][4], temp[4], a;
	size_t len;
	cin >> t;
	
	while(t--){
		flag = 0;
		flag1 = 0;
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++)
				tic[i][j] = 'z';
		}
		for(i = 0; i < 4; i++){
			for(j = 0; j < 4; j++){
				cin >> a;
				if(a == '.')
					a = 'z';
				tic[i][j] = a;
			}
		}
		for(k = 0; k < 10; k++){
			if(k <= 3){
				for(i = 0; i < 4; i++){
					temp[i] = tic[i][k];
				}
				//len = sizeof(temp)/sizeof(*temp);
				sort(temp, temp + 4);
				
				flag = checker(temp, n);
				if(flag == 2){
					break;
				}else if(flag == 1){
					flag1 = 1;
				}
			}
			else if(k > 3 && k <= 7){
				for(j = 0; j < 4; j++){
					temp[j] = tic[k-4][j];
				}
				sort(temp, temp + 4);

				flag = checker(temp, n);
				if(flag == 2)
					break;
				else if(flag == 1){
					flag1 = 1;
				}
			} else if(k == 8){
				for(i = 0; i < 4; i++)
					temp[i] = tic[i][i];
				sort(temp, temp + 4);

				flag = checker(temp, n);
				if(flag == 2)
					break;
				else if(flag == 1){
					flag1 = 1;
				}
			} else if(k == 9){
				for(i = 3, j = 0; i >= 0; i--, j++)
					temp[i] = tic[j][i];
				sort(temp, temp + 4);

				flag = checker(temp, n);
				if(flag == 2)
					break;
				else if(flag == 1)
					flag1 = 1;

			}
		}

		if(flag == 1){
			cout << "Case #" << n << ": " << "Game has not completed" << endl;
		}else if(flag == 3 && flag1 == 1){
			cout << "Case #" << n << ": " << "Game has not completed" << endl;
		}else if(flag == 3){
			cout << "Case #" << n << ": " << "Draw" << endl;
		}
	n++;
	}
	
	return 0;
}
