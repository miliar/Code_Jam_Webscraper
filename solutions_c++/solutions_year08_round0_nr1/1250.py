#include<iostream>
#include<vector>
#include<string>

using namespace std;

int findmin(int **matrix, int m, int nEngines)
{
	int minVal = 9999999999;
	
	for (int i =0;i<nEngines;i++)
	{
		if (matrix[i][m] != -1 && matrix[i][m] < minVal)
			minVal = matrix[i][m];
		
	}
	return(minVal);		
		

}

int main()
{
	int ntestCases;
	cin>>ntestCases;
	
	int count=1;	
	// for all test cases 
	while(count<=ntestCases)
	{
		
		// Individual test cases
		int nEngines, nQueries;
		cin>>nEngines;
		//cout<<nEngines<<nQueries<<endl;

		vector<string> engines, queries;
		engines.clear(); queries.clear();
	
		string tempstr;
		getline(cin,tempstr);	
		// read engine names  
		for (int i =0;i<nEngines;i++)
		{
			getline(cin,tempstr);
			//cout<<tempstr<<endl;
			engines.push_back(tempstr);
		}
		
		cin>>nQueries;
		
		//cout<<nEngines<<" "<<nQueries<<endl;
		//break;
		
		// read queries 

		getline(cin,tempstr);	
		for(int i =0;i<nQueries;i++)
		{
			getline(cin,tempstr);
			//cout <<tempstr<<endl;
			queries.push_back(tempstr);
		}
		
		//cout<<nQueries<<endl;	
		//cout<<"I am here"<<endl;	
		
		// Processing start here 
		// 2-D DTW

		//Assign Memory
		int **matrix;
		matrix = new int*[nEngines];
		for (int i =0;i<nEngines;i++)
			matrix[i] = new int[nQueries+1];
		
		
		//cout<<"I am here"<<endl;	
		for (int i =0;i<nEngines;i++)
			matrix[i][0] = 0;
	
		//cout<<"I am here"<<endl;	
		for (int i =1;i<=nQueries;i++)
		{
			for (int j =0;j<nEngines;j++)
			{		
				//cout<<i<<" "<<j<<endl;
				if(queries[i-1]==engines[j])
				{
					matrix[j][i]=-1;
				}
				else if(matrix[j][i-1]== -1)
				{
					matrix[j][i] = findmin(matrix,i-1,nEngines) + 1;
				}
				else 
				{
					matrix[j][i]= matrix[j][i-1];
				}		
			}
		}
		
		//cout<<"I am here"<<endl;	
	
		//cout<<nEngines<<" "<<nQueries<<endl;
		cout<<"Case #"<<count<<": "<<findmin(matrix,nQueries,nEngines)<<endl;
		count++;
		
		/*for(int i =0;i<nEngines;i++)
		{
			for (int j=0;j<=nQueries;j++)
				cout<<matrix[i][j]<<" ";
			cout<<endl;
		}*/	
		

		// Delete Memory
		for(int i=0;i<nEngines;i++)
			delete(matrix[i]);
		delete(matrix);	
		
		
	}
	return(0);

}
