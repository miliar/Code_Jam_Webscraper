#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#include<afxwin.h>
/*
int n, m, r;
char dat[6000][32];
char a[1024];
bool pos[32][32];
int ans;
*/
struct Plant{
	int x;
	int y;
	int r;
};

int main()
{
	// Get Time
	DWORD   dwStart=GetTickCount();  
	// Open File
	char filename[32]="D-small-attempt1";
	char infile[32], outfile[32];
	//scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");


	// Read Data
	int C;
	fscanf(fp, "%d", &C);
	// Read Matrix
	//for(i=1;i<=n;i++) fscanf(fp, "%s", &dat[i][1]);
	
	for(int tc=1;tc<=C;tc++)
	{
		int N;
		fscanf(fp, "%d", &N);
		// Init the array
		//memset(pos, false, sizeof(pos));
		// Get Data
		Plant p[41];
		int i, j;
		for(i=1; i<=N; i++){
			fscanf(fp, "%d %d %d", &p[i].x, &p[i].y, &p[i].r);
		}

		//
		double ra=0;
		if(N==1){
			ra=p[1].r;
		}
		else if(N==2){
			if(p[1].r>p[2].r){
				ra=p[1].r;
			}
			else{
				ra=p[2].r;
			}
		}
		else if(N==3){
			double dis12, dis23, dis31;
			dis12=sqrt((p[1].x-p[2].x)*(p[1].x-p[2].x) + (p[1].y-p[2].y)*(p[1].y-p[2].y))+p[1].r+p[2].r;
			dis23=sqrt((p[3].x-p[2].x)*(p[3].x-p[2].x) + (p[3].y-p[2].y)*(p[3].y-p[2].y))+p[3].r+p[2].r;
			dis31=sqrt((p[1].x-p[3].x)*(p[1].x-p[3].x) + (p[1].y-p[3].y)*(p[1].y-p[3].y))+p[1].r+p[3].r;

			if(dis12<dis23){
				if(dis12<dis31){
					ra=dis12/2.0;
					if(p[3].r>ra)
						ra=p[3].r;
				}
				else{
					ra=dis31/2.0;
					if(p[2].r>ra)
						ra=p[2].r;
				}
			}
			else{
				if(dis23<dis31){
					ra=dis23/2.0;
					if(p[1].r>ra)
						ra=p[1].r;
				}
				else{
					ra=dis31/2.0;
					if(p[2].r>ra)
						ra=p[2].r;
				}
			}

		}
		printf("Case #%d: %.6lf\n", tc, ra);
		fprintf(ofp, "Case #%d: %.6lf\n", tc, ra);
	}
	DWORD   dwEnd=GetTickCount();  
	printf("Time: %d\n", dwEnd-dwStart);
	return 0;
}
