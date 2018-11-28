#include <stdio.h>
#include <string.h>

const int ALPH_MAX = 'z' - 'a' + 1;
const int LENGH_MAX = 15;
//const int PATTERN_MAX = 500;
//const int VOCAB_MAX = 5000;
const int PATTERN_LENGH_MAX = LENGH_MAX * (ALPH_MAX +2);

int L, D, N;

char** vocab;

bool*** M;

int* count;

bool isAplh(char a){
	return ('a' <= a && a <= 'z');
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d %d %d",&L,&D,&N);

	vocab = new char*[D];
	for(int i=0; i<D; ++i){
		vocab[i] = new char[L+1];
		scanf("%s",vocab[i]);
	}
	
	M = new bool**[N];
	char pattert[PATTERN_LENGH_MAX+1];
	for(int i=0; i<N; ++i){
		M[i] = new bool*[L];
		for(int j=0; j<L; ++j){
			M[i][j] = new bool[ALPH_MAX];
			memset(M[i][j],0,ALPH_MAX*sizeof(bool));
		}
		scanf("%s",pattert);
		char * point = pattert;
		for(int j=0; j<L; ++j){
			if(isAplh(*point))
				M[i][j][*point - 'a'] = true;
			else{
				point++;
				while(isAplh(*point)){
					M[i][j][*point - 'a'] = true;
					point++;
				}
			}
			point++;
		}
	}

	count = new int[N];
	memset(count,0,N*sizeof(int));
	for(int i=0; i<D; ++i){
		for(int t=0; t<N; ++t){
			int j;
			for(j=0; j<L; ++j){
				char c = vocab[i][j] - 'a';
				if(!M[t][j][c])
					break;
			}
			if(j>=L)
				count[t]++;
		}
	}

	//printf("%d %d %d\n",L,D,N);
	//for(int i=0; i<D; ++i){
	//	printf("%s\n",vocab[i]);
	//}

	//for(int i=0; i<N; ++i){
	//	for(int j=0; j<L; ++j){
	//		for(int t=0; t<ALPH_MAX; ++t){
	//			printf("%d ",(int)M[i][j][t]);
	//		}
	//		printf("\n");
	//	}
	//	printf("\n");
	//}

	for(int i=0; i<N; ++i){
		printf("Case #%d: %d\n",i+1,count[i]);
	}

	return 0;
}