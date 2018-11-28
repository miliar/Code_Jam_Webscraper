#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdio>
#define eps (1e-5)
#define infinite ((1<<31)-1)

using namespace std;

char mat[64][64];
//int dp_r[64][64];
//int dp_l[64][64];
bool flag[64][64];

bool findK(char c,int n,int K){
	int cnt = 0;

	for(int i = 0;i < n;++i){
		cnt = 0;
		for(int j = 0;j < n;++j){
			if(mat[i][j] == c){
				cnt++;
				if(cnt >= K)
					return true;
			}
			else{
				if(cnt >= K)
					return true;
				cnt = 0;
			}

		}
	}

	
	for(int i = 0;i < n;++i){
		cnt = 0;
		for(int j = 0;j < n;++j){
			if(mat[j][i] == c){
				cnt++;
				if(cnt >= K)
					return true;
			}
			else{
				if(cnt >= K)
					return true;
				cnt = 0;
			}

		}
	}


	for(int i = 0;i < n;++i){
		for(int j = 0;j < n;++j){
			flag[i][j] = 0;
		}
	}

	cnt = 0;
	for(int i = 0;i < n;++i){
		for(int j = 0;j < n;++j){
			if(flag[i][j])
				continue;

			if(mat[i][j] == c){
				cnt = 1;
				int k = 1;
				while(i + k < n && j + k < n && mat[i + k][j + k] == c){
					cnt++;
					flag[i + k][j + k] = true;
					k++;
				}
				if(cnt >= K)
					return true;

			}
		}
	}


	for(int i = 0;i < n;++i){
		for(int j = 0;j < n;++j){
			flag[i][j] = 0;
		}
	}
	cnt = 0;
	for(int i = 0;i < n;++i){
		for(int j = 0;j < n;++j){
			if(flag[i][j])
				continue;

			if(mat[i][j] == c){
				cnt = 1;
				int k = 1;
				while(i + k < n && j - k >= 0 && mat[i + k][j - k] == c){
					cnt++;
					flag[i + k][j - k] = true;
					k++;
				}
				if(cnt >= K)
					return true;
			}
		}
	}

	return false;
}

int main(int argc, char *argv[]){

	FILE *fp = fopen(argv[1],"r");
	FILE *out = fopen("output.txt","w+");
	if(fp == NULL)
		printf("file error.\n");

	int T,n,K;
	fscanf(fp,"%d",&T);

	for(int i = 1;i <= T;++i){
		fscanf(fp,"%d %d",&n,&K);


		for(int i = 0;i < n;++i){
			for(int j = 0;j < n;++j){
				char c;
				fscanf(fp,"%c",&c);
				if(c == 'B' || c == 'R' || c == '.'){
					mat[j][n - i - 1] = c;
					//printf("%c",mat[j][n - i - 1]);
				}
				else
					j--;
			}
			//printf("\n");

		}


		//gravaity
		for(int j = 0;j < n;++j){
			int offset = 0;
			for(int i = n - 1;i >= 0;--i){
				if(mat[i][j] == '.')
					offset++;
				else{
					if(offset == 0)
						continue;
					for(int k = i;k >= 0;--k){
						mat[k + offset][j] = mat[k][j];
					}

					for(int k = 0;k < offset;++k)
						mat[k][j] = '.';

					i = i + offset;
					offset = 0;
				}

			}
		}

	/*	for(int i = 0;i < n;++i){
			for(int j = 0;j < n;++j)
				printf("%c ",mat[i][j]);
			printf("\n");
		}*/

		//find K
		bool flagb,flagr;
		flagb = findK('B',n,K);
		flagr = findK('R',n,K);

		if(flagb == true && flagr == true){
			fprintf(out,"Case #%d: Both\n",i);
			continue;
		}

		if(flagb == true){
			fprintf(out,"Case #%d: Blue\n",i);
			continue;
		}

		if(flagr == true){
			fprintf(out,"Case #%d: Red\n",i);
			continue;
		}


		fprintf(out,"Case #%d: Neither\n",i);
	}

	return 0;
}