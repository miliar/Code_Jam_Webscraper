#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;

int main(){
	int N;
	cin >> N;
	for(int times = 1; times <= N; times++){
		int myints[] = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15};
		char S[50001];
		char RLE[50001];
		char tmp[17];
		int K, len;
		int min_rle;

		cin >> K >> S;
		len = strlen(S);
		min_rle = INT_MAX;

		sort (myints,myints+K);

		do {
			int j;
			for(j = 0; j < len / K; j++){
				for(int i = 0; i < K; i++){
					tmp[i] = S[j * K + i];
				}
				for(int i = 0; i < K; i++){
					RLE[j * K + i] = tmp[myints[i]];
				}
			}
			char run = RLE[0];
			int rle = 1;
			for(int i = 1; i < len; i++){
				if(run != RLE[i]){
					rle++;
					run = RLE[i];
				}
			}
			if(min_rle > rle){
				min_rle = rle;
			}
		} while ( next_permutation (myints,myints+K) );


		cout << "Case #" << times << ": " << min_rle << endl;
	}
	return 0;
}
