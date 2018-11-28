//CODEJAM B

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//vars
	ifstream cin ("B-large.in");
	ofstream cout ("B-large.out");
	int n,a,b,sy,sx,y,x,Y,X,ny,nx;
	char nl,ch;
	int alt[101][101];
	char lab[101][101];
	//testcase loop
	cin >> n;
		for (a=1; a<=n; a++)
		{
			//input
			cin >> sy >> sx;
				for (y=0; y<sy; y++)
					for (x=0; x<sx; x++)
						cin >> alt[y][x];
			//find labels
			memset(lab,0,sizeof(lab));
			nl='a';
				for (y=0; y<sy; y++)
					for (x=0; x<sx; x++)
						if (!lab[y][x])
						{
							Y=y,X=x;
								while (!lab[Y][X])
								{
									b=alt[Y][X],ny=Y,nx=X;
										if ((Y>0) && (alt[Y-1][X]<b))
											b=alt[Y-1][X],ny=Y-1,nx=X;
										if ((X>0) && (alt[Y][X-1]<b))
											b=alt[Y][X-1],ny=Y,nx=X-1;
										if ((X<sx-1) && (alt[Y][X+1]<b))
											b=alt[Y][X+1],ny=Y,nx=X+1;
										if ((Y<sy-1) && (alt[Y+1][X]<b))
											b=alt[Y+1][X],ny=Y+1,nx=X;
										if ((ny==Y) && (nx==X))
											break;
									Y=ny,X=nx;
								}
								if (!lab[Y][X])
									ch=nl++;
								else
									ch=lab[Y][X];
							Y=y,X=x;
								while (!lab[Y][X])
								{
									lab[Y][X]=ch;
									b=alt[Y][X],ny=Y,nx=X;
										if ((Y>0) && (alt[Y-1][X]<b))
											b=alt[Y-1][X],ny=Y-1,nx=X;
										if ((X>0) && (alt[Y][X-1]<b))
											b=alt[Y][X-1],ny=Y,nx=X-1;
										if ((X<sx-1) && (alt[Y][X+1]<b))
											b=alt[Y][X+1],ny=Y,nx=X+1;
										if ((Y<sy-1) && (alt[Y+1][X]<b))
											b=alt[Y+1][X],ny=Y+1,nx=X;
										if ((ny==Y) && (nx==X))
											break;
									Y=ny,X=nx;
								}
						}
			//output
			cout << "Case #" << a << ": " << endl;
				for (y=0; y<sy; y++)
					for (x=0; x<sx; x++)
					{
						cout << lab[y][x];
							if (x<sx-1)
								cout << ' ';
							else
								cout << endl;
					}
		}
	return(0);
}