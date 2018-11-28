#include <iostream>
using std::cin;
using std::cout;
using std::endl;

#include <stdio.h>
using namespace std;

#include <fstream>
using namespace std;

#include <string>
using namespace std;

#include <math.h>

int main()
{
	srand(12321);

	int depths[102][102];
	char sinks[101][101]; // for simplicity matching to depths

	int i, j, k;
	int cases;
	string temp;

	ofstream of("C:\\Documents and Settings\\customer\\Desktop\\B-large-out.txt");	
//	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\B-small.in");
	ifstream f("C:\\Documents and Settings\\customer\\Desktop\\B-large.in");

	f >> cases;
	int H;
	int W;

	struct pathElement
	{
		pathElement * previous; 
		char * element;
	};

	pathElement * pathTrace=new(pathElement);
	pathElement * oldElement=new(pathElement);

	for(i=0; i< cases; i++)
	{
		of << "Case #" << i+1 << ":" << endl;
		f >> H;
		f >> W;

		for(j=0; j<H+2; j++) // create one border
		{
			depths[j][0]=1000000000;
			depths[j][W+1]=1000000000;
		}

		for(j=0; j<W+2; j++) // create the other border
		{
			depths[0][j]=1000000000;
			depths[H+1][j]=1000000000;
		}

		for(j=1; j<H+1; j++) // offset by 1
		{
			for(k=1; k<W+1; k++) // offset by 1
			{
				f >> depths[j][k];
			}
		} // end of depth initialization
		// now the depths are stored in the array, but offset by a border size 1, which is all high altitude (a 'fence')

		// initialize sinks
		for(j=1; j<H+1; j++)
		{
			for(k=1; k<W+1; k++)
			{
				sinks[j][k]=' ';
			}
		}

		char newSink='a';
		int currentdepth;
		int hdif;
		int vdif;
		int tempj;
		int tempk;
		// done initializing sinks

		for(j=1; j<H+1; j++)
		{
			for(k=1; k<W+1; k++)
			{
				pathTrace->previous=NULL;
				tempj=j;
				tempk=k;
				while(sinks[tempj][tempk]==' ')
				{
					currentdepth=depths[tempj][tempk]; // current to beat
					hdif=0; // staying put
					vdif=0;

					if(depths[tempj-1][tempk] < currentdepth) // north
					{
						hdif=-1; // north
						// at this point vdif can only be 0 so not needed to specify
						currentdepth=depths[tempj-1][tempk]; 
					}
					if(depths[tempj][tempk-1] < currentdepth) // west
					{
						hdif=0;
						vdif=-1;
						currentdepth=depths[tempj][tempk-1]; 
					}
					if(depths[tempj][tempk+1] < currentdepth) // east
					{
						hdif=0;
						vdif=+1;
						currentdepth=depths[tempj][tempk+1]; 
					}
					if(depths[tempj+1][tempk] < currentdepth) // south
					{
						hdif=+1;
						vdif=0;
						currentdepth=depths[tempj+1][tempk]; 
					}

					//cout << hdif << ", " << vdif << endl;
					if(hdif==0 && vdif==0)
					{
						sinks[tempj][tempk]=newSink;
						sinks[j][k]=newSink;
						newSink++;
					} else {
						pathTrace->element=&sinks[tempj][tempk]; // the pointer to the character to be updated later
						oldElement=pathTrace;
						pathTrace=new(pathElement);
						pathTrace->previous=oldElement;

						tempj+=hdif;
						tempk+=vdif;
						pathTrace->element=&sinks[tempj][tempk];
					}
				}

				sinks[j][k]=sinks[tempj][tempk];

				// found a resting location
				while(pathTrace->previous != NULL)
				{
					*pathTrace->element=sinks[j][k];
					oldElement=pathTrace;
					pathTrace=pathTrace->previous;
					delete oldElement;

/*
					if(i==0) // debug block
					{
						int l, m;
							for(l=1; l<H+1; l++)
							{
								for(m=1; m<W; m++)
								{
									cout << sinks[l][m] << " ";
								}
								cout << sinks[l][m] << endl;
							}
							cout << "_____________" << endl;
					} // end of debug block
//*/

				}
				//cout << "*****" << endl;
				
			} // k increment
		} // j increment

		for(j=1; j<H+1; j++)
		{
			for(k=1; k<W; k++)
			{
				of << sinks[j][k] << " ";
			}
			of << sinks[j][k] << endl;
		}
	} // i increment (cases)

	cout << endl << "done";
	char pause;
	cin >> pause;
	return 0;
}