#include <stdio.h>
#include <string.h>

		bool broken[20][20];

void sort(int* a, int c)
{
	int t;
	for(int i=1;i<c;i++)
		for(int j=i-1;(j>=0)&&(a[j+1]<a[j]);j--)
		{
			t = a[j+1];
			a[j+1] = a[j];
			a[j] = t;
		}
}


void expand(int scheme, int N, int* result)
{
	for(int i=0;i<N;i++)
	{
		result[i] = scheme % 2;
		scheme /= 2;
	}
}

int count(int scheme, int N)
{
	int c = 0;
	for(int i=0;i<N;i++){
		c += scheme % 2;
		scheme /= 2;
	}
	return c;

}
bool schemeOK(int scheme, int N)
{
	int current[20];
	expand(scheme,N,current);
	bool OK = true;
	for(int i=1;i<N;i++)
		if ((current[i]==1)&&(current[i-1]==1)) OK = false;
	return OK;
}

bool chairsOK(int row, int scheme, int N)
{
	int current[20];
	expand(scheme, N, current);
	bool fail = false;
	for(int k=0;k<N;k++) if ((current[k] == 1)&&(broken[row][k])) fail = true;
	return (fail == false);
}

void main(void){
	FILE* fin = fopen("cheating.in","rt");
	FILE* fout = fopen("cheating.out","wt");

	int Num;
	fscanf(fin,"%d",&Num);
	for(int i0=0;i0<Num;i0++){
		printf("Solving %d/%d...\n",i0,Num);

		int M,N,i,j,k;
		memset(broken,0,sizeof(broken));

		fscanf(fin, "%d %d\n", &M, &N);
		for(j=0;j<M;j++){
			char c[20];
 			fscanf(fin, "%s\n", c);
			for(int k=0;k<N;k++)
				if (c[k]=='x') broken[j][k] = true;
		}

		int D[20][2048];
		int current[20];

		int schemes = 1; for(int j=0;j<N;j++) schemes *= 2;
		for(j=0;j<schemes;j++)
		{
			if (schemeOK(j,N)&&chairsOK(0,j,N)) D[0][j] = count(j,N); else D[0][j] = -1000;
		}

		int P;
		for(i=1;i<M;i++)
			for(P=0;P<schemes;P++)
			{
				D[i][P] = -1000;
				if (!schemeOK(P,N)) continue;
				if (!chairsOK(i,P,N)) continue;
				
				expand(P, N, current);
				int previous[20];
				for(k=0;k<schemes;k++){
					if (!schemeOK(k,N)) continue;
					expand(k,N,previous);
					bool OK = true;
					if ((current[0]==1)&&(previous[1]==1)) OK = false;
					if ((current[N-1]==1)&&(previous[N-2]==1)) OK = false;
					for(int x=1;x<N-1;x++)
						if ((current[x] == 1)&&( (previous[x-1]==1 )||( previous[x+1]==1)   )) OK = false;
					if (OK)
						if ((D[i-1][k]+count(P,N))>D[i][P])
							D[i][P] = D[i-1][k]+count(P,N);

				}
			}

		int r = 0;
		for(i=0;i<schemes;i++)
			if (D[M-1][i]>r) r= D[M-1][i];
		fprintf(fout,"Case #%d: %d\n",i0+1, r);

	}

	fclose(fin);
	fclose(fout);
}