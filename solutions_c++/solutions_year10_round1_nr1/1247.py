#include <cstdio>

const int MAX_N = 10;

char old[MAX_N][MAX_N];
char brandnew[MAX_N][MAX_N];
char gravity[MAX_N][MAX_N];

int main() {
	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);

	int T;
	scanf("%d",&T);

	for(int caseNum=1;caseNum<=T;caseNum++) {
		for(int i=0;i<MAX_N;i++) {
			for(int j=0;j<MAX_N;j++) {
				old[i][j] = 0;
				brandnew[i][j] = 0;
				gravity[i][j] = 0;
			}
		}

		int N,K;
		scanf("%d %d",&N,&K);

		for(int i=0;i<N;i++) {
			scanf("%s\n",old[i]);
		}
		
		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
				brandnew[j][N-1-i] = old[i][j];
			}
		}
		
		for(int j=0;j<N;j++) {
			int start = N-1;
			for(int i=N-1;i>=0;i--) {
				if(brandnew[i][j]=='.') {
					continue;
				} else {
					gravity[start][j] = brandnew[i][j];
					start--;
				}
			}
		}

//		for(int i=0;i<N;i++) {
//			printf("%s\n",gravity[i]);
//		}

		//check for wins
		bool red = false;
		bool blue = false;

		for(int i=0;i<N;i++) {
			for(int j=0;j<N;j++) {
//				if(caseNum==81) {
//					printf("(%d,%d)....\n",j,i);
//				}
				//check horizontally right for red
				if((N-j)>=K) {
//					printf("can 1\n");
//					printf("(%d,%d),0\n",j,i);
					bool clean1 = true;
					bool clean2 = true;
					for(int z=0;z<K;z++) {
						if(gravity[i][j+z]=='B') {
							clean1 = false;
						} else if(gravity[i][j+z]=='R'){
							clean2 = false;
						} else {
							clean1 = false;
							clean2 = false;
						}
					}
				//	printf("\n");
					if(clean1==true && red==false) {
						red = true;
					}
					if(clean2==true && blue==false) {
						blue = true;
					}
				}
				if((N-i)>=K) {
//					printf("can 2\n");
					bool clean1 = true;
					bool clean2 = true;
					for(int z=0;z<K;z++) {
//						if(caseNum==62) {
//							printf("%c,%d\n",gravity[i+z][j],z);
//						}
						if(gravity[i+z][j]=='B') {
							clean1 = false;
						} else if(gravity[i+z][j]=='R'){
							clean2 = false;
						} else {
							clean1 = false;
							clean2 = false;
						}
					}
//					if(caseNum==62) {
//						printf("res = %d->(%d,%d)\n",i,clean1,clean2);
//					}
					if(clean1==true && red==false) {
						red = true;
					}
					if(clean2==true && blue==false) {
						blue = true;
					}
				}
				if((N-j)>=K && (N-i)>=K) {
//					printf("can 3\n");
					bool clean1 = true;
					bool clean2 = true;
					for(int z=0;z<K;z++) {
//						if(caseNum==81) {
//							printf("%c,%d\n",gravity[i+z][j+z],z);
//						}
						if(gravity[i+z][j+z]=='B') {
							clean1 = false;
						} else if(gravity[i+z][j+z]=='R'){
							clean2 = false;
						} else {
							clean1 = false;
							clean2 = false;
						}
					}
					//printf("res = (%d,%d)\n",clean1,clean2);
//					if(caseNum==81) {
//						printf("res = (%d,%d)\n",clean1,clean2);
//					}
					if(clean1==true && red==false) {
						red = true;
					}
					if(clean2==true && blue==false) {
						blue = true;
					}
				}
				if((i+1)>=K && (N-j)>=K) {
//					printf("can 4\n");
					bool clean1 = true;
					bool clean2 = true;
					for(int z=0;z<K;z++) {
						if(gravity[i-z][j+z]=='B') {
							clean1 = false;
						} else if(gravity[i-z][j+z]=='R'){
							clean2 = false;
						} else {
							clean1 = false;
							clean2 = false;
						}
					}
					//printf("res = (%d,%d)\n",clean1,clean2);
					if(clean1==true && red==false) {
						red = true;
					}
					if(clean2==true && blue==false) {
						blue = true;
					}
				}
			}
		}
//		printf("red = %d, blue = %d\n",red,blue);

		printf("Case #%d: ",caseNum);
		if(!red && !blue) {
			printf("Neither\n");
		} else if(!red && blue) {
			printf("Blue\n");
		} else if(red && !blue) {
			printf("Red\n");
		} else {
			printf("Both\n");
		}
	}

	return 0;
}
