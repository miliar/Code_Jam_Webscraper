#include<stdio.h>
#include<memory.h>
#include<string.h>
int TestNo;
int R; //Run Times
int k; // Capacity
int N; //Number of groups
int G[10]; //Array Groups size

int main()
{
	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");

	int i,j, old_SP , new_SP;
	int group;
	long result, qout;
	int cnt;
	char recalc;
	fscanf(fp, "%d", &TestNo);
	for(i=1;i<=TestNo;i++) // For each test case
    {
       fscanf(fp, "%d%d%d",&R,&k, &N);
       for(j=1;j<=N;j++)// Fill the group sizes
       {
          fscanf(fp, "%d",&G[j-1]);
       }
       // initialize state
       result = 0;
       old_SP = 0;
       new_SP = 0;
       for(j=1 ; j<=R;j++) // For each run
       {
          group = 0;
          recalc = 0;
          old_SP = new_SP;
          if ((group + G[new_SP])<= k)
          {
              group+= G[new_SP];
              if (new_SP == (N - 1))
              {
                 new_SP = 0;
              }
              else
              {
                 new_SP++;
              }
              if (new_SP == old_SP)
              {
                  recalc = 1;
              }
              while (recalc == 0)
              {
                    if ((group + G[new_SP])<= k)
                    {
                        group+= G[new_SP];
                        if (new_SP == (N - 1))
                        {
                            new_SP = 0;
                        }
                        else
                        {
                            new_SP++;
                        }
                        if (new_SP == old_SP)
                        {
                             recalc = 1;
                        }
                    }
                    else
                    {
                        recalc = 1;
                    }
              }
			  result += group;
			  if (new_SP == 0)
			  {
				  qout = R / j;
				  result *= qout;
				  j *= qout;
			  }
          }
          else
          {
              break;
          }
          
       }
       fprintf(ofp, "Case #%d: %d\n", i,result);
    }
	return 0;
}
