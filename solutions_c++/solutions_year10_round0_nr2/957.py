#include "iostream"
#include "fstream"
#include <vector>
#include <string>
using namespace std;

struct Employee
{
	int H;	//the home town
	int P;	//the number of passengers
}
typedef EMPLOYEE;

int process(vector<EMPLOYEE> arr, int numOfTowns,int homeTown, int *result);
void sapgiam(vector<EMPLOYEE> &arr);


void main()
{
	ifstream fin;
	ofstream fout;
	int C;	//number of testcases

	fin.open("B-large-practice.in", ios_base::in);
	fout.open("B-large-practice.out", ios_base::out);

	fin>>C;

	for(int i=1; i<=C; i++)
	{
		int N;
		int T;
		int E;	//number of employees
		vector<EMPLOYEE> arrEM;
		int *result;

		fin>>N;
		fin>>T;
		fin>>E;
		fout<<"Case #"<<i<<": ";
		result  = new int[N];
		for(int j=0; j<E; j++)
		{
			EMPLOYEE em;
			fin>>em.H;
			fin>>em.P;
			arrEM.push_back(em);
		}
		
		//process
		if(process(arrEM, N, T,result))
		{
			result[T-1]=0;
			for(int j=0; j<N; j++)
			{				
				fout<<result[j];
				if(j<N-1)
					fout<<" ";
			}
		}
		else
			fout<<"IMPOSSIBLE";

		if(i<C)
			fout<<endl;
	}

	fin.close();
	fout.close();
}

int process(vector<EMPLOYEE> arr, int numOfTowns,int homeTown, int *result)
{
	vector<vector<EMPLOYEE>> a;
	a.resize(numOfTowns);

	for(unsigned int i=0; i<arr.size(); i++)
	{		
		EMPLOYEE em =  arr[i];
		a[em.H-1].push_back(arr[i]);
	}

	for(int i=0; i<numOfTowns; i++)
	{
		int numPassenger	= 0;	
		int count			= 0;
		int maxPassenger	= 0;
		result[i] = 0;
		sapgiam(a[i]);

		if(a[i].size() > 0 && a[i][0].P==0 && a[i][0].H!=homeTown)
		{
			return 0;
		}
		
		for(unsigned int j = 0; j < a[i].size(); j++)
		{
			if(a[i][j].P > 0)
			{
				count++;
				numPassenger += a[i][j].P;
				if(maxPassenger<a[i][j].P)
					maxPassenger = a[i][j].P;
			}
			if(numPassenger >= a[i].size())
			{
				result[i] = count;
				break;
			}
		}
		if(numPassenger < a[i].size() && i+1!=homeTown)
			return 0;
	}
	return 1;
}
void sapgiam(vector<EMPLOYEE> &arr)
{
	if(arr.size()==0)
		return;
	for(unsigned int i = 0; i < arr.size()-1; i++)
	{
		for(unsigned int j = i+1; j < arr.size(); j++)
		{
			if(arr[i].P < arr[j].P)
			{
				EMPLOYEE tmp = arr[i];
				arr[i] = arr[j];
				arr[j] = tmp;
			}
		}
	}
}