// b.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"
#include <stdlib.h>


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* f = fopen("C-Small.in", "r+");
	if(f==0) return 1;
	FILE* o = fopen("C-Small.out", "w+");
	int T;
	fscanf(f, "%d", &T);
	for(int t=0; t<T; t++){
		int m, n;
		fscanf(f, "%d %d\n", &m, &n);
		bool** mas = new bool* [m];
		for(int i=0; i<m; i++){
			mas[i]=new bool[n];
			for(int j=0; j<n/4; j++){
				char c;
				fscanf(f, "%c", &c);
				int val;
				if((c>='0')&&(c<='9'))
					val = c - '0';
				else val = 10 + c - 'A';
				for(int q=0; q<4; q++){
					mas[i][j*4+q]=val&(1<<(3-q));
				}
			}
			fscanf(f, "\n");
		}
		/*for(int i=0; i<m; i++){
			for(int j=0; j<n; j++)
				printf("%c", mas[i][j]?' ':'*');
			puts("");
		}*/
		bool** used = new bool*[m];
		for(int i=0; i<m; i++){
			used[i] = new bool[n];
			for(int j=0; j<n; j++)
				used[i][j]=false;
		}

		int N=0;
		int** ans=NULL;

		for(int c = __min(m, n); c>1; c--){//>1 !!!!!!
			long count = 0;

			for(int i=0; i<=m-c; i++)
				for(int j=0; j<=n-c; j++){

					bool is = true;

					for(int h=0; (h<c)&&is; h++)
						for(int w=0; w<c; w++)
							if(used[i+h][j+w]){
								is = false;
								break;
							};

					for(int h=0; h<c; h++){
						for(int w=0; w<c-1; w++)
							if(/*used[i+h][j+w]||*/ !(mas[i+h][j+w]^mas[i+h][j+w+1])){
								is = false;
								break;
							};
						if(!is) break;
					}
					for(int h=0; h<c-1; h++)
						if(!(mas[i+h][j]^mas[i+h+1][j])){
							is = false;
							break;
						};

					if(is){
						count++;
						for(int h=0; h<c; h++)
							for(int w=0; w<c; w++)
								used[i+h][j+w]=true;
					}

				};
			if(count){
				N++;
				ans = (int**)realloc(ans, sizeof(int*)*N);
				ans[N-1] = new int[2];
				ans[N-1][0]=c;
				ans[N-1][1]=count;
			}

		}

		N++;
		ans = (int**)realloc(ans, sizeof(int*)*N);
		ans[N-1] = new int[2];
		ans[N-1][0]=1;
		int count = 0;
		for(int i=0; i<m; i++)
			for(int j=0; j<n; j++)
				if(!used[i][j]) count++;
		ans[N-1][1]=count;
		if(!count){
			delete ans[N-1];
			N--;
			ans = (int**)realloc(ans, sizeof(int*)*N);
		}

		fprintf(o, "Case #%d: %d\n", t+1, N);
		for(int i=0; i<N; i++)
			fprintf(o, "%d %d\n", ans[i][0], ans[i][1]);

		for(int i=0; i<N; i++)
			delete ans[i];
		delete ans;
		for(int i=0; i<m; i++){
			delete used[i];
			delete mas[i];
		}

		delete used;
		delete mas;

	}
	fclose(o);
	fclose(f);
	return 0;
}

