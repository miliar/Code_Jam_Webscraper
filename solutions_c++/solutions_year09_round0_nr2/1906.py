// p4.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <VECTOR>
#include <UTILITY>
#include <STACK>
#include <iostream>
#include <fstream>
#include <strstream>
#include <STRING>
#include <map>
#include <set>

using namespace std;

int alts[101][101];
int sinks[101][101];
int sinkx[101][101];
int sinky[101][101];
char sinkchar[101][101];

stack <pair<int,int> > path;
int height, width;
int heightmax = 20000;
map< pair<int,int> , char > assign;


void getNext(int j,int k)
{
	int northx,northy,southx,southy,eastx,easty,westx,westy;
	int minalt;
	int heightN=heightmax;
	int heightS = heightmax;
	int heightE = heightmax;
	int heightW = heightmax;
	bool issink = true;
	int minx = j;
	int miny = k;
	northx = (j-1);
	northy = k;
	southx = j+1;
	southy = k;
	eastx = j;
	westx = j;
	easty = k+1;
	westy = k-1;
	minalt = alts[j][k];
	if (easty < width ) heightE = alts[eastx][easty]; 
	if (westy >=0 ) heightW = alts[westx][westy];
	if (northx >=0) heightN = alts[northx][northy];
	if (southx < height ) heightS = alts[southx][southy];
	if (heightN < minalt) {
			issink = false;
			minx = northx;
			miny = northy;
			minalt = heightN;
	}
	if (heightW < minalt) {
			issink = false;
			minx = westx;
			miny = westy;
			minalt = heightW;
	}

	if (heightE < minalt) {
			issink = false;
			minx = eastx;
			miny = easty;
			minalt = heightE;
	}
	if (heightS < minalt) {
			issink = false;
			minx = southx;
			miny = southy;
			minalt = heightS;
	}
	if (!issink)
	{
		//water is flowing to next point. Sink not reached.
		path.push(make_pair(j,k));
		getNext(minx,miny);
	}
	else
	{
		// We reached a sink, it might already exist in the set
		while (!path.empty())
		{
			pair<int,int> temp = path.top();
			path.pop();
			sinkx[temp.first][temp.second] = minx;
			sinky[temp.first][temp.second] = miny;
		}
		sinkx[j][k] = minx;
		sinky[j][k] = miny;
	}


}


int main(int argc, char* argv[])
{
	//printf("Hello World!\n");
	ifstream fin("input.txt");
	FILE *f2 = fopen("output.txt","w");
	int numMaps;
	fin >> numMaps;
	int i,j,k,l;
	
	
	for ( i =0 ; i <numMaps ; ++i)
	{
		
		fin >> height;
		fin >> width;
		assign.clear();
		while (!path.empty()) path.pop();
		for (j=0; j< height;++j)
			for (k =0; k < width; ++k)
			{
				fin >> alts[j][k];
				sinkx[j][k]=-1;
				sinky[j][k]=-1;
			}

		for (j=0; j< height;++j)
			for (k =0; k < width; ++k)
			{
				if (sinkx[j][k] >= 0) continue;
				getNext(j,k);
									
			}
	fprintf(f2,"Case #%d:\n",i+1);
    char chartemp = 'a';
	for (j=0; j< height;++j)
			for (k =0; k < width; ++k)
			{
				pair<int,int> temp = make_pair(sinkx[j][k],sinky[j][k]);
				if (assign.find(temp) == assign.end())
				{
					assign[temp] = chartemp;
					++chartemp;
				}
				if (k <(width -1)) fprintf(f2,"%c ",assign[temp]);
				else fprintf(f2,"%c\n",assign[temp]);

			}
		
	}
	fclose(f2);
	return 0;
}

