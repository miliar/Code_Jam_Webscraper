#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>





using namespace std;


int getTimeFromString(string time)
	{
		char temp[4];
		int k=0;
		for(int i=0;i<time.size();i++)
			if(i!=2)
			{
				temp[k]=time[i];
				k++;
			}	
		
		return atoi(temp);
	}


bool removeTime(vector<int> &dep,int arrTime)
	{
		if(dep.size()==0) return false;
		for(int i=0;i<dep.size();i++)
			{

			

				if(dep[i]>=arrTime)
				{
					dep.erase(dep.begin()+i);
					return true;
					
				}

			}
		return false;

	}


int getNoOfTrain(vector<int> &dep,vector<int> &arr)
		{

		


			for(int i=0;i<arr.size();i++)
				{
							
					if(removeTime(dep,arr[i]))
						arr[i]=-1;

				
				

				}

			
			return dep.size();


		}




void main(){

	int totalCases;
	ifstream infile;
	ofstream outfile;

	
	
	infile.open("input.in");		 // open Input File "Input.in"
	outfile.open("output.in");       // open for Output

	infile>>totalCases;           // read total case from InputFile

	


	
for(int z=1;z<=totalCases;z++)
	{

		vector<int> depA,depB,arrA,arrB;
		int turnATime;
		int totalATrains,totalBTrains;
		

		infile>>turnATime;
		infile>>totalATrains;
		infile>>totalBTrains;
		
		for(int a=0;a<totalATrains;a++)
			{
				string arrTime,depTime;
				infile>>depTime;
				depA.push_back(getTimeFromString(depTime));
				infile>>arrTime;
				arrA.push_back(getTimeFromString(arrTime)+turnATime);
			}

		for(int b=0;b<totalBTrains;b++)
			{
				string arrTime,depTime;
				infile>>depTime;
				depB.push_back(getTimeFromString(depTime));
				infile>>arrTime;
				arrB.push_back(getTimeFromString(arrTime)+turnATime);
			}

		sort(depA.begin(),depA.end());
			
		sort(depB.begin(),depB.end());
		sort(arrA.begin(),arrA.end());
		sort(arrB.begin(),arrB.end());
		

		totalATrains = getNoOfTrain(depA,arrB);
		totalBTrains = getNoOfTrain(depB,arrA);
	
		

		outfile<<"Case #"<<z<<": "<<totalATrains<<" "<<totalBTrains<<endl;

	}//totalCases

	infile.close();
	outfile.close();



			
}//main

