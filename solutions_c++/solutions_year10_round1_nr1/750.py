#include <iostream>
using namespace std;

char Map[55][55];
char NewMap[55][55];
int dx[] = {0,0,1,-1,1,-1,1,-1};
int dy[] = {1,-1,0,0,1,-1,-1,1};
int n,k;

void ReLocate(){
	int i,j;
	for(j = 0; j < n; j++){
		char temp[55];
		int index = 0;
		for(i = 0; i < n; i++){
			if(NewMap[i][j] != '.')
				temp[index++] = NewMap[i][j];
		}

		int tIndex = 0;
		for(i = 0; i < n; i++){
			if(i < n-index)NewMap[i][j] = '.';
			else NewMap[i][j] = temp[tIndex++];
		}
	}
}

int Solve(){
	int ans = 0;
	int i,j,kk;
	char c = 'B';

	bool findedBlue,findedRed;
	bool finded = false;
	for(i = 0; i < n && !finded; i++)
	{
		for(j = 0; j < n && !finded; j++)
		{
			if(NewMap[i][j] == c){
				for(kk = 0; kk < 8 && !finded; kk++)
				{
					int Count = 1;
					int ci = i+dx[kk];
					int cj = j+dy[kk];
					while(ci>=0 && ci <n && cj>=0 && cj < n && NewMap[ci][cj] == c){
						Count++;
						cj += dy[kk];
						ci += dx[kk];
						if(Count >= k)
						{
							finded = true;
							break;
						}
					}

				}
			}
		}
	}
	findedBlue = finded;

	finded = false;
	c = 'R';
	for(i = 0; i < n && !finded; i++)
	{
		for(j = 0; j < n && !finded; j++)
		{
			if(NewMap[i][j] == c){
				for(kk = 0; kk < 8 && !finded; kk++)
				{
					int Count = 1;
					int ci = i+dx[kk];
					int cj = j+dy[kk];
					while(ci>=0 && ci <n && cj>=0 && cj < n && NewMap[ci][cj] == c){
						Count++;
						cj += dy[kk];
						ci += dx[kk];
						if(Count >= k)
						{
							finded = true;
							break;
						}
					}

				}
			}
		}
	}
	findedRed = finded;

	if(findedBlue && findedRed)return 2;
	if(findedBlue && !findedRed)return 1;
	if(!findedBlue && findedRed)return -1;
	if(!findedBlue && !findedRed)return 0;
}

int main(){
 	FILE *fin = fopen("A-large.in","r");
 	FILE *fout = fopen("Out.out","w");
//	FILE *fin = stdin;
	//FILE *fout = stdout;

	int t,tt,i,j;
	tt = 0;
	fscanf(fin,"%d",&t);
	while(t--){
		tt++;

		fscanf(fin,"%d %d",&n,&k);
		memset(Map,0,sizeof(Map));
		memset(NewMap,0,sizeof(NewMap));
		for(i = 0; i < n; i++)
			fscanf(fin,"%s",Map[i]);

		for(i = 0; i < n; i++)
		{
			for(j = 0; j < n; j ++)
				NewMap[i][j] = Map[n-j-1][i];
		}



		ReLocate();

// 		for(i = 0; i < n; i++)
// 			fprintf(fout,"%s\n",NewMap[i]);
// 		fprintf(fout,"\n");

		int ans = Solve();

		if(ans == 2)
			fprintf(fout,"Case #%d: Both\n",tt);
		if(ans == 1)
			fprintf(fout,"Case #%d: Blue\n",tt);
		if(ans == -1)
			fprintf(fout,"Case #%d: Red\n",tt);
		if(ans == 0)
			fprintf(fout,"Case #%d: Neither\n",tt);



	}


	fclose(fin);
	fclose(fout);
	return 0;
}