#include <stdio.h>
#include <string.h>

#define INVALID -1

int W,H;

struct item
{
	int num;
	int nBasin;
	bool checked;
};

struct point
{
	int x,y;
};

bool isInBounds(int num, int max)
{
	return (num >= 0) && (num < max);
}

void checkMin(item **matrix, int posX, int posY, point *pnt)
{
	if((pnt->x == INVALID) ||(matrix[posY][posX].num < matrix[pnt->y][pnt->x].num))
	{
		pnt->x = posX;
		pnt->y = posY;
	}
}

point findMin(item **matrix, int posX, int posY)
{
	point pnt = {INVALID,INVALID};
	if(isInBounds(posY - 1,H))
		checkMin(matrix,posX,posY - 1,&pnt);
	if(isInBounds(posX - 1,W))
		checkMin(matrix,posX - 1,posY,&pnt);
	if(isInBounds(posX + 1,W))
		checkMin(matrix,posX + 1,posY,&pnt);
	if(isInBounds(posY + 1,H))
		checkMin(matrix,posX,posY + 1,&pnt);
	return pnt;
}

int connectBasins(item **matrix, int posX, int posY)
{
	if(!matrix[posY][posX].checked)
	{
		matrix[posY][posX].checked = true;
		if(matrix[posY][posX].nBasin == INVALID)
		{
			point pnt = findMin(matrix, posX, posY);
			matrix[posY][posX].nBasin = connectBasins(matrix,pnt.x,pnt.y);
		}
	}
	return matrix[posY][posX].nBasin;
}

void findSinks(item **matrix)
{
	int nBasin = 0;
	for(int posX = 0; posX < W; posX++)
	{
		for(int posY = 0; posY < H; posY++)
		{
			bool isSink = true;
			for(int x = -1; (x <= 1) && isSink; x += 2)
			{
				if(isInBounds(posY + x,H))
				{
					if(matrix[posY + x][posX].num < matrix[posY][posX].num)
						isSink = false;
				}

				if(isInBounds(posX + x,W))
				{
					if(matrix[posY][posX + x].num < matrix[posY][posX].num)
						isSink = false;
				}
			}
			if(isSink)
				matrix[posY][posX].nBasin = nBasin++;
		}
	}
}


int main(int argc, char *argv[])
{
	if(argc != 2)
		return -1;
	FILE *pFile;
	if((pFile = fopen(argv[1],"rb")) == NULL)
		return -2;
	int N;
	fscanf(pFile,"%d\n",&N);
	FILE *output = fopen("output.txt","wb");
	char buf[200];
	for(int i = 0; i < N; i++)
	{
		fgets(buf,200,pFile);
		sscanf(buf,"%d %d\n", &H, &W);
		item **matrix = new item*[H];
		for(int y = 0; y < H; y++)
		{
			matrix[y] = new item[W];
			fgets(buf,200,pFile);
			int bufIndex = 0;
			for(int x = 0; x < W; x++)
			{
				sscanf(&buf[bufIndex],"%d",&matrix[y][x].num);
				matrix[y][x].checked = false;
				matrix[y][x].nBasin = INVALID;
				if(matrix[y][x].num > 9)
					bufIndex+=3;
				else
					bufIndex+=2;
			}
		}
		//Built Matrix
		int nBasin = 0;
		findSinks(matrix);
		for(int x = 0; x < W; x++)
		{
			for(int y = 0; y < H; y++)
			{
				if(!matrix[y][x].checked)
					connectBasins(matrix,x,y);
			}
		}
		char basins[26];
		memset(basins,INVALID,26 * sizeof(char));
		char cBasin = 'a';
		fprintf(output,"Case #%d:\n",i+1);
		for(int y = 0; y < H; y++)
		{
			for(int x = 0; x < W; x++)
			{
				if(x != 0)
					fputc(' ',output);
				if(basins[matrix[y][x].nBasin] == INVALID)
					basins[matrix[y][x].nBasin] = cBasin++;
				fputc(basins[matrix[y][x].nBasin],output);
			}
			fputc('\n',output);
		}
		for(int i = 0; i < H; i++)
			delete[] matrix[i];
		delete[] matrix;
	}
	fflush(output);
	fclose(output);
	getchar();
	return 0;
}
