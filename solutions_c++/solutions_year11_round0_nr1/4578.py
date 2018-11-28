#include <stdio.h>
#include <string.h>
#define SMFILE "D:\\lab\\codejam\\1\\A-small-attempt3.in"
#define LGFILE "D:\\lab\\codejam\\1\\A-large.in"
#define N 100
struct action{
	char robot;
	int  pos;
	int  order;
}action;
int calculate(int num, int step, struct action oAct[N], struct action bAct[N]);
int main()
{
	FILE * fp;
	if ((fp = fopen(LGFILE, "r")) == NULL)
	{
		printf("%s failed to open!\n", SMFILE);
	}
	
	int count = 0;
	int num = 0;
	int n = 0;
	int i,j,k;
	fscanf(fp, "%d\n", &count);
	struct action oAct[N];
	struct action bAct[N];
	struct action tAct;
	char tmp;
	while (!feof(fp))
	{
		num++;
		j = k = 0;

		memset(oAct, '\0', N*sizeof(struct action));
		memset(bAct, '\0', N*sizeof(struct action));
		
		fscanf(fp, "%d", &n);
		fscanf(fp, "%c", &tmp);
		for (i = 0; i < n; i++)
		{
			memset(&tAct, '\0', sizeof(struct action));
			fscanf(fp, "%c", &tAct.robot);
			fscanf(fp, "%d", &tAct.pos);
			fscanf(fp, "%c", &tmp);
			if (tAct.robot == 'O')
			{
				oAct[j].robot = tAct.robot;
				oAct[j].pos   = tAct.pos;
				oAct[j].order = i+1;
				j++;
			}
			else if (tAct.robot == 'B')
			{
				bAct[k].robot = tAct.robot;
				bAct[k].pos   = tAct.pos;
				bAct[k].order = i+1;
				k++;
			}
		}
		//puts("\n");
	
		calculate(num, n, oAct, bAct);
		if (num == count)
			return 0;
	}

	return 0;
}

int calculate(int num, int step, struct action oAct[N], struct action bAct[N])
{
	int i,j;
	int second = 0;
	int oPos = 1;
	int bPos = 1;
	int oPush = 0;
	int bPush = 0;
	i = j = 0;
	int exec = 1;
	while (1)
	{
		second++;
		if (oAct[i].order == exec)		 /**/
		{
			/*Orange robot*/
			if (oPos < oAct[i].pos)	/*执行完这一步已经在oPos+1位置了*/
			{
				oPos++;
			}
			else if (oPos == oAct[i].pos)	/*already in pos,next second will exec*/ 
			{
				//push
				i++;
				exec++;
			}
			else		/*back one step*/
			{
				oPos--;
			}
			
			/*Blue robot*/
			if (bPos < bAct[j].pos)	/*blue robot is not move to the right pos*/
			{
				bPos++;
			}
			else if(bPos == bAct[j].pos)	/*blue robot is moved to the right pos*/
			{
				//wait
			}
			else
			{
				bPos--;
			}
		}
		else if (bAct[j].order == exec)	/**/
		{
			/*Blue robot*/
			if (bPos < bAct[j].pos)
			{
				bPos++;
			}
			else if (bPos == bAct[j].pos)
			{
				//push
				j++;
				exec++;
			}
			else	/* back one step */	
			{
				bPos--;
			}

			/* Orange robot */
			if (oPos < oAct[i].pos)
			{
				oPos++;
			}
			else if (oPos == oAct[i].pos)	/*wait*/
			{

			}
			else
			{
				oPos--;
			}
		}
		if (exec == step + 1)
			break;
	}
	printf("Case #%d: %d\n", num, second);
	return 0;
}