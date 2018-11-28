
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <string>

using namespace std;

const int M=100;
int buff[M][M];
char cbuff[M][M];
int mov[M*M];

int d1[]={-1,0,0,1};
int d2[]={0,-1,1,0};

void Process(int H,int W)
{
	memset(cbuff,0,sizeof(cbuff));
	
	char l='a';
	for (int h=0;h<H;++h)
	{
		for (int w=0;w<W;++w)
		{
			if (cbuff[h][w]) { continue; }

			int nP=0;
			int pH=h;
			int pW=w;
			bool bContinue=true;
			while(true)
			{
				int nS=-1;
				int min=buff[pH][pW];
				for (int s=0;s<4;++s)
				{
					if (pH+d1[s]<0||pH+d1[s]>=H) { continue; }
					if (pW+d2[s]<0||pW+d2[s]>=W) { continue; }
					if (buff[pH+d1[s]][pW+d2[s]]<min)
					{
						min=buff[pH+d1[s]][pW+d2[s]];
						nS=s;
					}
				}

				if (nS==-1) { break; }
				
				mov[nP]=nS;
				pH+=d1[nS];
				pW+=d2[nS];
				++nP;

				if (cbuff[pH][pW]) { break; }
			}
			
			char nL=(cbuff[pH][pW])?cbuff[pH][pW]:l++;
			for (int p=nP-1;p>=0;--p)
			{
				cbuff[pH][pW]=nL;
				pH-=d1[mov[p]];
				pW-=d2[mov[p]];
			}
			cbuff[h][w]=nL;
		}
	}
}

void ProcessFile(ifstream &fIn,ofstream &fOut)
{	
	const int nLen=3;
	string params[nLen];
	
	string line;
	getline(fIn,line);
	int nN=atoi(line.c_str());
	
	
	for (int i=0;i<nN;++i)
	{
		getline(fIn,line);
		size_t sep=line.find(" ");
		string sH(line.substr(0,sep));
		string sW(line.substr(sep+1,line.size()-sep));
		int H=atoi(sH.c_str());
		int W=atoi(sW.c_str());

		
		for (int i=0;i<H;++i)
		{
			getline(fIn,line);
			string s;
			
			int si=0;
			int j=0;
			while (true)
			{
				if (!line[si]||line[si]==' ')
				{
					buff[i][j]=atoi(s.c_str());
					s.clear();
					++j;
					if (!line[si]) { break; }
				}
				else
				{
					s+=line[si];
				}		
				++si;
			}
		}

		Process(H,W);
		fOut << "Case #" << (i+1) << ":\n";
		for (int i=0;i<H;++i)
		{
			fOut << cbuff[i][0];
			for (int j=1;j<W;++j)
			{
				fOut << " " << cbuff[i][j];
			}
			fOut << "\n";
		}
		
	}
}



int main(int argc, char* args[])
{
	string fsIn(args[1]);
	string fsOut(fsIn+".out");
	ifstream fIn(fsIn.c_str());
	ofstream fOut(fsOut.c_str());
	ProcessFile(fIn,fOut);
	fIn.close();
	fOut.close();
}