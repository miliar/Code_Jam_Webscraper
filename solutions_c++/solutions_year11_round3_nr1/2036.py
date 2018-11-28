// testA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <queue>

#define		MAX_NUM  50

int parse1(char **buff, int row, int col)
{
	std::queue<int> que;
	int cnt = 0;
	int k = 0;
	int m = 0;
	int j = 0;
	int i = 0;

	for (i = 0; i < row; i ++){
		while(!que.empty()){
			k = que.front();
			if (buff[i][k] == '#' && buff[i][k +1] == '#'){
				m = i - 1;
				buff[m][k] ='/';
				buff[m][k + 1] = '\\';
				buff[i][k] ='\\';
				buff[i][k + 1] = '/';
			}
			que.pop();
		}

		for (j = 0; j < col; j ++){
			if (buff[i][j] == '#'){
				cnt ++;
				if ((j + 1) < col && buff[i][j + 1] == '#'){
					que.push(j);
					cnt ++;
					j ++;
				}
			}
		}

		if ((cnt % 2)  != 0){
			return 0;
		}

	}
	return 1;
}


int main(int argc, char* argv[])
{
	if (argc != 2) {
		printf("Usage: ./main input_file\n");
		return -1;
    }
    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
		printf("Input File %s Open Error.\n", argv[1]);
		return 0;
    }
	
	char buff[MAX_NUM][MAX_NUM];
	char *p[MAX_NUM];
    int T, N, M;
	int nret,i,j,k ;
	
	p[0] = &buff[0][0];

	for (int f = 1; f < MAX_NUM; f ++){
		p[f] = buff[f];
	}

    fscanf(fp, "%d\n", &T);
    for (i = 0; i < T; i++) {
		fscanf(fp, "%d %d", &N, &M);

		for (j=0; j < N; j++){
			for (k = 0; k < M; k ++){
				fscanf(fp, " %c", &buff[j][k]);
			}
		}

		nret = parse1(p,N,M);
		if (!nret){
			printf("Case #%d: \nImpossible \n", i + 1);
			continue;
		}
		printf("Case #%d:\n", i + 1);

		for (j = 0; j < N; j ++){
			for (k = 0; k < M; k ++){
				printf("%c", buff[j][k]);
			}
			printf("\n");
		}

	}
	fclose(fp);



	return 0;
}

/*

struct node{
	int64 n;
	int pd;
	int pg;
};

int parse(struct node *ptmp)
{

	if (ptmp->pd == 0){
		return 1;
	}
	if (ptmp->pg == 100 && ptmp->pd == 100){
		return 1;
	}
	if (ptmp->pg == 100 && ptmp->pd != 100){
		return 0;
	}

	int64 tmp = (int64)(ptmp->pd/xx(ptmp->pd, 100));
	
	if (tmp <= ptmp->n){
		return 1;
	}
	return 0;
}
*/