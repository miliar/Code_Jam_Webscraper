#include <stdio.h>
#include <string.h>

#define ni(x) scanf("%d", &x)
#define ns(x) scanf("%s", x)
#define ndirs 4
#define valid(r,c) (r>=0 && r<row && c>=0 && c<col)

int map[108][108];
int dir[108][108];
int fid[108][108];
int dirs[4][2] = {
	{-1,0},//North
	{0,-1},//West
	{0,1},//East
	{1,0},//South
	
};

int row, col;

void finddirection()
{
	for(int r=0;r<row;++r)
	{
		for(int c=0;c<col;++c)
		{
			int cur = map[r][c];
			dir[r][c] = -1;//initially sink
			for(int i=0;i<ndirs;++i)
			{
				int p = r+dirs[i][0];
				int q = c+dirs[i][1];
				if(valid(p,q)) 
				{
					if(map[p][q] < cur)
					{
						dir[r][c] = i;
						cur = map[p][q];
					}
				}
			}
			//printf("%d ", dir[r][c]);
		}
		//puts("");
	}
}


int qr[108*108];
int qc[108*108];
int head,tail;
#define qinit() head=0,tail=0
#define qsize() (head - tail)
#define qpush(r,c) (qr[head]=r, qc[head]=c, ++head, fid[r][c]=id) //, printf("push %d %d\n",r,c))
#define qpop(r,c) (r=qr[tail], c=qc[tail], ++tail) //, printf("pop %d %d\n",r,c))

#define flowhere(p,q,i) ((dir[p][q] + i) == 3)

void breadthfirst()
{
	int id = 0;
	memset(fid, 0, sizeof(fid));
	
	for(int r=0;r<row;++r)
		for(int c=0;c<col;++c) if(dir[r][c]==-1)
		{
			//start bfs
			++id;
			qinit();
			qpush(r,c);
			while( qsize() > 0 )
			{
				int s,t;
				qpop(s,t);
				for(int i=0;i<ndirs; i++)
				{
					int p = s+dirs[i][0];
					int q = t+dirs[i][1];
					if(valid(p,q) && fid[p][q]==0 && flowhere(p,q,i))
						qpush(p,q);
				}
			}
		}
}

char ass[30];
void assignlabel()
{
	memset(ass, 0, sizeof(ass));
	char ch = 'a';
	for(int r=0;r<row;++r)
	{
		for(int c=0;c<col;++c)
		{
			if(0 == ass[fid[r][c] ]) ass[fid[r][c]] = ch++;
			//printf("%d ", fid[r][c]);
		}
		//puts("");
	}
}

void output(int ks)
{
	
	printf("Case #%d:\n", ks);
	for(int r=0;r<row;++r)
		for(int c=0;c<col;++c)
		{
			putchar( ass[ fid[r][c] ] );
			putchar( (c+1 == col)? 10 : ' ');
		}
}

int main()
{
	int nmaps;
	ni(nmaps);
	

	for(int ks = 1; ks <= nmaps; ++ks)
	{
		ni(row);
		ni(col);
		for(int r=0;r<row;++r)
			for(int c=0;c<col;++c)
				ni(map[r][c]);
		
		finddirection();
		breadthfirst();
		assignlabel();
		output(ks);
	}
}
