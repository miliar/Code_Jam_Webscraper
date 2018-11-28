// googleCodeContest.cpp : Defines the entry point for the console application.
//

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

int main()
{
	ifstream f("A-small.in");
	ofstream of("A-small-out.txt");
	int cases;
	int searchEngines;
	int queries;
	int switches;
	int numleft;
	string query;
	string Engines[20];
	bool usedEngine[20];

	int w, x, y, z;

	f >> cases;
//	cout << cases;
	for(x=0; x<cases; x++)
	{
		f >> searchEngines;
		numleft=searchEngines;
//		cout << searchEngines;
		getline(f, query); // flush the linefeed at the end
		for(y=0; y<searchEngines; y++)
		{
			getline(f, Engines[y]);
			usedEngine[y]=false;
//			cout << y;
//			cout << Engines[y];
		}
		switches=0;
		f >> queries;
		getline(f, query); // flush the linefeed at the end
		for(z=0; z<queries; z++)
		{
			getline(f,query);
//			cout << query;
//			cout << "Query #"<< z <<": " << query;
			for(y=0; y<searchEngines; y++)
			{
				if(Engines[y]==query)
				{
//					cout << "Matches engine #" << y << ": " << Engines[y] << endl;
					if(!usedEngine[y])
					{
						numleft-=1;
						if(numleft<1)
						{
							for(w=0; w<searchEngines; w++)
							{
								usedEngine[w]=false;
							}
							switches++;
							numleft=searchEngines-1;
						}
						usedEngine[y]=true;
						continue;
					}
				} 
			}
//			cout << endl;
		}
		of << "Case #" << (x+1) << ": " << switches << endl;
	}
	f.close();
	of.close();


	cout << "Done." << endl;

    char a;
	cin >> a;
	return 0;
}
