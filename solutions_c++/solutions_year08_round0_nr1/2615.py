#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int S_MAX=100; //Maximum number of search engines
int Q_MAX=1000; //Maximum number of queries


void setfalse(bool* arr, int size_s);
bool checktrue(bool* arr, int size_s);

int main()
{
	
	ifstream fin;
	ofstream fout;
	fin.open("A-small.in");
	fout.open("A-small.out");
	
	int n_cases, size_s, size_q, current_case=1;
	char s[S_MAX][100], q[Q_MAX][100];
	
	char temp[100];
	fin.getline (temp, 100);
	n_cases = atoi (temp);
	//cout << n_cases;
	while (current_case <= n_cases)
	{
		int switch_count=0;
		fin.getline (temp, 100);
		size_s = atoi (temp);
		//cout << "*** " << size_s << endl;
		for(int i = 0; i < size_s; i++)
		{
			fin.getline (s[i], 100);
			//cout << current_case << " " << i << " " << s[i] << endl;
		}
	
		
		fin.getline (temp, 100);
		size_q = atoi (temp);
		//cout << "*** " << size_q << endl;
		for(int i = 0; i < size_q; i++)
		{
			fin.getline (q[i], 100);
			//cout << current_case << " " << i << " " << q[i] << endl;
		}
				
		
		
		bool check_furthest[size_s];
		setfalse (check_furthest, size_s);
		
		for(int y = 0; y < size_q; y++)
		{
			for(int i = 0; i < size_s; i++) // Go through all the search engines
			{
				if (strcmp (q[y], s[i]) == 0) //If current query is equal to the search engine
					check_furthest[i] = true; //Set the checking array for that SE to true
			}
		
			if (checktrue (check_furthest, size_s) == true)//If all of the search engine names have been queried
			{
				switch_count++; //A switch is needed: increment switch count
				setfalse (check_furthest, size_s); //Reset checking array
				y--;
			}
		
		}

		
		fout << "Case #" << current_case << ": " << switch_count << endl;
		
		current_case++;
	}	
	
	fin.close();
	fout.close();
	
	return 0;
}




void setfalse (bool* arr, int size_s)
{
	for (int i = 0; i < size_s; i++) //For all of the array
		arr[i] = false; //Set to false
}

bool checktrue (bool* arr, int size_s)
{
	for (int i = 0; i < size_s; i++) //Go through the array
		if (arr[i] == false) //If any one of the array has a false element
			return false; //Then return false
	return true; //If the array has only true elements, return true
}