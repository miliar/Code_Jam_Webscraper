#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<iostream>
#include<cstring>
#include<fstream>
#include<sstream>

using namespace std;

int main(){
    
	char filename[32];
	char infile[32], outfile[32];
	int i, j, k, ncases, n, t,no=0;
	
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    fscanf(fp,"%d",&ncases);
    for (i = 0; i < ncases; i += 1)
    {
        fscanf(fp,"%d %d",&n, &k);
        k=k+1;
        t=k;
        for (j = 0; j < n; j++)
        {
            if(t%2==0)
                t=t/2;
            else {
                no=1;
                break;
            }
        }
        if(no)
            fprintf(ofp,"Case #%d: OFF\n",i+1);
        else
            fprintf(ofp,"Case #%d: ON\n",i+1);
        no=0;
    }

    fclose(fp);
    fclose(ofp);
    
    return 0;
}

