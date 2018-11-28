#include <cstdio>
#include <cstring>
#define MAX 55

int ncases, tabsize, kjoin, t;
char tab[MAX][MAX], newtab[MAX][MAX];

void shiftright()
{
	for(int i=0; i<tabsize; i++)
		for(int j=tabsize-2; j>=0; j--)
		{
			int k=j;
			while(tab[i][k]!='.' && k+1!=tabsize && tab[i][k+1]=='.')
			{
				tab[i][k+1]=tab[i][k];
				tab[i][k]='.';
				k++;
			}
		}
	/*for(int i=0; i<tabsize; i++)
		printf("%s\n", tab[i]);*/
}

void rotate()
{
	for(int i=0; i<tabsize; i++)
		for(int j=0; j<tabsize; j++)
			newtab[i][j]=tab[tabsize-j-1][i];
	/*for(int i=0; i<tabsize; i++)
		printf("%s\n", newtab[i]);
	printf("\n\n");*/
}

void detect()
{
	bool blue=false, red=false;
	for(int i=tabsize-1; i>=0; i--)
	{
		if(red && blue) break;
		for(int j=0; j<tabsize; j++)
		{
			if(red && blue) break;
			if(newtab[i][j]=='.') break;
			char curcolor=newtab[i][j];
			int currow;
			
			currow=0;
			//test horizontal
			for(int k=0; k<kjoin; k++)
			{
				if(j+k<tabsize && newtab[i][j+k]==curcolor)
					currow++;
				else
					break;
			}
			if(currow==kjoin)
			{
				if(curcolor=='B')
					blue=true;
				else
					red=true;
			}
			
			currow=0;
			//test vertical
			for(int k=0; k<kjoin; k++)
			{
				if(i-k>=0 && newtab[i-k][j]==curcolor)
					currow++;
				else
					break;
			}
			if(currow==kjoin)
			{
				if(curcolor=='B')
					blue=true;
				else
					red=true;
			}
			
			currow=0;
			//test diagonal up
			for(int k=0; k<kjoin; k++)
			{
				if(j+k<tabsize && i-k>=0 && newtab[i-k][j+k]==curcolor)
					currow++;
				else
					break;
			}
			if(currow==kjoin)
			{
				if(curcolor=='B')
					blue=true;
				else
					red=true;
			}
			
			currow=0;
			//test diagonal down
			for(int k=0; k<kjoin; k++)
			{
				if(j+k<tabsize && i+k<tabsize && newtab[i+k][j+k]==curcolor)
					currow++;
				else
					break;
			}
			if(currow==kjoin)
			{
				if(curcolor=='B')
					blue=true;
				else
					red=true;
			}
		}
	}
	if(red && blue)
		printf("Case #%d: Both\n", t+1);
	if(red && !blue)
		printf("Case #%d: Red\n", t+1);
	if(!red && blue)
		printf("Case #%d: Blue\n", t+1);
	if(!red && !blue)
		printf("Case #%d: Neither\n", t+1);
}

int main()
{
	scanf("%d", &ncases);
	for(t=0; t<ncases; t++)
	{
		memset(tab, 0, sizeof(tab));
		memset(newtab, 0, sizeof(newtab));
		scanf("%d %d", &tabsize, &kjoin);
		for(int i=0; i<tabsize; i++)
			scanf("%s", tab[i]);
		
		shiftright();
		rotate();
		detect();
	}
	return 0;
}
