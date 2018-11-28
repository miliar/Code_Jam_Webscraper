#include <iostream>
using namespace std;

int input[500][2];
int o[500];
int b[500];
int x;
int count_o = 0;
int count_b = 0;
void init()
{
	count_o = 0;
	count_b = 0;
	for(int i=0;i<x;i++){
		input[i][0] = 0;
		input[i][1] = 1;
		o[i] = 0;
		b[i] = 0;
	}
}
int solve()
{
	int time_res = 0;
	int curr_o = 1;
	int next_o = 1;
	int curr_b = 1;
	int next_b = 1;
	int time_b = 0;
	int time_o = 0;
	for(int i=0;i<x;i++){
		if( input[i][0] == 0 ){
			int temp = input[i][1] - curr_o;
			if(temp < 0){
				temp = -temp;
			}
			if( temp <= time_o ){
				temp = 0;
			}else{
				temp = temp - time_o;
			}
			time_o = 0;
			curr_o = input[i][1];
			time_res+=temp;
			time_res++;
			time_b = time_b + temp + 1;
		}else if( input[i][0] == 1 ){
			int temp = input[i][1] - curr_b;
			if(temp < 0){
				temp = -temp;
			}
			if( temp <= time_b){
				temp = 0;
			}else{
				temp = temp - time_b;
			}
			time_b = 0;
			if(temp < 0){
				temp = -temp;
			}
			time_o = time_o + temp + 1;
			curr_b = input[i][1];
			time_res = time_res + temp;
			time_res++;
		}
	}
	return time_res;
}
		
int main()
{
	int t = 0;
	cin >> t;
	int j = 0;
	while(t--){
		j++;
		cin >> x;
		init();
	//	int input[x][2];
	//	int o[x];
	//	int b[x];
	//	int count_o = 0;
	//	int count_b = 0;
		for(int i=0;i<x;i++){
			char c;
			cin >> c;
			int a;
			cin >> a;
			if( c == 'O' ){
				input[i][0] = 0;
				o[count_o++] = a;
			}else if( c == 'B' ){
				input[i][0] = 1;
				b[count_b++] = a;
			}
			input[i][1] = a;
			//cout << input[i][0] << "	" << input[i][1] << endl;
		}
		int res = solve();
		cout << "Case #" << j << ": " << res << endl;
	}
	return 0;
}

			
