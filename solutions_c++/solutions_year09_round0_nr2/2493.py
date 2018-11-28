// WaterSheds.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <iostream>
#include <string>
#include <stack>
#include <math.h>
#include <fstream>
using namespace std;

char labels[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

class coOrdinates
{
public:
	int x,y;
};

class Box
{
public:
	coOrdinates position;		
	int altitude;
	int cellNo;
	int linkedTo;
	int linkedAltitude;
	bool isSink;
	char label;
	int labelNo;
	Box();
};

Box::Box()
{

	isSink=false;
	cellNo=-1;
	linkedTo=-1;
	altitude=-1;
	linkedAltitude=-1;

}

class Grid
{
public:
	
	Box *boxArray;
	int width,height;
	int boxCount;	
	~Grid(){delete []boxArray;}	
	void initBoxes();
	void Process();
	int findBoxbyPOS(int boxX,int boxY);
	int assignLink(int arrayIndex,int x,int y);
	int assignLabels();
	int FindMyLowestLink(int arrayIndex);
};

void Grid::initBoxes()
{
	boxArray=new Box[boxCount];
}



int Grid::assignLink(int arrayIndex,int x,int y)
{
	coOrdinates north,west,east,south;

	north.x=x;
	north.y=y-1;
	south.x=x;
	south.y=y+1;
	east.x=x+1;
	east.y=y;
	west.x=x-1;
	west.y=y;
	
	bool foundALink=false;

	if(south.y<height)
	{
		int foundBox;
		foundBox=findBoxbyPOS(south.x,south.y);

		if(foundBox!=-1)
		{
			if(boxArray[foundBox].altitude<boxArray[arrayIndex].altitude)
			{
				if(boxArray[arrayIndex].linkedAltitude==-1 || boxArray[arrayIndex].linkedAltitude>=boxArray[foundBox].altitude)
				{
					boxArray[arrayIndex].linkedTo=foundBox;
					boxArray[arrayIndex].linkedAltitude=boxArray[foundBox].altitude;
					foundALink=true;
				}
			}
		}
	}
	
	if(east.x<width)
	{
		int foundBox;
		foundBox=findBoxbyPOS(east.x,east.y);

		if(foundBox!=-1)
		{
			if(boxArray[foundBox].altitude<boxArray[arrayIndex].altitude)
			{
				if(boxArray[arrayIndex].linkedAltitude==-1 || boxArray[arrayIndex].linkedAltitude>=boxArray[foundBox].altitude)
				{
					boxArray[arrayIndex].linkedTo=foundBox;
					boxArray[arrayIndex].linkedAltitude=boxArray[foundBox].altitude;
					foundALink=true;
				}
			}
		}
	}

	if(west.x>=0)
	{
		int foundBox;
		foundBox=findBoxbyPOS(west.x,west.y);

		if(foundBox!=-1)
		{
			if(boxArray[foundBox].altitude<boxArray[arrayIndex].altitude)
			{
				if(boxArray[arrayIndex].linkedAltitude==-1 || boxArray[arrayIndex].linkedAltitude>=boxArray[foundBox].altitude)
				{
					boxArray[arrayIndex].linkedTo=foundBox;
					boxArray[arrayIndex].linkedAltitude=boxArray[foundBox].altitude;
					foundALink=true;
				}
			}
		}
	}

	if(north.y>=0)
	{
		int foundBox;
		foundBox=findBoxbyPOS(north.x,north.y);

		if(foundBox!=-1)
		{
			if(boxArray[foundBox].altitude<boxArray[arrayIndex].altitude)
			{
				if(boxArray[arrayIndex].linkedAltitude==-1 || boxArray[arrayIndex].linkedAltitude>=boxArray[foundBox].altitude)
				{
					boxArray[arrayIndex].linkedTo=foundBox;
					boxArray[arrayIndex].linkedAltitude=boxArray[foundBox].altitude;
					foundALink=true;
				}
			}
		}
	}

	if(foundALink)
	{
		boxArray[arrayIndex].isSink=false;
	}
	else
	{
		boxArray[arrayIndex].isSink=true;		
	}


	return 0;


}



void Grid::Process()
{
	for(int i=0;i<boxCount;i++)
	{
		assignLink(i,boxArray[i].position.x,boxArray[i].position.y);
	}

	//for(int i=0;i<boxCount;i++)
	//{
	//	cout<<"Box#:"<<i<<" is linked to box#:"<<boxArray[i].linkedTo<<"\n";
	//}


	int corrected=0;
	do
	{
		corrected=0;
		for(int i=0;i<boxCount;i++)
		{
			if(!boxArray[i].isSink)
			{
				if(!boxArray[boxArray[i].linkedTo].isSink)
				{
					boxArray[i].linkedTo=boxArray[boxArray[i].linkedTo].linkedTo;
					corrected++;
				}

			}
		}

	}while(corrected>0);

	// Assign initial labels to sinks
	int labelCounter=0;
	for(int i=0;i<boxCount;i++)
	{
		if(boxArray[i].isSink)
		{			
			boxArray[i].label=labels[labelCounter];
			boxArray[i].labelNo=labelCounter;
			labelCounter++;			
		}
	}

	// Sort box labels
	for(int i=0;i<boxCount;i++)
	{
		if(boxArray[i].isSink)
		{
			for(int m=0;m<boxCount;m++)
			{
				if(m==i) continue;
				if(boxArray[m].isSink)
				{
					//cout<<"Finding lowest link for Box#:"<<i<<" :"<<FindMyLowestLink(i);
					//cout<<"Finding lowest link for Box#:"<<m<<" :"<<FindMyLowestLink(m);	

					if(FindMyLowestLink(i)<FindMyLowestLink(m) && boxArray[i].labelNo>boxArray[m].labelNo)
					{
						char tmpLabel;
						int tmpLabelNo;
						tmpLabel=boxArray[i].label;
						tmpLabelNo=boxArray[i].labelNo;

						boxArray[i].label=boxArray[m].label;
						boxArray[i].labelNo=boxArray[m].labelNo;

						boxArray[m].label=tmpLabel;
						boxArray[m].labelNo=tmpLabelNo;
					}
				}
			}

		}
	}

	// Assign labels to linked boxes
	for(int i=0;i<boxCount;i++)
	{
		if(!boxArray[i].isSink)
		{
			boxArray[i].label=boxArray[boxArray[i].linkedTo].label;
		}

	}



}

int Grid::FindMyLowestLink(int arrayIndex)
{
	int mylowestLink=arrayIndex;	
	for(int z=0;z<boxCount;z++)
	{
		if(boxArray[z].linkedTo==arrayIndex && z<mylowestLink)
		{
			mylowestLink=z;
		}
	}

	return mylowestLink;
}


int Grid::assignLabels()
{

	return 0;

}


int Grid::findBoxbyPOS(int boxX,int boxY)
{
	for(int x=0;x<boxCount;x++)
	{
		if(boxArray[x].position.x==boxX && boxArray[x].position.y==boxY)
			return x;
	}
	return -1;
}

int _tmain(int argc, _TCHAR* argv[])
{

	ifstream inputFile;
	ofstream outputFile;
	string filename,filename2; 

	filename="input.txt";
	filename2="output.txt";

	inputFile.open(filename.c_str());  
	if(!inputFile)
	{
		cout<<"Error Opening File";
	}
	else
	{
		outputFile.open(filename2.c_str());
	
		int noCases;
		inputFile>>noCases;

		for(int i=1;i<=noCases;i++)
		{
			int height,width;
			inputFile>>height>>width;

			int totalCells;
			totalCells=height*width;

			Grid map;
			map.width=width;
			map.height=height;			
			map.boxCount=totalCells;
			map.initBoxes();
			
			int tmpAltitude;
			int tmpX,tmpY;
			tmpX=tmpY=0;

			for(int j=0;j<totalCells;j++)
			{
				inputFile>>tmpAltitude;
				map.boxArray[j].altitude=tmpAltitude;	
				if (j%width==0&&j!=0)
				{
					tmpX=0;
					tmpY++;
				}
				
				map.boxArray[j].position.x=tmpX;
				map.boxArray[j].position.y=tmpY;
				tmpX++;

			}

			map.Process();

			outputFile<<"Case #"<<i<<":\n";
						
			for(int j=0;j<totalCells;j++)
			{
				outputFile<<map.boxArray[j].label<<" ";
				if ((j+1)%width==0) outputFile<<"\n";
			}
										

			


		}

		outputFile.close();

	}

	inputFile.close();
		
	cout<<"\n";
	system ("pause");
	return 0;	
}

