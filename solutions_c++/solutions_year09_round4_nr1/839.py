#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<afxwin.h>
/*
int n, m, r;
char dat[6000][32];
char a[1024];
bool pos[32][32];
int ans;
*/
//int dat[40][40]={0};

int main()
{
	// Get Time
	DWORD   dwStart=GetTickCount();  
	// Open File
	char filename[32]="A-large";
	char infile[32], outfile[32];
	//scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");


	// Read Data
	int T;
	fscanf(fp, "%d", &T);
	// Read Matrix
	//for(i=1;i<=n;i++) fscanf(fp, "%s", &dat[i][1]);
	
	for(int tc=1;tc<=T;tc++)
	{
		int N;
		fscanf(fp, "%d", &N);
		// Init the array
		//memset(pos, false, sizeof(pos));
		// Get Data
		int data[41]={0};
		int i, j;
		fgetc(fp);
		for(i=1; i<=N; i++){
			for(j=1; j<=N; j++){
				int temp=fgetc(fp)-'0';
				if(temp==1){
					data[i]=j;
				}
			}
			fgetc(fp);
		}
		/*for(i=0; i<N; i++){
			printf("%d\n", data[i]);
		}*/

		int count=0;
		int ok=0;
		for(i=1; i<=N; i++){
			// Not match
			if(data[i]>i){
				// find match
				for(j=i; j<=N; j++){
					if(data[j]<=i){
						// swap
						int time = j-i;
						for(int k=0; k<time; k++){
							int temp=data[j-k-1];
							data[j-k-1]=data[j-k];
							data[j-k]=temp;
						}
						count+=time;
						i=0;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d\n", tc, count);

		// Write File
		fprintf(ofp, "Case #%d: %d\n", tc, count);
	}
	DWORD   dwEnd=GetTickCount();  
	printf("Time: %d\n", dwEnd-dwStart);
	return 0;
}
