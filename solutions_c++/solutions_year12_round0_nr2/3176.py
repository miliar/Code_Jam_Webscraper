#include<stdio.h>
#include<memory.h>
#include<string.h>

int data[101];
int main()
{
    char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
	
	int t;
	fscanf(fp,"%d",&t);
	for(int i = 1;i <= t;i++)
	{
        int ans(0);
        int n,s,p;
        fscanf(fp,"%d%d%d",&n,&s,&p);
        int tmp1 = p *3 - 2;
        int tmp2 = p * 3 - 4;
        if(p == 1)
        {
            for(int j =0;j != n;j++)
            {
                int tmp;
                fscanf(fp,"%d",&tmp);
                if(tmp > 0)
                ans ++;
            }
            fprintf(ofp, "Case #%d: %d\n", i, ans);
            continue;
        }
        for(int j =0;j != n;j++)
        {
            int tmp;
            fscanf(fp,"%d",&tmp);
            if(tmp >= tmp1)
            {
                ans ++;
                continue;
            }
            if(tmp >= tmp2 && s)
            {
                ans ++;
                s--;
                continue;
            }
        }
        fprintf(ofp, "Case #%d: %d\n", i, ans);
    }
    return 0;
}
