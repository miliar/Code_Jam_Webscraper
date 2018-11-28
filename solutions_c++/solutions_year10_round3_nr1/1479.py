#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
#include <set>
#include <sstream>

using namespace std;

 int n, m;
long int r;
long int a1[10000][2];
char a[100][100][100],b[100][100];

int main()
{   

long int t1,t2,loc;
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");

	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
 
	int i, j, tc;
	fscanf(fp, "%d", &r);
		
	
	for(i=1;i<=r;i++) 
{

loc = 0;
int r1;
	fscanf(fp, "%d", &r1);
	for (int j1 = 0; j1 < r1 ; j1++)
	{
        fscanf(fp, "%ld%ld", &t1,&t2);

        a1[j1][0] = t1;
        a1[j1][1] = t2;
        }

	for (int j2 = 0; j2 < r1 ; j2++)
	{
        	for (int j3 = j2; j3 < r1 ; j3++){
        if ( ((a1[j2][0] - a1[j3][0]) < 0 && (a1[j2][1] - a1[j3][1])  > 0) || ((a1[j2][0] - a1[j3][0]) < 0 && (a1[j2][1] - a1[j3][1])  > 0) )
        loc++;
        }
        }






fprintf(ofp, "Case #%d: %ld\n", i, loc);
          
	}
	return 0;
}

