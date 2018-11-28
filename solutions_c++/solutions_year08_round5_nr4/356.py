#include <stdio.h>
#include <string.h>

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

void main(void){
	FILE* fin = fopen("knight.in","rt");
	FILE* fout = fopen("knight.out","wt");
	int N;
	fscanf(fin,"%d",&N);

	for(int i=0;i<N;i++){
		printf("Solving %d/%d...\n",i,N);

		int H,W,R,x,y;
		bool rocks[200][200];
		int C[200][200];

		memset(rocks,0,sizeof(rocks));
		memset(C,0,sizeof(C));

		fscanf(fin,"%d %d %d",&H, &W, &R);
		for(int j=0;j<R;j++) {
			fscanf(fin,"%d %d",&x, &y);
			rocks[x][y] = true;
		}
		
		C[1][1] = 1;
		for(x=2;x<=H;x++)
			for(y=2;y<=W;y++)
			{
				if (rocks[x][y]) continue;
				if((x>1)&&(y>2)) C[x][y] += C[x-1][y-2];
				if((x>2)&&(y>1)) C[x][y] += C[x-2][y-1];
				C[x][y] %= 10007;
			}


		fprintf(fout,"Case #%d: %d\n",i+1, C[H][W]);

	}

	fclose(fin);
	fclose(fout);
}