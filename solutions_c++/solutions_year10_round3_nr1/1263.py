#include<iostream>
#include<memory.h>
#include<string.h>

using namespace std;

int cases,tc, n, i, j, temp;
int x[1000],y[1000],ans=0;

int main()
{
    char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
    
    fscanf(fp, "%d", &cases);
	for(tc=1;tc<=cases;tc++)
	{
        ans=0;
        fscanf(fp, "%d", &n);
        for (i=0;i<n;i++) fscanf(fp, "%d%d", &x[i], &y[i]);
        for (i=0;i<n;i++) for(j=i+1;j<n;j++) if (x[i]>x[j]) { temp=x[i]; x[i]=x[j]; x[j]=temp; temp=y[i]; y[i]=y[j]; y[j]=temp; }
        for (i=0;i<n;i++) for(j=i+1;j<n;j++) if ((y[i]>y[j]) && ((x[i]-y[i])!=(x[j]-y[j]))) ans++;
        //cout<<ans<<endl;
        //for (i=0;i<n;i++) cout<<x[i]<<"\t"<<y[i]<<endl;
       	fprintf(ofp, "Case #%d: %d\n", tc, ans);
    }
    //system("pause");
    return 0;
}
