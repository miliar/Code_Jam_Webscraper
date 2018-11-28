#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

int main(int argc, char **argv){
	FILE *fp = fopen("B-small-attempt2.in", "rb");
	char line[500];
	int n, s, p, i = 0;
	char *pch;

	int index = 0;

	if(fp != NULL){
		vector<int> temp;
		while(fgets(line, 500, fp) != NULL){
			index++;
			if( i == 0){
				i++;
				continue;
			}
			pch = strtok(line, " ");
			i = 0;
			while(pch != NULL){
				if(i == 0){
					n = atoi(pch);
				} else if (i == 1) {
					s = atoi(pch);
				} else if (i == 2) {
					p = atoi(pch);
				} else { 
					temp.push_back(atoi(pch));
				}
				i++;
				pch = strtok(NULL, " ");
			}

			int count = 0;
			int surprise = s;
			for(int j = 0; j < temp.size(); ++j){
				int score = temp[j];
				int k = (score/3);

				if(k == 0){
					if((score == 0) && (p == 0)){
						count++;
					} else if ((score == 1) && (p <= 1)){
						count++;
					} else if (score == 2) {
						if((p == 2) && (surprise > 0)){
							count++;
							surprise--;
						} else if (p <= 1){
							count++;
						}
					}
					continue;
				}

				if((score%k) == 0){
					
					if(k >= p){
						count++;
					} else if((surprise > 0)	&& ((k+1) >= p)){
						count++;
						surprise--;
					}
				} else if ((score%k) == 1){
					if((k+1) >= p){
						count++;
					}
				} else {
					if((k+1) >= p){
						count++;
					} else if(((k+2) >= p) && (surprise > 0)){
						surprise--;
						count++;
					}
				}
			}

			cout << "Case #" << index-1 << ": " << count << endl;
			temp.clear();
		}
	}

	return 0;
}
