#include<fstream.h>
struct cell
{ int alt;
  char basin;
};

cell** map;
int H,W;
char basno;

int isSink(int i, int j)
{ int thisalt=map[i][j].alt;

  //if any neighbouring cell has lower altitude, it is not a sink

  if((i-1)>=0 && map[i-1][j].alt<thisalt)
	 return 0;
  if((i+1)<H && map[i+1][j].alt<thisalt)
	return 0;
  if((j-1)>=0 && map[i][j-1].alt<thisalt)
	return 0;
  if((j+1)<W && map[i][j+1].alt<thisalt)
	return 0;

  return 1;
}

char getBasin(int i, int j)
{
	if(map[i][j].basin!='0')
		return map[i][j].basin;

	if(isSink(i,j))
	{ map[i][j].basin=basno;
		  basno++;
	  return map[i][j].basin;
	}

	int minalt=10001;   //setting it to 1 greater than max alt
	char mindir='0';

  if((i-1)>=0 && map[i-1][j].alt<minalt)
	{ mindir='N'; minalt=map[i-1][j].alt;}
  if((j-1)>=0 && map[i][j-1].alt<minalt)
	{ mindir='W'; minalt=map[i][j-1].alt;}
  if((j+1)<H && map[i][j+1].alt<minalt)
	{ mindir='E'; minalt=map[i][j+1].alt;}
  if((i+1)<W && map[i+1][j].alt<minalt)
	{ mindir='S'; minalt=map[i+1][j].alt;}

  switch(mindir)
  { case 'W': if(map[i][j-1].basin!='0')
						map[i][j].basin = map[i][j-1].basin;
					else
						map[i][j].basin = getBasin(i,j-1);
					break;
  case 'N': if(map[i-1][j].basin!='0')
						map[i][j].basin = map[i-1][j].basin;
					else
						map[i][j].basin = getBasin(i-1,j);
					break;
  case 'S': if(map[i+1][j].basin!='0')
						map[i][j].basin = map[i+1][j].basin;
					else
						map[i][j].basin = getBasin(i+1,j);
					break;
  case 'E': if(map[i][j+1].basin!='0')
						map[i][j].basin = map[i][j+1].basin;
					else
						map[i][j].basin = getBasin(i,j+1);
					break;
  }

  return map[i][j].basin;
}


void main()
{ ifstream fin("inputb.txt");
  ofstream fout("outputb.txt");

  int T;

  fin>>T;

  for(int i=0; i<T; i++)
  {	fin>>H>>W;
		basno='a';

		//allocating memory
		map = new cell*[H];
		for(int j=0; j<H; j++)
			map[j] = new cell[W];

		//initializing map values
		int row,col;
		for(row=0; row<H; row++)
			for(col=0; col<W; col++)
				{ fin>>map[row][col].alt;
				  map[row][col].basin='0';  //0 indicates not decided
				}


		//evaluating basins
		for(row=0; row<H; row++)
		{  for(col=0; col<W; col++)
			{
				 map[row][col].basin=getBasin(row,col);
			}
		}

		//freeing memory
		for(j=0;j<H;j++)
		 delete map[j];
		delete map;

  }


  fin.close();
  fout.close();
}
