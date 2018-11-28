#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <istream>
#include <fstream>
#include <cmath>
#include <map>
#include <set>
using namespace std;

int num;
int n;
int arr[41];

void getResult()
{
	num = 0;
	for ( int i = 0; i < n; i++ )
	{
		if(arr[i] <= i)continue;
		int temp = arr[i];
		for( int j = i+1; j < n; j++ )
		{
			num++;
			if( arr[j] <= i )
			{
				arr[i] = arr[j];
				arr[j] = temp;
				break;
			}
			int t = arr[j];
			arr[j] = temp;
			temp = t;
		}
	}
}

int main()
{
	ifstream fin("A-large.in");  
	ofstream fout("results.txt");
	int caseNum;
	string str;
	
	fin >> caseNum;
	for ( int i = 1; i <= caseNum; i++ )
	{
		fin >> n;
		for ( int j = 0; j < n; j++ )
		{
			fin >> str;
			int temp = -1;
			for( int k = n-1; k >= 0; k-- )
			{
				if(str[k] == '1')
				{
					temp = k;
					break;
				}
			}
			arr[j] = temp;
		}
		getResult();
		fout << "Case #" << i << ": " << num << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}