#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <iomanip>


using namespace std;

int Perfect_Harmony(int l,int h,vector<int > freq);

int main (int argc, char * const argv[]) 
{
	int t,n,l,h,temp;	
	
	ifstream fichier("C-small-attempt0.in.txt", ios::in);
	
	vector<int> frq;
	vector<int> sortie;
	
	fichier>>t;
	
	for (int i=0; i<t; i++) 
	{
		fichier>>n>>l>>h;
		for (int j=0; j<n; j++) 
		{
			fichier>>temp;
			frq.push_back(temp);
		}	
		
		sortie.push_back(Perfect_Harmony(l,h,frq));
		frq.clear();
		
	}
	
	
	ofstream output("output.out", ios::out | ios::trunc);

	for (int i=0; i<sortie.size(); i++) 		
	{
		if(sortie[i]==-1)
			output << "Case #"<<i+1<<": NO"<<"\n";
		else
			output << "Case #"<<i+1<<": "<<sortie[i]<<"\n";

	
	}	
			
	
	//for (int i=0; i<sortie.size(); i++) 
	//{
	//	cout <<sortie[i]<<" ";
	//}
	
    return 0;
}

int Perfect_Harmony(int l,int h,vector<int > freq)
{
	vector<int > plage;
	
	vector<int>temp(freq.size());
	
	copy(freq.begin(), freq.end(), temp.begin());
	
	sort(temp.begin(), temp.end());
	
	
	for (int i=l; i<=h; i++) 
	{
		plage.push_back(i);
		//cout << i<<"  ";
	}
	
	//cout <<"\n\n";
	
	
	
	int s=-1;
	bool b;
	
	for (int j=0; j<plage.size(); j++) 
	{
		b=true;
		
		for (int i=0; i<temp.size(); i++) 	
		{
			s=plage[j];
			
			if(plage[j]>temp[i])
			{
				if(plage[j]%temp[i]!=0)
					b=false;
			}
			else 
			{
				if(temp[i]%plage[j]!=0)
					b=false;
			}
			
			if(!b)
				break;

		}
		if(b)
			break;
	}
	if(b)
		return s;
	else
		return -1;
	
	
}