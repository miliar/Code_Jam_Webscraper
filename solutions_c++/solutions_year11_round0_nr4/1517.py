#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>

using namespace std;

double goro(vector<int> nbr);
int main (int argc, char * const argv[]) {
    
	int t,n,temp;
	ifstream fichier("A-small-practice.in.txt", ios::in);
	
	fichier>>t;
	
	vector<int> nbr;

	vector<double> sortie;
	
	 	
	for (int i=0; i<t; i++) 
	{
		fichier>>n;
		for (int j=0; j<n; j++) 
		{
			fichier>>temp;
			nbr.push_back(temp);
		}	
		
		sortie.push_back(goro(nbr));
		nbr.clear();
		
	}
	
	cout.precision(6);
	
	ofstream output("output.out", ios::out | ios::trunc);
	for (int i=0; i<sortie.size(); i++) 		
	 output << "Case #"<<i+1<<": "<<setprecision (5)<<sortie[i]<<"\n";

	
	
    
    return 0;
}

double goro(vector<int> nbr)
{
	vector<int>temp(nbr.size());
	copy(nbr.begin(), nbr.end(), temp.begin());
	sort(temp.begin(), temp.end());
	double n=0.000000;
	
	for (int i=0; i<temp.size(); i++) 
	{
		if(temp[i]!=nbr[i])
			n++;
	}
	
	return n;
	
	
}
