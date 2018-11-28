#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

int main () {
    FILE *fin  = fopen ("BotTrust.in", "r");
    FILE *fout = fopen ("BotTrustL.out", "w");
    int T;
    fscanf(fin, "%d", &T);
    for(int caseN = 1; caseN<=T; caseN++)
    {
		int N;
		fscanf(fin, "%d", &N);
		int code[N];
		for(int i=0; i<N; i++)
		{
			char rbt;
			int btn;
			fscanf(fin, " %c %d", &rbt, &btn);
			//printf(" %c %d", rbt, btn);
			if(rbt=='O')
				btn*=-1;
			code[i]=btn;
		}
		
		int O=1, B=1;
		int OT=0, BT=0;
		int totalT=0;
		//printf("\n");
		for(int i=0; i<N; i++)
		{
			if(code[i]<0)
			{
				OT += (code[i]*-1 - O > 0)?code[i]*-1 - O:O - code[i]*-1;
				if(OT<BT)
					OT=BT;
				OT++;
				O=code[i]*-1;
			}
			else
			{
				BT += (code[i] - B > 0)?code[i] - B:B - code[i];
				if(BT<OT)
					BT=OT;
				BT++;
				B=code[i];
			}
			//printf("%d %d %d %d\n", O, B, OT, BT);
		}
		fprintf(fout, "Case #%d: %d\n", caseN, (OT>BT)?OT:BT);
	}
    return 0;
}
