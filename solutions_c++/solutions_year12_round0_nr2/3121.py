#include <stdio.h>

#define fr(x,N) for(x=0;x<N;x++)
#define fr1(x,N) for(x=1;x<=N;x++)

int main(int argc, char *argv[])
{
	FILE *fp,*o;
	fp = (argc<=1)?fopen("input.txt", "r+"):fopen(argv[1],"r+");
	o = fopen("output.txt","w+");

	if(fp) {
		int T;
		int i;
		int j,k;
		fscanf(fp,"%d",&T);
		fr(i,T) {
			int N,S,p;
			int c = 0,s=0;
			fscanf(fp,"%d %d %d",&N,&S,&p);

			fr(j,N) {
				int x,y,z;
				short flag = 0;

				fscanf(fp,"%d",&x);

				for(y=3,z=p;y>1 && z<=x;y=k){

					y = (x - z)/2;
					k = (y>z)?y-z+1:z-y;

					if(k>2) {
						if( y < z) break;
						z++;
					}
					else if (k==2) {
						if(s<S) {
							s++; c++;
							flag=1;
						}
						else if( y < z) break;

						z++;
					}
					else {
						if(!flag) {
							c++; //printf("Count:%d\n",c);
							flag = 0;
						}
						else s--;

						break;
					}
				}
			}
			fprintf(o,"Case #%d: %d\n",i+1, c);
		}
	}

	return 0;
}