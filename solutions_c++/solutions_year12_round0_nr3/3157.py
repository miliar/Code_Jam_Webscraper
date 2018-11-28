#include <stdio.h>

#define fr(x,N) for(x=0;x<N;x++)
#define fr1(x,N) for(x=1;x<=N;x++)

int main(int argc, char *argv[])
{
	FILE *fp,*o;
	fp = (argc<=1)?fopen("input.txt", "r"):fopen(argv[1],"r");
	o = fopen("output.txt","w+");

	if(fp) {
		int T;
		int i;

		fscanf(fp,"%d",&T);

		fr(i,T) {
			int x,y;
			int j,k;
			int s = 1;
			int c = 0;
			int ic, me = 10;

			fscanf(fp,"%d %d", &x,&y);
			c = x;
			while( c = c/10 ) { s++; me *= 10; }

			for(j=x;j<=y;j++)
			{
				int m = me;
				while((m=m/10)>=10) {
					int t = (j%m)*(me/m) + (j/m);
					if(j<t && t<=y && t>=x) {
						c++;
						//fprintf(o,"==%d %d %d==\n",j,t, c);
					}
				}
			}

			fprintf(o,"Case #%d: %d\n",i+1,c);
		}
		fclose(fp);
	}
	fclose(o);
	return 0;
}