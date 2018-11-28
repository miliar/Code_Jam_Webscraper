#include <iostream>
using namespace std;
#include <fstream>
#include <string>
#include <vector>
#include <map>


class coordinate{
public:
	int x,y;	
	coordinate(){x=y=-1;}
	coordinate(int _x,int _y){x=_x;y=_y;}
	coordinate inverse(){return coordinate(y,x);}

};

void LoadMap(vector<vector<vector<int>>> &tbl){
	ifstream fin("B-large.in");
	string temp;
	getline(fin, temp, '\n');
	int t = atoi(temp.c_str());
	tbl.resize(t);
	for(int i=0;i<t;++i)
	{
		getline(fin, temp, ' ');
		int h = atoi(temp.c_str());
		getline(fin, temp, '\n');
		int w = atoi(temp.c_str());
		tbl[i].resize(h);
		for(int j=0;j<h;++j)tbl[i][j].resize(w);

		for(int j=0;j<h;++j)
		{
			for(int k=0;k<w;++k)
			{
				fin >> tbl[i][j][k];
				fin.get();
			}
		}
	}
}

coordinate traceFlow(coordinate startingPt,vector<vector<int>> &theMap,vector<vector<coordinate>> &basins)
{
	int height=theMap[startingPt.x][startingPt.y];
	int neighbors[4];
	if(startingPt.y>0)neighbors[1]=theMap[startingPt.x][startingPt.y-1];
	else neighbors[1]=10001;
	if(startingPt.x>0)neighbors[0]=theMap[startingPt.x-1][startingPt.y];
	else neighbors[0]=10001;
	if(startingPt.x<theMap.size()-1)neighbors[3]=theMap[startingPt.x+1][startingPt.y];
	else neighbors[3]=10001;
	if(startingPt.y<theMap[0].size()-1)neighbors[2]=theMap[startingPt.x][startingPt.y+1];
	else neighbors[2]=10001;
	int currentLow=height;
	int choice=-1;
	for(int i=0;i<4;++i)
	{
		if(neighbors[i]<currentLow)
		{
			choice=i;
			currentLow=neighbors[i];
		}
	}
	switch(choice)
	{
	case -1:
		return startingPt.inverse();
	case 1:
		if((basins[startingPt.x][startingPt.y-1]).x!=-1)return (basins[startingPt.x][startingPt.y-1]);
		else return traceFlow(coordinate(startingPt.x,startingPt.y-1),theMap,basins);
	case 0:
		if((basins[startingPt.x-1][startingPt.y]).x!=-1)return (basins[startingPt.x-1][startingPt.y]);
		else return traceFlow(coordinate(startingPt.x-1,startingPt.y),theMap,basins);
	case 3:
		if((basins[startingPt.x+1][startingPt.y]).x!=-1)return (basins[startingPt.x+1][startingPt.y]);
		else return traceFlow(coordinate(startingPt.x+1,startingPt.y),theMap,basins);
	case 2:
		if((basins[startingPt.x][startingPt.y+1]).x!=-1)return (basins[startingPt.x][startingPt.y+1]);
		else return traceFlow(coordinate(startingPt.x,startingPt.y+1),theMap,basins);
	}
}

void findBasins(vector<vector<vector<coordinate>>> &basins, vector<vector<vector<int>>> &maps){
	basins.resize(maps.size());
	for(int i=0;i<maps.size();++i)
	{
		basins[i].resize(maps[i].size());
		int sze = maps[i].size();
		for(int j=0;j<sze;++j)
		{
			basins[i][j].resize(maps[i][j].size());
		}
	}

	for(int i=0;i<maps.size();++i)
	{
		for(int j=0;j<maps[i].size();++j)
		{
			for(int k=0;k<maps[i][j].size();++k)
			{
				basins[i][j][k] = traceFlow(coordinate(j,k),maps[i],basins[i]);
			}
		}
	}
	
}

int key(coordinate c){return c.x*1000+c.y;}

void labelBasins(vector<vector<vector<char>>> &basinsLabeled, vector<vector<vector<coordinate>>> &basins)
{
	basinsLabeled.resize(basins.size());
	for(int i=0;i<basins.size();++i)
	{
		basinsLabeled[i].resize(basins[i].size());
		int sze = basins[i].size();
		for(int j=0;j<sze;++j)
		{
			basinsLabeled[i][j].resize(basins[i][j].size());
		}
	}

	for(int i=0;i<basins.size();++i)
	{
		map<int,char> labels;
		for(int j=0;j<basins[i].size();++j)
		{
			for(int k=0;k<basins[i][j].size();++k)
			{
				map<int,char>::iterator data = labels.find(key(basins[i][j][k]));
				if(data == labels.end())
				{
					labels[key(basins[i][j][k])] = labels.size()+'a';
					basinsLabeled[i][j][k]= labels.size()+'a'-1;
				}
				else
				{
					basinsLabeled[i][j][k]=data->second;
				}
				
			}
		}
	}	
}

int main(void)
{

	vector<vector<vector<int>>> theMaps;
	LoadMap(theMaps);

	vector<vector<vector<coordinate>>> basins;
	findBasins(basins,theMaps);

	vector<vector<vector<char>>> basinsLabeled;
	labelBasins(basinsLabeled,basins);

	ofstream fout("B-large.out");
	for(int i=0;i<basinsLabeled.size();++i)
	{
		fout << "Case #"<<i+1<<":\n";
		for(int j=0;j<basinsLabeled[i].size();++j)
		{
			for(int k=0;k<basinsLabeled[i][j].size();++k)
			{
				fout << basinsLabeled[i][j][k];
				if(k<basinsLabeled[i][j].size()-1)fout<<' ';
			}
			fout << '\n';
		}
	}
	return 0;
}
