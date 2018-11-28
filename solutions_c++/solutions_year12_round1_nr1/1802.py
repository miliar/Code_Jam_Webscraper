#include <iostream>

using namespace std;

#define MIN(x,y) (x)<(y)?(x):(y)

int main()
{
	FILE* inFP = fopen("A-small-attempt0.in","rb");
	FILE* outFP = fopen("A-small-attempt0.out","wb");

	int T = 0;
	fscanf(inFP,"%d",&T);

	for(int t=1;t<=T;t++)
	{
		int TotalChar = 0;
		int TypedChar = 0;

		fscanf(inFP,"%d%d",&TypedChar, & TotalChar);
		float *P;
		P = new float[TypedChar+1];
		for(int k=1;k<=TypedChar;k++)
			fscanf(inFP,"%f",&P[k]);
		
		float min = TotalChar-TypedChar+1;
		int i;
		int keepMin = min;

		for(i=TypedChar;i>1;i--)
		{
			//min keystrokes in case i want to keep this char
			float keep = P[i]*min + (1-P[i])*(keepMin+TotalChar+1);
			float del  = (TypedChar-i+1)*2+(TotalChar-TypedChar+1);
			if(keep>del)
			{
				min = del;
				keepMin = del;
			}
			else
			{
				min = keep;
			}
		}

		float keep = P[i]*min + (1-P[i])*(keepMin+TotalChar+1);
		float del  = TotalChar+2;
		min = MIN(keep,del);
		
		fprintf(outFP,"Case #%d: %0.6f\n",t,min);
		delete[] P;		
	}

	fclose(inFP);
	fclose(outFP);
	return 0;
}