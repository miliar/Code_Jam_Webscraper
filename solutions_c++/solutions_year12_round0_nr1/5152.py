#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int T;
	string G, X;
	vector<string> Gs, Xs;
	
	ifstream inFile( "A-small-attempt0.in" );
	ofstream outFile( "A-small.txt" );

	inFile >> T;	
	
	while(getline(inFile, G))
	{
		Gs.push_back(G);
	}

	string s1 = "abcdefghijklmnopqrstuvwxyz ";
	string s2 = "yhesocvxduiglbkrztnwjpfmaq ";
	for(int i = 1; i <= T; i++)
	{
		X = "";
		for(int j = 0; j < Gs[i].size(); j++)
		{
			char temp = s2[s1.find(Gs[i][j])];
			X += temp;
		}
		Xs.push_back(X);
	}
    
	for(int i = 0; i < T; i++)
	{
		outFile << "Case #" << i+1 << ": " << Xs[i] << endl;
	}
	return 0;
}
