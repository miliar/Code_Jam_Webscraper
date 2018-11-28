#include<stdio.h>
#include<string.h>

int main()
{
	FILE *fin = fopen("A-small-attempt0.in","r");
	FILE *fo = fopen("out.txt","w");

	int t,n;
	char a;
	int b,k,i;
	int Opos, Bpos,cnt;
	int O[100]={0},B[100]={0},Ocnt,Bcnt;
	int j, time;
	int ONum[100]={0}, BNum[100]={0};

	fscanf(fin,"%d",&t);
	for(k = 0 ; k < t ; k++)
	{
		fscanf(fin,"%d",&n);
		Ocnt = 0; Bcnt = 0;
		memset(O, 0, sizeof(O));
		memset(B, 0, sizeof(B));
		memset(ONum, 0, sizeof(ONum));
		memset(BNum, 0, sizeof(BNum));

		for(i = 0 ; i < n ; i++)
		{
			fscanf(fin," %c %d",&a,&b);
			if(a == 'O')
			{
				O[Ocnt] = b;
				ONum[Ocnt++] = i;
			}
			else
			{
				B[Bcnt] = b;
				BNum[Bcnt++] = i;
			}
		}

		Opos = 1; Bpos = 1; cnt = 0;
		// start
		for(i = 0, j = 0, time = 0 ; i < Ocnt || j < Bcnt ; time ++)
		{
			if(Opos == O[i] && cnt == ONum[i] && i < Ocnt)
			{
				i++; cnt++;
				if(Bpos != B[j])
				{
					if(Bpos < B[j]) Bpos++;
					else Bpos--;
				}
			}
			else if(Bpos == B[j] && cnt == BNum[j] && j < Bcnt)
			{
				j++; cnt++;
				if(Opos != O[i])
				{
					if(Opos < O[i]) Opos++;
					else Opos--;
				}
			}
			else
			{
				if(Opos != O[i])
				{
					if(Opos < O[i]) Opos++;
					else Opos--;
				}
				if(Bpos != B[j])
				{
					if(Bpos < B[j]) Bpos++;
					else Bpos--;
				}
			}
		}

		fprintf(fo,"Case #%d: %d\n",k+1, time);
	}

	fcloseall();
	return 0;
}