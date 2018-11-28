#include <iostream>

using namespace std;

void paintPathToSink(int i, int j);

const int maxT = 100;
const int maxH = 100;
const int maxW = 100;
const int maxHW = 100;
const int maxAltitude = 10000;
int T, H, W;
int a[maxH][maxW];
char p[maxH][maxW];
char label;

int main()
{
	cin >> T;
	for(int t=1; t<=T; t++){
		/************************************
			Input Data
		*************************************/
		//cout << L << ' ' << D << ' ' << N << endl;
		cin >> H >> W;
		label = 'a'-1;
		for(int i=0; i<H; i++)
		for(int j=0; j<W; j++){
			cin >> a[i][j];
		}
		//cout << "debug2" << endl;
		//cin.ignore(maxLen,'\n'); // skipping end-of-line
		/************************************
			Solve the Problem
		*************************************/
		memset(p,0,sizeof(p));
		for(int i=0; i<H; i++)
		for(int j=0; j<W; j++){
			if(p[i][j])
				continue;
			paintPathToSink(i,j);
		}
		/************************************
			Output Results
		*************************************/
		cout << "Case #" << t << ":" << endl;
		for(int i=0; i<H; i++)
		{
			cout << p[i][0];
			for(int j=1; j<W; j++)
				cout << ' ' << p[i][j];
			cout << endl;
		}
		/* Debug
		cout << "----------------\n";
		for(int j=0; j<S; j++)
			cout << searchEngineNames[j] << endl;
		cout << "----------------\n";
		for(int j=0; j<Q; j++)
			cout << queries[j] << endl;
		*/
	}
	return 0;
}

int not_sink(int i, int j)
{
	int min = maxAltitude, nNeighbour, wNeighbour, eNeighbour, sNeighbour, r;
	if(i==0) nNeighbour = maxAltitude+1; 	else nNeighbour = a[i-1][j];
	if(j==0) wNeighbour = maxAltitude+1;	else wNeighbour = a[i][j-1];
	if(i==H-1) sNeighbour = maxAltitude+1;	else sNeighbour = a[i+1][j];
	if(j==W-1) eNeighbour = maxAltitude+1;	else eNeighbour = a[i][j+1];

	if(min>nNeighbour) { min = nNeighbour; r = 1; }
	if(min>wNeighbour) { min = wNeighbour; r = 2; }
	if(min>eNeighbour) { min = eNeighbour; r = 3; }
	if(min>sNeighbour) { min = sNeighbour; r = 4; }
	if(min>=a[i][j]) r = 0;
	return r;
}

void paintPathToSink(int i, int j)
{
	int path[maxHW*maxHW][2];
	int pathLen = 0, dir;
	while(!p[i][j] && (dir = not_sink(i,j)))
	{
		path[pathLen][0] = i;   path[pathLen][1] = j;
		pathLen++;
		switch(dir){
			case 1:	
					// to the north
				i--;
				break;
			case 2:
					// to the west
				j--;
				break;
			case 3:
					// to the east
				j++;
				break;
			case 4:
					// to the south
				i++;
				break;
		}
	}
	if(!p[i][j]){ // ia a sink?
		p[i][j] = ++label;
	}
	for(int k=0; k<pathLen; k++)
		p[path[k][0]][path[k][1]] = p[i][j];
}
