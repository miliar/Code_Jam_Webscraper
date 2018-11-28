#include <iostream>

using namespace std;

#define MAX(x,y) (x)>(y)?(x):(y)

int main()
{
	FILE* inFP = fopen("B-large.in","rb");
	FILE* outFP = fopen("2_large.out","wb");

	int T,N,S,P;
	fscanf(inFP,"%d",&T);
	for(int t=1;t<=T;t++)
	{
		int count = 0;
		int Surprises = 0;
		fscanf(inFP,"%d", &N);
		fscanf(inFP,"%d", &S);
		fscanf(inFP,"%d", &P);

		for(int i=1;i<=N;i++)
		{
			int totalPoints;
			fscanf(inFP,"%d", &totalPoints);
			int NoSur = MAX(0,P-1);
			int Sur = MAX(0,P-2);
			if(totalPoints>=(P+2*NoSur))
			{
				count++;
			}
			else if(totalPoints>=(P+2*Sur) && Surprises<S)
			{
				Surprises++;
			}
		}

		fprintf(outFP,"Case #%d: %d\n",t,count+Surprises);
	}


	fclose(inFP);
	fclose(outFP);
	return 0;
}