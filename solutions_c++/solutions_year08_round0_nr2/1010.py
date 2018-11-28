#include<iostream>
#include<vector>
#include<fstream>
#include<cstdlib>
#include<algorithm>

using namespace std;

int get_num(vector<int> dep, vector<int> arr,int taTime);
int main()
{
	int n;
	ifstream fin("B-large.in",ifstream::in);
	fin>>n;
	for(int i=1;i<=n;i++)
	{
		vector<int> depA;
		vector<int> arrA;
		vector<int> depB;
		vector<int> arrB;
		int startA = 0;
		int startB = 0; 	
		
		int taTime;
		fin>>taTime;
		int na,nb;
		fin>>na;
		fin>>nb;
		char temp[10];
		fin.getline(temp,10,'\n');
		for(int j=0;j<na;j++)
		{
			char myDHour[2];
			char myDMin[2];
			char myAHour[2];
			char myAMin[2];
			int hr,min,myTime;
			
			fin.getline(myDHour,5,':');
			hr = atoi(myDHour);
			fin.getline(myDMin,5,' ');
			min = atoi(myDMin);
			myTime = 100*hr + min;
			depA.push_back(myTime);

			fin.getline(myAHour,5,':');
			hr = atoi(myAHour);
			fin.getline(myAMin,5,'\n');
			min = atoi(myAMin);
			myTime = 100*hr + min;
			arrB.push_back(myTime);
		}

		for(int j=0;j<nb;j++)
		{
			char myDHour[2];
			char myDMin[2];
			char myAHour[2];
			char myAMin[2];
			int hr,min,myTime;
			
			fin.getline(myDHour,5,':');
			hr = atoi(myDHour);
			fin.getline(myDMin,5,' ');
			min = atoi(myDMin);
			myTime = 100*hr + min;
			depB.push_back(myTime);

			fin.getline(myAHour,5,':');
			hr = atoi(myAHour);
			fin.getline(myAMin,5,'\n');
			min = atoi(myAMin);
			myTime = 100*hr + min;
			arrA.push_back(myTime);
		}

		startA = get_num(depA,arrA,taTime);
		startB = get_num(depB,arrB,taTime);

		cout<<"Case #"<<i<<": "<<startA<<" "<<startB<<endl;
	}
}

int get_num(vector<int> dep, vector<int> arr,int taTime)
{
	int num = 0;
	sort(dep.begin(), dep.end());
	sort(arr.begin(), arr.end());

	for(int i=0;i<dep.size();i++)
	{
		if(arr.size() != 0)
		{
			int myHour = arr[0]/100;
			int myMin = arr[0]%100;
			myMin = myMin + taTime;
			if(myMin >= 60)
			{
				myHour++;
				myMin = myMin - 60;
			}
			int myTime = myHour*100 + myMin;

			if(dep[i] >= myTime)
				arr.erase(arr.begin()+0);
			else
				num++;
		}
		else
			num++;
	}
	return num;
}
