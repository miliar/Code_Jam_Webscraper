#include<stdio.h>
#include<memory.h>
#include<string.h>
#include<math.h>
long long int p1, p2;
long int r;

int main()
{
	char nameoffile[32];
	char inputname[32], outputname[32];
	scanf("%s", nameoffile);
	strcpy(inputname, nameoffile); strcpy(outputname, nameoffile);
	strcat(inputname, ".in"); strcat(outputname, ".out");

	FILE *fp=fopen(inputname, "r"), *ofp=fopen(outputname, "w");
 
	long int i, j, tc;
	fscanf(fp, "%ld", &r);
	
	for(i=1;i<=r;i++) 
{

           fscanf(fp, "%Ld%d", &p1,&p2);

long long int zo = pow(2,p1);

long long int sd = (p2+1)%zo;

	if(sd == 0)
		fprintf(ofp, "Case #%d: %s\n", i, "ON");
     else
           fprintf(ofp, "Case #%d: %s\n", i, "OFF");
	}
	return 0;
}
