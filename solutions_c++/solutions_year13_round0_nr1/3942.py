#include<stdio.h>
#include<stdlib.h>

int	main()
{
	FILE *f1,*f2;
	int error;
	error = fopen_s(&f1,"A-large.in","r");
	if(error == -1)
		printf("eroare la deschidere");
	error = fopen_s(&f2,"A-large.out","w");
	if(error == -1)
		printf("eroare la deschidere2");

	int i,j,k,N;
	int oline,ocolumn[4],xline,xcolumn[4],odiag,xdiag,odiags,xdiags;
	bool owon,xwon,incomplete;
	char c;

	fscanf_s(f1,"%d",&N);

	for(i=0;i<N;i++)
	{
		incomplete = false;
		owon = false;
		xwon = false;
		odiag = xdiag = 0;
		odiags = xdiags = 0;
		for(j=0;j<4;j++){
			xcolumn[j]=0;
			ocolumn[j]=0;
		}

		for(j=0;j<4;j++){
			c=fgetc(f1);
			oline = xline = 0;
			for(k=0;k<4;k++){
				c=fgetc(f1);
				switch (c){
					case 'T':
						xcolumn[k]++;
						ocolumn[k]++;
						xline ++;
						oline ++;
						if(k==j)
						{
							odiag ++;
							xdiag ++;
						}
						if( k == 3-j)
						{
							odiags ++;
							xdiags ++;
						}
						break;
					case '.':
						incomplete = true;
						break;
					case 'O':
						ocolumn[k]++;
						oline++;
						if(k==j)
						{
							odiag ++;
						}
						if( k == 3-j)
						{
							odiags ++;
						}
						break;
					case 'X':
						xcolumn[k] ++;
						xline ++;
						if(k==j)
						{
							xdiag ++;
						}
						if( k == 3-j)
						{
							xdiags ++;
						}
						break;
					default:
						break;
				}
			}
			if(xdiag == 4 || xdiags == 4 || xline == 4){
				xwon = true;
			}
			else if(odiag == 4 || odiags == 4 || oline == 4){
				owon = true;
			}
		}
		for(j=0;j<4;j++){
			if(xcolumn[j] == 4){
				xwon = true;
			}
			else if(ocolumn[j] == 4){
				owon = true;
			}
		}
		fprintf_s(f2,"Case #%d: ",i+1);
		if(xwon)
		{
			fprintf_s(f2,"X won\n");
		}
		else if(owon)
		{
			fprintf_s(f2,"O won\n");
		}
		else if(incomplete)
		{
			fprintf_s(f2,"Game has not completed\n");
		}
		else
		{
			fprintf_s(f2,"Draw\n");
		}
		c=fgetc(f1);
		
	}
return 0;
}