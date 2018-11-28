#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Watershed
{
private:
	int _Height;
	int _Width;
	char MaxResult;

	vector<vector<int> > theMap;
	vector<vector<char> > theMapResult;

	char GetMaxResult()
	{
		char tempMaxResult = 'a';
		for (vector<vector<char> >::iterator iter=theMapResult.begin();iter!=theMapResult.end();++iter)
		{
			for (vector<char>::iterator iter2=iter->begin();iter2!=iter->end();++iter2)
			{
				tempMaxResult = max<char>(tempMaxResult,*iter2);
			}
		}
		return tempMaxResult;
	}
	
	bool checkPoint(int H,int W)
	{
		MaxResult  = GetMaxResult();
		int checkAltitude = theMap[H][W];
		// test case Altitude range is 0 ¡Ü altitudes < 10,000.
		double AltitudeOfNorth = 1000000;
		double AltitudeOfWest = 1000000;
		double AltitudeOfEast = 1000000;
		double AltitudeOfSouth = 1000000;

		if (H-1>=0)
		{
			if (checkAltitude > theMap[H-1][W])
				AltitudeOfNorth = theMap[H-1][W] + 0.1; // if AltitudeOfNorth=AltitudeOfWest will use AltitudeOfNorth
		}
		if (W-1>=0)
		{
			if (checkAltitude > theMap[H][W-1])
				AltitudeOfWest = theMap[H][W-1] + 0.2;
		}
		if (W+1<_Width)
		{
			if (checkAltitude > theMap[H][W+1])
				AltitudeOfEast = theMap[H][W+1] + 0.3;
		}
		if (H+1<_Height)
		{
			if (checkAltitude > theMap[H+1][W])
				AltitudeOfSouth = theMap[H+1][W] + 0.4;
		}

		int ChoosePointH;
		int ChoosePointW;

		double tmp = AltitudeOfNorth;
		ChoosePointH = H-1;
		ChoosePointW = W;
		if (tmp > AltitudeOfWest)
		{
			tmp = AltitudeOfWest;
			ChoosePointH = H;
			ChoosePointW = W-1;
		}
		
		if (tmp > AltitudeOfEast)
		{
			tmp = AltitudeOfEast;
			ChoosePointH = H;
			ChoosePointW = W+1;
		}

		if (tmp > AltitudeOfSouth)
		{
			tmp = AltitudeOfSouth;
			ChoosePointH = H+1;
			ChoosePointW = W;
		}

		if (tmp==1000000)
		{
			if (theMapResult[H][W]==0)
				theMapResult[H][W] = ++MaxResult;
			return false;
		}
		else
		{
			char Result = theMapResult[H][W];
			if (Result!=0)
			{
				if (theMapResult[ChoosePointH][ChoosePointW]==0)
				{
					theMapResult[ChoosePointH][ChoosePointW] = Result;
				}
				else 
				{
					if (theMapResult[ChoosePointH][ChoosePointW] < Result)
					{
						theMapResult[H][W] = theMapResult[ChoosePointH][ChoosePointW];
						if (H-1>=0 )
						{
							checkPoint(H-1,W); 
						}
						if (W-1>=0 )
						{
							checkPoint(H,W-1);
						}
						if (W+1<_Width )
						{
							checkPoint(H,W+1);
						}
						if (H+1<_Height)
						{
							checkPoint(H+1,W);
						}
					}
					else if (theMapResult[ChoosePointH][ChoosePointW] > Result)
					{
						theMapResult[ChoosePointH][ChoosePointW] = theMapResult[H][W];
						if (ChoosePointH-1>=0 )
						{
							checkPoint(ChoosePointH-1,ChoosePointW); 
						}
						if (ChoosePointW-1>=0 )
						{
							checkPoint(ChoosePointH,ChoosePointW-1);
						}
						if (ChoosePointW+1<_Width )
						{
							checkPoint(ChoosePointH,ChoosePointW+1);
						}
						if (ChoosePointH+1<_Height)
						{
							checkPoint(ChoosePointH+1,ChoosePointW);
						}
					}
				}
			}
			else 
			{
				if (theMapResult[ChoosePointH][ChoosePointW]!=0)
				{
					if (Result==0)
					{
						theMapResult[H][W] = theMapResult[ChoosePointH][ChoosePointW];
					}
				}
				else
				{
					Result = ++MaxResult;
					if (theMapResult[H][W]==0)
						theMapResult[H][W] = Result;
					if (theMapResult[ChoosePointH][ChoosePointW]==0)
						theMapResult[ChoosePointH][ChoosePointW] = Result;
				}
			}

		}
	}
public:
	Watershed(int Height,int Width) : _Height(Height),_Width(Width) 
	{
		theMap.resize(Height);
		for (vector<vector<int> >::iterator iter=theMap.begin();iter!=theMap.end();++iter)
		{
			iter->resize(Width);
		}

		theMapResult.resize(Height);
		for (vector<vector<char> >::iterator iter=theMapResult.begin();iter!=theMapResult.end();++iter)
		{
			iter->resize(Width);
		}
	}

	bool checkResult()
	{
		string temp = "";
		char tempMaxResult = 'a';
		for (vector<vector<char> >::iterator iter=theMapResult.begin();iter!=theMapResult.end();++iter)
		{
			for (vector<char>::iterator iter2=iter->begin();iter2!=iter->end();++iter2)
			{
				tempMaxResult = max<char>(tempMaxResult,*iter2);
				if (temp.find_first_of(*iter2) == -1)
					temp += *iter2;
			}
		}
		if (tempMaxResult-'a'+1 != temp.length())
		{
			sort(temp.begin(),temp.end());
			for (vector<vector<char> >::iterator iter=theMapResult.begin();iter!=theMapResult.end();++iter)
			{
				for (vector<char>::iterator iter2=iter->begin();iter2!=iter->end();++iter2)
				{
					int pos = temp.find_first_of(*iter2);
					if (pos > -1)
						*iter2 = 'a'+pos;
				}
			}
			return false;
		}
		else
		{
			return true;
		}
	}

	void AddAltitude(int H,int W,int Altitude)
	{
		theMap[H][W] = Altitude;
	}

	void Printout()
	{
		for (vector<vector<int> >::iterator iter=theMap.begin();iter!=theMap.end();++iter)
		{
			for (vector<int>::iterator iter2=iter->begin();iter2!=iter->end();++iter2)
			{
				cout << *iter2 << ' ';
			}

			cout << endl;
		}
	}

	void PrintoutResult(ofstream &fout)
	{
		for (vector<vector<char> >::iterator iter=theMapResult.begin();iter!=theMapResult.end();++iter)
		{
			for (vector<char>::iterator iter2=iter->begin();iter2!=iter->end();++iter2)
			{
				fout << *iter2 << ' ';
			}

			fout << endl;
		}
	}

	void Calculate()
	{
		if (theMapResult.empty() || theMap.empty())
			return;

		MaxResult = 'a';

		theMapResult[0][0] = MaxResult;
		for (int i=0 ; i<_Height ; ++i)
		{
			for (int j=0 ; j<_Width ; ++j)
			{
				checkPoint(i,j);
			}
		}

		checkResult();
	}
};

int main(int argc, char* argv[])  
{
    if(argc != 3)  
    {  
  		cout << "Usage: Watersheds INPUT_FILE OUTPUT_FILE" << endl;
        return 0;  
    }  

	//ifstream fin("test.in");
	//ofstream fout("test.out");
	ifstream fin(argv[1]);
	ofstream fout(argv[2]);

	if (!fin)
    {
        cout << "Read fail!" << endl;
        return 1;  
    }


	int mapNum;  
	int MapHeight;  
	int MapWidth;
	int Altitude;

	string Line;
	std::getline(fin, Line);
	
	mapNum = atoi(Line.c_str());
	for (int i=0 ; i<mapNum ; ++i)
	{
		std::getline(fin, Line);
		int pos = Line.find_first_of(" ");
		MapHeight = atoi(Line.substr(0,pos).c_str());
		Line = Line.substr(pos+1,Line.length()-pos);
		MapWidth = atoi(Line.c_str());

		Watershed watershed(MapHeight,MapWidth);
		
		for (int j=0 ; j<MapHeight ; ++j)
		{
			std::getline(fin, Line);
			for (int k=0 ; k<MapWidth ; ++k)
			{
				pos = Line.find_first_of(" ");
				Altitude = atoi(Line.substr(0,pos).c_str());
				watershed.AddAltitude(j,k,Altitude);

				Line = Line.substr(pos+1,Line.length()-pos);
			}
		}

		//watershed.Printout();

		watershed.Calculate();
		
		fout << "Case #" << i+1 << ':' << endl;
		watershed.PrintoutResult(fout);
		
	}	
}

