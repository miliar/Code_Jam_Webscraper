// ViszinisA

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int map[102][102];
char labeled_map[102][102];

int followflow(char basin_no, int j, int l, int height, int width, char checkto)
{
	// North, West, East, South.
	int alt;
	char flowto;
	alt = map[j-1][l];
	flowto = 'n';
	if (alt>map[j][l-1])
	{
		alt = map[j][l-1];
		flowto = 'w';
	}
	if (alt>map[j][l+1])
	{
		alt = map[j][l+1];
		flowto = 'e';
	}
	if (alt>map[j+1][l])
	{
		alt = map[j+1][l];
		flowto = 's';
	}
	if (checkto == flowto)
	{
		labeled_map[j][l] = basin_no;
		if (j-1>0 && flowto != 'n' && map[j][l] < map[j-1][l])
		{
			followflow(basin_no, j-1, l, height, width, 's');
		}
		if (j+1<=height && flowto != 's' && map[j][l] < map[j+1][l])
		{
			followflow(basin_no, j+1, l, height, width, 'n');
		}
		if (l-1>0 && flowto != 'w' && map[j][l] < map[j][l-1])
		{
			followflow(basin_no, j, l-1, height, width, 'e');
		}
		if (l+1<=width && flowto != 'e' && map[j][l] < map[j][l+1])
		{
			followflow(basin_no, j, l+1, height, width, 'w');
		}
	}
	/*
	followflow(basin_no, j-1, l, height, width, "south");
	followflow(basin_no, j+1, l, height, width, "north");
	followflow(basin_no, j, l-1, height, width, "east");
	followflow(basin_no, j, l+1, height, width, "west");
	*/
};
int main ()
{
	FILE * pfin, * pfout;
	pfin = fopen ("b.in", "r");
	pfout = fopen ("b.out", "w");

	int maps, height, width;
	int i,j,l;
	//int map[102][102];
	//char labeled_map[102][102];
	char basin_no;
	char basin_labels[27] = {};
	char next_label;

	for (i=0; i<102; i++)
	{
		for (j=0; j<102; j++)
		{
			map[i][j] = 11;
		}
	}

	fscanf (pfin, "%d\n", &maps);
	for (i=1; i<=maps; i++)
	{
		if (i>1)
		{
			fprintf (pfout, "\n");
		}

		fprintf (pfout, "Case #%d:\n", i);

		fscanf (pfin, "%d %d\n", &height, &width);
		//printf ("%d %d\n", height, width);

		next_label = 'a';

		// borders
		for (j=1; j<width+1; j++)
		{
			map[height+1][j] = 11;
		}
		for (j=1; j<height+1; j++)
		{
			map[j][width+1] = 11;
		}

		// labels
		for (j=1; j<=26; j++)
		{
			basin_labels[j] = '\0';
		}

		// read
		for (j=1; j<=height; j++)
		{
			for (l=1; l<=width; l++)
			{
				fscanf (pfin, "%d", &map[j][l]);
			}
		}
		/*
		for (j=1; j<=height; j++)
		{
			for (l=1; l<=width; l++)
			{
				cout << map[j][l];
			}
			cout << endl;
		}
		*/		
		basin_no = '0';
		for (j=1; j<=height; j++)
		{
			for (l=1; l<=width; l++)
			{
				if (map[j][l]<=map[j-1][l] && map[j][l]<=map[j][l-1] && map[j][l]<=map[j+1][l] && map[j][l]<=map[j][l+1])
				{
					basin_no++;
					labeled_map[j][l] = basin_no;
					if (j-1>0 && map[j][l] < map[j-1][l])
					{
						followflow(basin_no, j-1, l, height, width, 's');
					}
					if (j+1<=height && map[j][l] < map[j+1][l])
					{
						followflow(basin_no, j+1, l, height, width, 'n');
					}
					if (l-1>0 && map[j][l] < map[j][l-1])
					{
						followflow(basin_no, j, l-1, height, width, 'e');
					}
					if (l+1<=width && map[j][l] < map[j][l+1])
					{
						followflow(basin_no, j, l+1, height, width, 'w');
					}
					/*
					followflow(basin_no, j-1, l, height, width, 's');
					followflow(basin_no, j+1, l, height, width, 'n');
					followflow(basin_no, j, l-1, height, width, 'e');
					followflow(basin_no, j, l+1, height, width, 'w');
					*/
				}
			}
		}

		for (j=1; j<=height; j++)
		{
			for (l=1; l<=width; l++)
			{
				if (basin_labels[labeled_map[j][l]-48]=='\0')
				{
					basin_labels[labeled_map[j][l]-48] = next_label;
					next_label++;
				}
				//cout << labeled_map[j][l] << ";" << basin_labels[labeled_map[j][l]-48] << " ";
				labeled_map[j][l] = basin_labels[labeled_map[j][l]-48];
			}
			//cout << endl;
		}

		for (j=1; j<=height; j++)
		{
			if (j>1)
			{
				fprintf (pfout, "\n");
			}
			for (l=1; l<=width; l++)
			{
				if (l>1)
				{
					fprintf (pfout, " ");
				}
				fprintf (pfout, "%c", labeled_map[j][l]);
			}
			//cout << endl;
		}

/*
		// print
		for (j=0; j<12; j++)
		{
			for (l=0; l<12; l++)
			{
				printf ("%2d ", map[j][l]);
			}
			cout << endl;
		}
*/		
//		cout << endl;
	}


	fclose (pfin);
	fclose (pfout);
	system ("Pause");
	return 0;
}
