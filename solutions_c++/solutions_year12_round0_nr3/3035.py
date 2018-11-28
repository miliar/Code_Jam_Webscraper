#include <stdio.h>

void main()
{
	FILE *in, *out;
	int i, j, k, l, N;
	int start, end, length, num, cnt;
	char str[10];

	in = fopen("C-small-attempt0.in","r");
	out = fopen("C-small-attempt0.out","w");
	
	fscanf(in,"%d",&N);

	for(i=0;i<N;i++) {

		fscanf(in, "%d %d",&start, &end);
		
		cnt=0;

		for(j=start; j<=end; j++) {

			length = sprintf(str,"%d%d",j,j)/2;
		
			for(k=0; k<length; k++) {

				num=0;
				for(l=k;l<k+length;l++) {
					num *= 10;
					num += str[l]-'0';
				}

				if(  num > j && num >= start && num <= end)	{
					cnt++;
				}
			}
		}

		fprintf(out,"Case #%d: %d\n",i+1,cnt);
	}
}