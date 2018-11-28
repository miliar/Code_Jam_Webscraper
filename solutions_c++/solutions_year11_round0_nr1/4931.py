#include <iostream>
using namespace std;

int main(){
	int t, n, i , j, k, o_pos, b_pos, o_ind, b_ind, index, step;
	int p[100];
	char color[100];
	cin >> t;
	for(i = 1 ; i <= t ; i++){
		o_pos = 1;
		b_pos = 1;
		o_ind = 0;
		b_ind = 0;
		index = 1;
		step = 0;
		cin >> n;
		for(j = 1 ; j <= n ; j++)
		{
			cin >> color[j];
			cin >> p[j];
		}
		while(index <= n)
		{
			// 時間を進める
			step++;
			//cout << index << " " << o_pos << " " << b_pos <<  " "<< o_ind << " " <<  b_ind <<endl;
			// 動かなくてはいけない位置をサーチする	
			if(o_ind < index)
			{
				for(k = index; k <= n; k++){
					if(color[k] == 'O'){
						o_ind = k;
						break;
					}
				}
			}

			if(b_ind < index)
			{
				for(k = index; k <= n; k++){
					if(color[k] == 'B'){
						b_ind = k;
						break;
					}
				}
			}
			// o_ind,b_indを見れば良い。
			
			// 押せるかどうか判定
			if(index == o_ind && p[o_ind] == o_pos){
				// 押す
				index++;
			}
			else if(index == b_ind && p[b_ind] == b_pos){
				index++;
			}
			
			// 移動
			if(o_pos < p[o_ind])
			{
				o_pos++;
			}
			else if(o_pos > p[o_ind]){
				o_pos--;
			}	
			// 移動
			if(b_pos < p[b_ind])
			{
				b_pos++;
			}
			else if(b_pos > p[b_ind]){
				b_pos--;
			}
		}
		cout << "Case #" << i << ": " << step << endl;
	}
	return 0;
}