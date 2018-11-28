#include <stdio.h>
#include <string.h>

void sortd(int* a, int c)
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
		int M,N;
		bool s[20][20];
		bool b[20][20];
		int map[20];
		bool used[20];

bool generate(int c) {
	if(c == M)
	{
		bool same = true;
		for(int j1=0;j1<M;j1++)
			for(int j2=0;j2<M;j2++)
				if (s[j1][j2])
					if(!b[map[j1]][map[j2]])
						same = false;
		return same;
	}
	else
	{
		for(int i=0;i<N;i++)
			if(used[i] == false)
			{
				used[i] = true;
				map[c] = i;
				if (generate(c+1)) return true;
				used[i] = false;
			}
		return false;
	}
}
void main(void){
	FILE* fin = fopen("d.in","rt");
	FILE* fout = fopen("d.out","wt");
	int totalCases,i,j,k;
	fscanf(fin,"%d",&totalCases);

	for(int Case=0;Case<totalCases;Case++){
		printf("Solving %d/%d...\n",Case,totalCases);


		memset(s,0,sizeof(s));
		memset(used,0,sizeof(used));
		memset(map,0,sizeof(map));
		memset(b,0,sizeof(b));
		fscanf(fin, "%d",&N);
		for(i=0;i<N-1;i++)
		{
			fscanf(fin, "%d %d",&j,&k);
			j--;k--;
			b[j][k] = true; 
			b[k][j] = true;
		}
		fscanf(fin, "%d",&M);
		for(i=0;i<M-1;i++)
		{
			fscanf(fin, "%d %d",&j,&k);
			j--;k--;
			s[j][k] = true; 
			s[k][j] = true;
		}


		if(generate(0))
			fprintf(fout,"Case #%d: YES\n",Case+1);
		else
			fprintf(fout,"Case #%d: NO\n",Case+1);
	
	}

	fclose(fin);
	fclose(fout);
}