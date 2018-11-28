#include<string>
#include<iostream>
#include<fstream>
#include<vector>
#include<stack>

using namespace std;

#define North 1
#define West 2
#define East 4
#define South 8

class Plat
{
public:
	Plat(): Altitude(0), FlowOut(0), FlowIn(0),Mark(0) {}
	int Altitude;
	int FlowOut;
	int FlowIn;
	char Mark;
};

class Point
{
public:
	Point(void): X(0), Y(0) {}
	Point(int x, int y): X(x), Y(y) {}
	inline Point NorthPoint(void) const {return Point(X, Y-1);}
	inline Point WestPoint(void) const {return Point(X-1, Y);}
	inline Point EastPoint(void) const {return Point(X+1, Y);}
	inline Point SouthPoint(void) const {return Point(X, Y+1);}
	int X;
	int Y;
};

class Map
{
public:
	Map(const Point & size);
	inline Plat * PlatAt(const Point & pos) { return &data[pos.X + pos.Y * size.X]; }
	inline Plat * NorthPlat(const Point & pos) { if(pos.Y > 0) return &data[pos.X + (pos.Y-1) * size.X]; else return NULL; }
	inline Plat * WestPlat(const Point & pos) { if(pos.X > 0) return &data[(pos.X-1) + pos.Y * size.X]; else return NULL; }
	inline Plat * EastPlat(const Point & pos) { if(pos.X < size.X-1) return &data[(pos.X+1) + pos.Y * size.X]; else return NULL; }
	inline Plat * SouthPlat(const Point & pos) { if(pos.Y < size.Y-1) return &data[pos.X + (pos.Y+1) * size.X]; else return NULL; }
	Point Size(void) { return this->size; }
	void MarkRegions(void);

private:
	Point size;
	vector<Plat> data;
	bool markTree(const Point & pos, char mark);
};

Map::Map(const Point & size):data(size.Y * size.X),size(size)
{
}

void Map::MarkRegions()
{
	for(int y=0; y < this->size.Y; y++)
		for(int x=0; x < this->size.X; x++)
		{
			Point pos(x, y);
			Plat * pPlat = PlatAt(pos);
			Plat * pLowPlat = NULL;
			Plat * pCPlat = NorthPlat(pos);
			if(pCPlat && pCPlat->Altitude < pPlat->Altitude && ((pLowPlat && pCPlat->Altitude < pLowPlat->Altitude) || pLowPlat == NULL))
			{
				pLowPlat = pCPlat;
				pPlat->FlowOut = North;
			}
			pCPlat = WestPlat(pos);
			if(pCPlat && pCPlat->Altitude < pPlat->Altitude && ((pLowPlat && pCPlat->Altitude < pLowPlat->Altitude) || pLowPlat == NULL))
			{
				pLowPlat = pCPlat;
				pPlat->FlowOut = West;
			}
			pCPlat = EastPlat(pos);
			if(pCPlat && pCPlat->Altitude < pPlat->Altitude && ((pLowPlat && pCPlat->Altitude < pLowPlat->Altitude) || pLowPlat == NULL))
			{
				pLowPlat = pCPlat;
				pPlat->FlowOut = East;
			}
			pCPlat = SouthPlat(pos);
			if(pCPlat && pCPlat->Altitude < pPlat->Altitude && ((pLowPlat && pCPlat->Altitude < pLowPlat->Altitude) || pLowPlat == NULL))
			{
				pLowPlat = pCPlat;
				pPlat->FlowOut = South;
			}
			switch(pPlat->FlowOut)
			{
			case 0:
				break;
			case North:
				NorthPlat(pos)->FlowIn |= South;
				break;
			case West:
				WestPlat(pos)->FlowIn |= East;
				break;
			case East:
				EastPlat(pos)->FlowIn |= West;
				break;
			case South:
				SouthPlat(pos)->FlowIn |= North;
				break;
			}
		}

	char mark = 'a';
	for(int y=0; y < this->size.Y; y++)
		for(int x=0; x < this->size.X; x++)
		{
			Point pos(x, y);
			bool isMarked = this->markTree(pos, mark);
			if(isMarked)
				mark++;
		}
}

bool Map::markTree(const Point & pos, char mark)
{
	if(this->PlatAt(pos)->Mark)
		return false;

	typedef pair<Point, int> TravelNote; //(position, direction completed)
	stack<TravelNote> taravelPath;
	this->PlatAt(pos)->Mark = mark;
	taravelPath.push(TravelNote(pos, 0));
	while(!taravelPath.empty())
	{
		TravelNote & travelNote = taravelPath.top();

		const Point & currentPos = travelNote.first;
		Plat & currentPlat = *(this->PlatAt(currentPos));
		int & direction = travelNote.second;
		switch(direction)
		{
		case 0:
			direction = North;
			if(currentPlat.FlowOut == North || (currentPlat.FlowIn & North) != 0)
			{
				Point northPos = currentPos.NorthPoint();
				Plat * pPlat = this->PlatAt(northPos);
				if(pPlat && pPlat->Mark == 0)
				{
					pPlat->Mark = mark;
					taravelPath.push(TravelNote(northPos, 0));
				}
			}
			break;
		case North:
			direction = West;
			if(currentPlat.FlowOut == West || (currentPlat.FlowIn & West) != 0)
			{
				Point westPos = currentPos.WestPoint();
				Plat * pPlat = this->PlatAt(westPos);
				if(pPlat && pPlat->Mark == 0)
				{
					pPlat->Mark = mark;
					taravelPath.push(TravelNote(westPos, 0));
				}
			}
			break;
		case West:
			direction = East;
			if(currentPlat.FlowOut == East || (currentPlat.FlowIn & East) != 0)
			{
				Point eastPos = currentPos.EastPoint();
				Plat * pPlat = this->PlatAt(eastPos);
				if(pPlat && pPlat->Mark == 0)
				{
					pPlat->Mark = mark;
					taravelPath.push(TravelNote(eastPos, 0));
				}
			}
			break;
		case East:
			direction = South;
			if(currentPlat.FlowOut == South || (currentPlat.FlowIn & South) != 0)
			{
				Point southPos = currentPos.SouthPoint();
				Plat * pPlat = this->PlatAt(southPos);
				if(pPlat && pPlat->Mark == 0)
				{
					pPlat->Mark = mark;
					taravelPath.push(TravelNote(southPos, 0));
				}
			}
			break;
		case South:
			taravelPath.pop();
		}
	}
	return true;
}


class Data
{
public:
	Data(string filename);
	~Data(void);
	vector<Map*> MapPts;
	void Display(void);
	void SaveResult(string filename);
};

Data::Data(string filename)
{
	ifstream in(filename.c_str());
	int mapCount;
	Point size;
	in>>mapCount;
	MapPts.resize(mapCount);
	for(int i=0; i<mapCount; i++)
	{
		in>>size.Y>>size.X;
		MapPts[i] = new Map(size);
		for(int y=0; y<size.Y; y++)
			for(int x=0; x<size.X; x++)
			{
				int altitude;
				in>>altitude;
				MapPts[i]->PlatAt(Point(x, y))->Altitude = altitude;
			}
	}

}

Data::~Data()
{
	for(vector<Map*>::iterator iter = this->MapPts.begin(); iter < this->MapPts.end(); iter++)
	{
		delete *iter;
	}
}

void Data::Display()
{
	for(vector<Map*>::iterator iter = this->MapPts.begin(); iter < this->MapPts.end(); iter++)
	{
		Point size = (*iter)->Size();
		cout<<size.Y<<" "<<size.X<<endl;
		for(int y=0; y<size.Y; y++)
		{
			for(int x=0; x<size.X; x++)
			{
				cout<<(*iter)->PlatAt(Point(x, y))->Altitude<<" ";
			}
			cout<<endl;
		}
	}
}

void Data::SaveResult(string filename)
{
	ofstream out(filename.c_str());
	for(vector<Map*>::size_type mapIndex=0; mapIndex<this->MapPts.size(); mapIndex++)
	{
		Map & currentMap = *(this->MapPts[mapIndex]);
		out<<"Case #"<<mapIndex+1<<":"<<endl;
		for(int y=0; y<currentMap.Size().Y; y++)
		{
			for(int x=0; x<currentMap.Size().X; x++)
			{
				out<<currentMap.PlatAt(Point(x,y))->Mark<<" ";
			}
			out<<endl;
		}
	}
}

int main(int argc, char *argv[])
{
	Data data("B-large.in");
	//data.Display();

	for(vector<Map*>::size_type mapIndex=0; mapIndex<data.MapPts.size(); mapIndex++)
	{
		data.MapPts[mapIndex]->MarkRegions();
		cout<<mapIndex<<endl;
	}
	data.SaveResult("B-large.out");

	return 0;
}