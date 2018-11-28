#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct line
{
	int start;
	int end;
};

line arr[1000];

int main()
{
	ifstream in("i.txt");
	ofstream out("output.txt");

	int cases, N, numSect;
	in >> cases;
	
	for(int c=0; c<cases; c++)
	{
		numSect=0;
		in >> N;
		for(int i=0; i<N; i++)
			in >> arr[i].start >> arr[i].end;
		for(int i=0; i<N-1; i++)
			for(int j=i+1; j<N; j++)
				if( ((arr[i].start > arr[j].start)&&(arr[i].end < arr[j].end))
					|| ((arr[i].start < arr[j].start)&&(arr[i].end > arr[j].end)) )
					numSect++;
		out << "Case #" << c+1 << ": " << numSect << endl;
	}

}