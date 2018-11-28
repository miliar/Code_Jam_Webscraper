#include <stdio.h>

int progs[2][200];
int progtime[2][200];
int proglen[2];
int progptr[2];
int botpos[2];

int main(void)
{

    FILE *f;
	f=fopen("A-large.in","r");

	int time=0;
	int tc;
	fscanf(f,"%d\n",&tc);
	for(int t=0;t<tc;t++)
	{
		int N;
		fscanf(f,"%d ",&N);

		proglen[0] = 0;
		proglen[1] = 0;
		time=0;

		for(int i=0;i<N;i++)
		{
			int c;
			char buffer[1024];
			fscanf(f,"%s %d",&buffer,&c);

			int side=-1;
			if (buffer[0]=='O') side=0;
			if (buffer[0]=='B') side=1;

            if (buffer[1] || side==-1) return 0;

			progtime[side][proglen[side]] = time;
			progs[side][proglen[side]++] = c;
			time++;
		};

		botpos[0]=1;
		botpos[1]=1;
		progptr[0] =0;
		progptr[1] =0;

		int outtime=0;
		int count=0;
		while(progptr[0] < proglen[0] || progptr[1] < proglen[1])
		{
			int origouttime = outtime;
			for(int side=0;side<2;side++)
			{
				if (progptr[side] < proglen[side])
				{
					if (botpos[side] > progs[side][progptr[side]])
					{
						botpos[side]--;
//						printf("moveleft   ");
					}
					else
					{
						if (botpos[side] < progs[side][progptr[side]])
						{
							botpos[side]++;
//							printf("moveright  ");
						}
						else
						{


							if (botpos[side] == progs[side][progptr[side]])
							{
								// push button
								if (origouttime==progtime[side][progptr[side]])
								{
									// push and next
									progptr[side]++;
									outtime++;
//									printf("push        ");
								}
								else
								{
//									printf("stay        ");
								};
							};
						}
					};
				}

			};
//			printf("\n");
			count++;
		};
		printf("Case #%d: %d\n",t+1,count);

	};





	return 1;
};