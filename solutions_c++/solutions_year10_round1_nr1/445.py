#include<algorithm>
#include<iostream>
#include<string>
#include<vector>
#include<cstdio>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<fstream>
#include<map>
#include<set>

#define MAX(x, y) ((x) > (y) ? (x) : (y))
#define MIN(x, y) ((x) < (y) ? (x) : (y))
#define ABS(x) ((x) > 0 ? (x) : -(x))

#define SWAP(x, y) {(x) += (y); (y) = (x) - (y); (x) -= (y);}

#define EPS 1e-6
#define PI 3.14159265358979323846

#define BLUE 0
#define	RED 1

char C[] = {'B', 'R'};

using namespace std;

int ncase, idx, N, K, H, W;

char board[50][50];

void rotate(){

	for(int i = 0; i < H; i++){

		vector<char> tmp;

		for(int j = 0; j < W; j++){
			if(board[i][j] - '.'){
				tmp.push_back(board[i][j]);
			}
		}

		int len = tmp.size();

		for(int j = 0; j < W - len; j++){
			board[i][j] = '.';
		}
		for(int j = W - len; j < W; j++){
			board[i][j] = tmp[j - W + len];
		}

	}
}

int yes[2];

string check(){

	memset(yes, 0, sizeof(yes));

	//horizontal
	for(int i = 0; i < H; i++){
		int len = 0;
		int start = -1;
		for(int j = 0; j < W; j++){

			if(start < 0 && board[i][j] - '.'){
				len = 1;
				start = (board[i][j] == 'B' ? 0: 1);
				continue;
			}

			int k = start;
			if(k < 0)	continue;
			if(board[i][j] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i][j] - C[1 - k]){
					len = 0;
					start = -1;
				}
				else{
					len = 1;
					start = 1 - k;
				}
			}
		}
	}
	//
	//vertical
	for(int j = 0; j < W; j++){
		int len = 0;
		int start = -1;
		for(int i = 0; i < H; i++){

			if(start < 0 && board[i][j] - '.'){
				len = 1;
				start = (board[i][j] == 'B' ? 0: 1);
				continue;
			}


			int k = start;
			if(k < 0)	continue;

			if(board[i][j] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i][j] - C[1 - k]){
			 		len = 0;
					start = -1;
				}
				else{
					len = 1;

					start = 1 - k;
				}
			}
		}
	}

	//  
	for(int j = 0; j < W; j++){

		int i = 0;
		int len = 0;
		int start = -1;
		while(i < H && j + i < W){

			if(start < 0 && board[i][j + i] - '.'){
				len = 1;
				start = (board[i][j + i] == 'B' ? 0: 1);
				i++;
				continue;
			}

			int k = start;
			if(k < 0){
				i++;
				continue;
			}

			if(board[i][j + i] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i][j + i] - C[1 - k]){
				len = 0;
				start = -1;
				}
				else{
					len = 1;
					start = 1 - k;
				}

			}

			i++;
		}

	}
	// / 
	for(int j = 0; j < W; j++){

		int i = 0;
		int len = 0;
		int start = -1;
		while(i < H && j - i >= 0){

			if(start < 0 && board[i][j - i] - '.'){
				len = 1;
				start = (board[i][j - i] == 'B' ? 0: 1);
				i++;
				continue;
			}

			int k = start;
			if(k < 0){
				i++;
				continue;
			}
			if(board[i][j - i] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i][j - i] - C[1 - k]){
				len = 0;
				start = -1;
				}
				else{
					len = 1;
					start = 1 - k;
				}
			}
			i++;
		}
	}
	//  
	for(int i = 0; i < H; i++){

		int j = 0;
		int len = 0;
		int start = -1;
		while(j < W && j + i < H){

			if(start < 0 && board[i + j][j] - '.'){
				len = 1;
				start = (board[i + j][j] == 'B' ? 0: 1);
				j++;
				continue;
			}

			int k = start;
			if(k < 0){
				j++;
				continue;
			}
			if(board[i + j][j] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i + j][j] - C[1 - k]){
				len = 0;
				start = -1;
				}
				else{
					len = 1;
					start = 1 - k;
				}
			}
			j++;
		}

	}

	// / 
	for(int i = 0; i < H; i++){

		int j = W - 1;
		int len = 0;
		int start = -1;
		while(j >= 0 && i + (W - 1 - j) < H){
		//while(j < W && i - j >= 0){

			if(start < 0 && board[i + W - 1 - j][j] - '.'){
				len = 1;
				start = (board[i + W - 1 - j][j] == 'B' ? 0: 1);
				//j++;
				j--;
				continue;
			}

			int k = start;
			if(k < 0){
				//j++;
				j--;
				continue;
			}
			if(board[i + W - 1 - j][j] == C[k]){
				len++;
				if(len >= K)	yes[k] = 1;
			}
			else{
				if(len >= K){
					yes[k] = 1;
				}
				if(board[i + W - 1 - j][j] - C[1 - k]){
				len = 0;
				start = -1;
				}
				else{
					len = 1;
					start = 1 - k;
				}
			}
			//j++;
			j--;
		}

	}

	if(yes[0] && yes[1])	return string("Both");
	if(yes[0])	return string("Blue");
	if(yes[1])	return string("Red");
	return string("Neither");


}

int main()
{

	//scanf("%d", &ncase);
	cin >> ncase;

	for(idx = 1; idx <= ncase; idx++){

		//scanf("%d %d\n", &N, &K);
		//scanf("%d", &K);

		cin >> N >> K;

		H = W = N;
		//printf("N = %d, K = %d\n", N, K);

		for(int i = 0; i < N; i++){
			for(int j = 0; j < N; j++){
				//scanf("%c", &board[i][j]);
				//printf("%c", board[i][j]);
				cin >> board[i][j];
			}
		}
		/*
		printf("before rotated:\n");
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				printf("%c", board[i][j]);
			}
			printf("\n");
		}
		*/



		rotate();

		/*
		printf("rotated:\n");
		for(int i = 0; i < H; i++){
			for(int j = 0; j < W; j++){
				printf("%c", board[i][j]);
			}
			printf("\n");
		}
		*/

		cout << "Case #" << idx << ": " << check() << endl;


	}

	
	return 0;
}

/*
 * vim: ts=2 sw=2
 * Local variables:
 * tab-width: 2
 * End:
 */
