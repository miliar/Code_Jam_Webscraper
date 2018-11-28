

#include "stdafx.h"
#include <string>
#include <fstream>

using namespace std;
using std::string;

int caseNum = 0;

static struct DataItem
{
	int altitude;

	int index;
	int nextInd;
	int prevInd;
	int sinkIndex;

	char sinkChar;

	bool isSink;
};

struct Sink
{
	int dataIndex;
	bool mark;
	char letter;
};

void findResult(DataItem** dataItm, int curIndex, int h, int w, int H, int W, int SINK_INDEX);

int _tmain(int argc, _TCHAR* argv[])
{
	const char *inputFileName;
	string inputFileName_s = "D:\\CodeJam09\\B-large.in";
	//string inputFileName_s = "D:\\CodeJam09\\a.txt";
	inputFileName = inputFileName_s.c_str();

	FILE *inp;

	fopen_s(&inp, inputFileName, "r");
	
	fscanf_s(inp, "%d",&caseNum);

	//int caseNum = 1;

	FILE * pFile = fopen ("D:\\CodeJam09\\outputLargeFile.txt","w");

	int H, W;
	for(int t=0 ; t<caseNum ; t++)
	{	
		fscanf_s(inp, "%d",&H);
		fscanf_s(inp, "%d",&W);
		
		//DataItem data[H][W];
		DataItem **data = (DataItem**) malloc(H*sizeof(DataItem*)); 
		for(int i=0 ; i<H ; i++)
			data[i] = (DataItem*) malloc(W*sizeof(DataItem));

		Sink *sinkData = (Sink*) malloc(W*H*sizeof(Sink)); 

		int ind = 0;
		for(int i=0 ; i<H ; i++){
			for(int j=0 ; j<W ; j++){
				fscanf_s(inp, "%d",&data[i][j].altitude);
				data[i][j].index = ind;
				data[i][j].nextInd = -1;
				data[i][j].prevInd = -1;
				data[i][j].sinkIndex = -1;
				data[i][j].isSink = false;
				ind++;
			}
		}

		for(int q=0 ; q<H*W ; q++)
		{
			sinkData[q].mark = false;
		}

		int sinkNum = 0;
		for(int i=0 ; i<H ; i++)
		{
			for(int j=0 ; j<W ; j++)
			{
				bool isChange = false;
				int min = data[i][j].altitude;
				if(i-1>=0 && data[i-1][j].altitude<min){
					min = data[i-1][j].altitude;
					data[i][j].nextInd = data[i-1][j].index;
					//if(data[i-1][j].prevInd == -1)
					//	data[i-1][j].prevInd = data[i][j].index;
					isChange = true;
				}				
				if(j-1>=0 && data[i][j-1].altitude<min){
					min = data[i][j-1].altitude;
					data[i][j].nextInd = data[i][j-1].index;
					//if(data[i][j-1].prevInd == -1)
					//	data[i][j-1].prevInd = data[i][j].index;
					isChange = true;
				}
				if(j+1<W && data[i][j+1].altitude<min){
					min = data[i][j+1].altitude;
					data[i][j].nextInd = data[i][j+1].index;
					//if(data[i][j+1].prevInd == -1)
					//	data[i][j+1].prevInd = data[i][j].index;
					isChange = true;
				}
				if(i+1<H && data[i+1][j].altitude<min){
					min = data[i+1][j].altitude;
					data[i][j].nextInd = data[i+1][j].index;
					//if(data[i+1][j].prevInd == -1)
					//	data[i+1][j].prevInd = data[i][j].index;
					isChange = true;
				}

				if(isChange == false){
					data[i][j].isSink = true;
					data[i][j].sinkIndex = sinkNum;
					sinkData[sinkNum].dataIndex = data[i][j].index;
					sinkNum++;
				}
				//outFile << data[i][j].altitude<<"("<<data[i][j].prevInd<<","<<data[i][j].nextInd<<")\t";
			}
			//outFile << "\n";
		}

		for(int i=0 ; i<H ; i++){
			//for(int j=0 ; j<W ; j++)
				//outFile << data[i][j].altitude<<"("<<data[i][j].nextInd<<")\t";
			//outFile << "\n";
		}

		//outFile << "Case #"<<caseNum<<":\n";

		for(int k=0 ; k<sinkNum ; k++)
		{
			int dataIndex = sinkData[k].dataIndex;

			int i = dataIndex / W;
			int j = dataIndex % W;

			findResult(data, dataIndex, i, j, H, W, k);
		}
		
		fprintf (pFile, "Case #%d:\n", t+1);

		char currentLetter = 'a';
		for(int m=0 ; m<H ; m++){
			for(int n=0 ; n<W ; n++){
				int sink = data[m][n].sinkIndex;

				if(m==0 && n==0)
				{
					sinkData[sink].letter = 'a';
					sinkData[sink].mark = true;
				}
				else if(sinkData[sink].mark == false){
					currentLetter++;
					sinkData[sink].letter = currentLetter;
					sinkData[sink].mark = true;
				}
				
				//outFile << sinkData[sink].letter <<"\t";
				fprintf (pFile, "%c ", sinkData[sink].letter);

			}
			//outFile << "\n";
			fprintf (pFile, "\n");
		}
	}	

	//outFile.close();
	fclose (pFile);


	
	return 0;
}

void findResult(DataItem** dataItm, int curIndex, int i, int j, int H, int W, int SINK_INDEX)
{
	if(i-1 >= 0 && dataItm[i-1][j].nextInd == curIndex) 
	{
		dataItm[i-1][j].sinkIndex = SINK_INDEX;
			findResult(dataItm, dataItm[i-1][j].index, i-1, j, H, W, SINK_INDEX);
	}
	if(i+1 < H && dataItm[i+1][j].nextInd == curIndex) 
	{
		dataItm[i+1][j].sinkIndex = SINK_INDEX;
			findResult(dataItm, dataItm[i+1][j].index, i+1, j, H, W, SINK_INDEX);
	}
	if(j-1 >= 0 && dataItm[i][j-1].nextInd == curIndex) 
	{
		dataItm[i][j-1].sinkIndex = SINK_INDEX;
			findResult(dataItm, dataItm[i][j-1].index, i, j-1, H, W, SINK_INDEX);
	}
	if(j+1 < W && dataItm[i][j+1].nextInd == curIndex) 
	{
		dataItm[i][j+1].sinkIndex = SINK_INDEX;
			findResult(dataItm, dataItm[i][j+1].index, i, j+1, H, W, SINK_INDEX);
	}
}