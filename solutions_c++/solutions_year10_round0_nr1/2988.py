#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void main()
{
	int t=0, n=0, k=0, i=1;
	string light = "OFF";
	ifstream in;
	in.open("A-large.in");
	ofstream out;
	out.open("snapper.txt");
	int arr[30];
	arr[0] = 1;
	for(int i = 1; i < 30; i++)
		arr[i] = (arr[i-1]*2)+1;

	in >> t;

	while(t>0)
	{
		in >> n >> k;

		while(k > arr[n-1])
			k = k-(arr[n-1]+1);

		if(k == arr[n-1])
			light = "ON";
		else
			light = "OFF";
		out << "Case #" << i << ": " << light << endl;
		i++;
		t--;
	}
	out.close();
}