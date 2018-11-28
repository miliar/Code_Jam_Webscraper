#include <iostream>
#include <fstream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

ifstream fin;
ofstream fout;

void compute();
char wheretoflow(int H, int W,int i,int j,char (&mapchar)[120][120],int mapint[120][120]);

int main()
{
	fin.open("small1.in");
	fout.open("small1.out");

	char numbers[100];

	fin.getline(numbers,100);

	int T;

	sscanf(numbers,"%d",&T);

	for (int i = 0; i < T; i++)
	{
		fout<<"Case #"<<(i+1)<<":"<<endl;
		compute();
	}
}

void compute()
{
	int H;
	int W;

	char numbers[100];

	fin.getline(numbers,100);

	sscanf(numbers,"%d %d",&H,&W);

	char map[1000000];
	int  mapint[120][120];

	for (int i = 0; i < 1000000; i++)
		map[i]=' ';

	for (int i = 0; i < H; i++)
		for (int j = 0; j < W; j++)
			mapint[i][j] = 0;

	for (int i = 0; i < H; i++)
	{
	    fin.getline(map,1000000);
		char *temp = map;
        for(int j = 0; j < W; j++)
		{
			char track[7];
			int tempint = 0;
			while(*temp != ' ')
			{
				track[tempint] = *temp;
				tempint++;
				temp++;
			}
			track[tempint] = '\0';
			temp++;
			sscanf(track,"%d",&(mapint[i][j]));
		}
	}

    char  mapchar[120][120];

	for(int i = 0; i < 120; i++)
		for(int j = 0; j < 120; j++)
		      mapchar[i][j] = '*';

	char c1 = 'a';

    for (int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
		{
		    if(( i>=1 && (mapint[i-1][j] >= mapint[i][j])) || (i==0))
			{	if((j>=1 && (mapint[i][j-1] >= mapint[i][j])) || (j==0))
			{       if((j<W-1 && (mapint[i][j+1] >= mapint[i][j])) || (j==W-1))
			{          if((i<H-1 && (mapint[i+1][j] >= mapint[i][j])) || (i==H-1))
					  {  mapchar[i][j] = c1;
			             c1++;
			          }
		    }
			}
			}
		}

	char   mapchar1[120][120];
	for(int i = 0; i < 120; i++)
		for(int j = 0; j < 120; j++)
		      mapchar1[i][j] =  mapchar[i][j];

    for (int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
		{
			mapchar1[i][j]=wheretoflow(H, W,i,j,mapchar,mapint);
		}

	for(int i = 0; i < 120; i++)
		for(int j = 0; j < 120; j++)
		      mapchar[i][j] = '*';

    mapchar[0][0] = 'a';
    for (int i = 0; i < H; i++)
		for(int j = 0; j < W; j++)
		{
			if (mapchar1[i][j]==mapchar1[0][0])
				    mapchar[i][j] = 'a';
		}
	bool ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' )
			{
				mapchar[i][j] = 'b';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'b';
				   }
			   ind = false;
			}
		}
    ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b')
			{
				mapchar[i][j] = 'c';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'c';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c')
			{
				mapchar[i][j] = 'd';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'd';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d')
			{
				mapchar[i][j] = 'e';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'e';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e')
			{
				mapchar[i][j] = 'f';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'f';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'&& mapchar[i][j]!='f')
			{
				mapchar[i][j] = 'g';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'g';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'&& mapchar[i][j]!='f'&& mapchar[i][j]!='g')
			{
				mapchar[i][j] = 'h';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'h';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h')
			{
				mapchar[i][j] = 'i';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'i';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i')
			{
				mapchar[i][j] = 'j';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'j';
				   }
			    ind = false;
			}
		}

	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j')
			{
				mapchar[i][j] = 'k';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'k';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'&& mapchar[i][j]!='k')
			{
				mapchar[i][j] = 'l';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'l';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'&& mapchar[i][j]!='k'&& mapchar[i][j]!='l')
			{
				mapchar[i][j] = 'm';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'm';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m')
			{
				mapchar[i][j] = 'n';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'n';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n')
			{
				mapchar[i][j] = 'o';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'o';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o')
			{
				mapchar[i][j] = 'p';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'p';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'&& mapchar[i][j]!='p')
			{
				mapchar[i][j] = 'q';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'q';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'&& mapchar[i][j]!='p'&& mapchar[i][j]!='q')
			{
				mapchar[i][j] = 'r';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'r';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r')
			{
				mapchar[i][j] = 's';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 's';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s')
			{
				mapchar[i][j] = 't';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 't';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t')
			{
				mapchar[i][j] = 'u';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'u';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t'&& mapchar[i][j]!='u')
			{
				mapchar[i][j] = 'v';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'v';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t'&& mapchar[i][j]!='u'&& mapchar[i][j]!='v')
			{
				mapchar[i][j] = 'w';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'w';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t'&& mapchar[i][j]!='u'&& mapchar[i][j]!='v'&& mapchar[i][j]!='w')
			{
				mapchar[i][j] = 'x';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'x';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t'&& mapchar[i][j]!='u'&& mapchar[i][j]!='v'&& mapchar[i][j]!='w'&& mapchar[i][j]!='x')
			{
				mapchar[i][j] = 'y';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'y';
				   }
			    ind = false;
			}
		}
	ind = true;
    for (int i = 0; i < H && ind == true; i++)
		for(int j = 0; j < W && ind == true; j++)
		{
			if (mapchar[i][j]!='a' && mapchar[i][j]!='b'&& mapchar[i][j]!='c'&& mapchar[i][j]!='d'&& mapchar[i][j]!='e'
				&& mapchar[i][j]!='f'&& mapchar[i][j]!='g'&& mapchar[i][j]!='h'&& mapchar[i][j]!='i'&& mapchar[i][j]!='j'
				&& mapchar[i][j]!='k'&& mapchar[i][j]!='l'&& mapchar[i][j]!='m'&& mapchar[i][j]!='n'&& mapchar[i][j]!='o'
				&& mapchar[i][j]!='p'&& mapchar[i][j]!='q'&& mapchar[i][j]!='r'&& mapchar[i][j]!='s'&& mapchar[i][j]!='t'
				&& mapchar[i][j]!='u'&& mapchar[i][j]!='v'&& mapchar[i][j]!='w'&& mapchar[i][j]!='x'&& mapchar[i][j]!='y')
			{
				mapchar[i][j] = 'z';
			    for (int i1 = 0; i1 < H; i1++)
		           for(int j1 = 0; j1 < W; j1++)
				   {
					   if (mapchar1[i1][j1]==mapchar1[i][j])
						   mapchar[i1][j1] = 'z';
				   }
			    ind = false;
			}
		}

    for (int i = 0; i < H; i++)
	    {for (int j = 0; j < W; j++)
			fout<<mapchar[i][j]<<' ';
            fout<<endl;
	    }
	    


	
}

char wheretoflow(int H, int W, int i,int j,char (&mapchar)[120][120],int mapint[120][120])
{
	if (mapchar[i][j] != '*')
		return (mapchar[i][j]);

	int i1 = 20000;
	int i2 = 20000;
	int i3 = 20000;
	int i4 = 20000;

	if (i >=1)
		i1 = mapint[i-1][j];
	if (j >=1)
		i2 = mapint[i][j-1];
	if (j <W-1)
		i3 = mapint[i][j+1];
	if (i <H-1)
		i4 = mapint[i+1][j];

	int least = i1;
	if (i2 < least)
		least = i2;
	if (i3 < least)
		least = i3;
	if (i4 < least)
		least = i4;

	if (least == i1)
		return (wheretoflow(H,W,i-1,j,mapchar,mapint));
	else if (least == i2)
		return (wheretoflow(H,W,i,j-1,mapchar,mapint));
	else if (least == i3)
		return (wheretoflow(H,W,i,j+1,mapchar,mapint));
	else if (least == i4)
		return (wheretoflow(H,W,i+1,j,mapchar,mapint));
}
