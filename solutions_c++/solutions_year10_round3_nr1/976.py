#include <string>
#include <vector>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <iostream>
#include <cstdio>
using namespace std;


int main(){

	char filename[32];
	char infile[32], outfile[32];
	int i, j, k, ncases, n, t,no=0;
	const int N=1000;
	int a[N],b[N];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	//printf("%s",infile);
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    fscanf(fp,"%d",&ncases);
    for (i = 0; i < ncases; i += 1)
    {
        int x=0;
        fscanf(fp,"%d",&n);
        for (j = 0; j < n; j++)
        {
            fscanf(fp,"%d %d",&a[j], &b[j]);
        }
        for (j = 0; j < n-1; j++)
        {
            for (k = j+1; k < n; k++)
            {
                if( (a[j]-a[k])*(b[j]-b[k])<0 )
                	x++;
            }
        }
        //cout<<x<<endl;
        fprintf(ofp,"Case #%d: %d\n",i+1,x);
    }

    fclose(fp);
    fclose(ofp);

    return 0;
}
