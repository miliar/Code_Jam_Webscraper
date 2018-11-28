#include <cstdio>

inline int min(int a, int b) {
	if(a<b) return a;
	return b;
}

int main() {
	
	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
//		printf("START case %d\n",caseNum);
		int M,N;
		scanf("%d %d",&M,&N);

		getchar();

		bool grid[35][35];
		bool used[35][35] = {0};
		int sizes[35] = {0};

		for(int i=0;i<M;i++) {
			for(int j=0;j<N/4;j++) {
				char inpString[2];
				inpString[0] = getchar();
				unsigned int this4;
				sscanf(inpString,"%x",&this4);
				for(int k=0;k<4;k++) {
					grid[i][j*4+k] = this4 & (1<<(3-k));
				}
			}
			getchar();
		}

		int maxSize = min(M,N);
		int squaresRem = M*N;
		for(int gridSize=maxSize;gridSize>=2;gridSize--) {
//			printf("trying size %d\n",gridSize);
			for(int i=0;M-i>=gridSize;i++) {
				for(int j=0;N-j>=gridSize;j++) {
					bool start = !grid[i][j];
					bool last = !grid[i][j];
					bool isOK = true;
					for(int y=0;y<gridSize;y++) {
						if(grid[i+y][j]!=start) {
							start = grid[i+y][j];
						} else {
							isOK = false;
						}

						for(int z=0;z<gridSize;z++) {
							if((grid[i+y][j+z]!=last||z==0) && !used[i+y][j+z]) {
								last = grid[i+y][j+z];
							} else {
								if(gridSize==6 && i==0 && j==13 && caseNum==1) {
//									printf("failed @ (%d,%d), last = %d\n",j+z,i+y,last);
								}
								isOK = false;
							}
						}
					}
					if(isOK) {
						sizes[gridSize]++;
						for(int y=0;y<gridSize;y++) {
							for(int z=0;z<gridSize;z++) {
								used[i+y][j+z] = true;
							}
						}
						squaresRem -= gridSize*gridSize;
//						printf("square of size %d found at (%d,%d)\n",gridSize,j,i);
					}
				}
			}
		}
		sizes[1] = squaresRem;
	
		int total = 0;
		for(int i=maxSize;i>=1;i--) {
			if(sizes[i]>0) {
				total++;
			}
		}

		printf("Case #%d: %d\n",caseNum,total);

		for(int i=maxSize;i>=1;i--) {
			if(sizes[i]>0) {
				printf("%d %d\n",i,sizes[i]);
			}
		}
	}
	return 0;
}

