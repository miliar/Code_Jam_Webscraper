#include <iostream>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define MAXNM 32


int main() {
	printf("Program start.\n");
	if(freopen("C-small-practice.in", "r", stdin)){
		freopen("C-small-practice.out","w",stdout);
	}else{
		printf("file not found.\n");
		return 0;
	}

//	if(freopen("C-large-practice.in", "r", stdin)){
//		freopen("C-large-practice.out","w",stdout);
//	}else{
//		printf("file not found.\n");
//		return 0;
//	}

	int TestCases;
	scanf("%d", &TestCases);

	for(int caseID=1;caseID<=TestCases;caseID++){
		printf("Case #%d: ", caseID);
		int N,M;
		bool map[MAXNM][MAXNM];
		bool umap[MAXNM+1][MAXNM+1];
		int sizelist[MAXNM];
		for(int i=0;i<MAXNM;i++) sizelist[i]= 0;

		for(int i=0;i<MAXNM+1;i++){
			for(int j=0;j<MAXNM+1;j++){
				umap[i][j]=false;
			}
		}


		scanf("%d", &M);
		scanf("%d", &N);

		for(int i=0;i<M;i++){
			for(int j=0;j<N;j++){
				map[i][j] = false;
				umap[i][j] = true;
			}
		}
		char null;

		scanf("%c",&null);
		for(int i=0;i<M;i++){
			for(int j=0;j<N/4;j++){
				char c;
				int t;
				scanf("%c", &c);
				if(c<=57)
					t = atoi(&c);
				else
					t = (int)c - 55;
				if((t&1)==1)
					map[i][j*4+3] = true;
				if((t&2)==2)
					map[i][j*4+2] = true;
				if((t&4)==4)
					map[i][j*4+1] = true;
				if((t&8)==8)
					map[i][j*4] = true;
			}
			scanf("%c", &null);
		}
//		printf("\n");
//		for(int i=0;i<M+1;i++){
//			for(int j=0;j<N+1;j++){
//				if(umap[i][j])
//					printf("1");
//				else
//					printf("0");
//			}
//			printf("\n");
//		}

		for(int s=min(M,N);s>0;s--){
			for(int i=0;i<M;i++){
				for(int j=0;j<N;j++){
					if(s>1){
						bool r = true;
						if((s<=(M-i))&&(s<=(N-j))){
							bool t = true;
							for(int x=i;x<i+s;x++){
								if(x==i){
									t = map[i][j];
									for(int y=j;y<j+s-1;y++){
										if(map[x][y]==map[x][y+1]||!umap[x][y]||!umap[x][y+1]){
											r = false;
											break;
										}
									}
								}else{
									if(t!=map[x][j]){
										t = map[x][j];
										for(int y=j;y<j+s-1;y++){
											if(map[x][y]==map[x][y+1]||!umap[x][y]||!umap[x][y+1]){
												r = false;
												break;
											}
										}
									}else{
										r = false;
										break;
									}
								}
							}
						}else
							r = false;
						if(r){
							sizelist[s]++;
							for(int x=i;x<i+s;x++){
								for(int y=j;y<j+s;y++){
									umap[x][y]=false;
								}
							}
						}
					}else{
						if(umap[i][j]){
							sizelist[1]++;
							umap[i][j]=false;
						}
					}
				}
			}
		}

		int total = 0;
		for(int i=MAXNM;i>0;i--){
			if(sizelist[i]!=0)
				total++;
		}
		printf("%d\n", total);
		for(int i=MAXNM;i>0;i--){
			if(sizelist[i]!=0)
				printf("%d %d\n", i, sizelist[i]);
		}

	}

	fclose(stdin);
	fclose(stdout);
	printf("Program finish.\n");
	return 0;
}
