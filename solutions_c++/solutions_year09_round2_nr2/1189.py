#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int main()
{	
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int i=0; i<t; i++)
	{
		vector<int> arr;
		string line;
		in >> line;
		for(int j=0; j < line.size(); j++)
		{
			arr.push_back( line[j] - '0');
		}
		bool b=true;
		int k;
		for(int j=arr.size()-1; b&&j >0; j--)
		{
			k=j-1;
			int min=99;
			int pos=0;
			
				if( arr[k] < arr[j] )
				{
					for(int h=k; h<arr.size(); h++)
					{
						if(arr[h] > arr[k])
						{
							if(arr[h] < min)
							{
								min =arr[h];
								pos = h;
							}
						}
					}
					swap(arr[k], arr[pos]);
					sort(arr.begin()+k+1, arr.end());
					b=false;
				}
			
		}
		if( b)
		{
			sort(arr.begin(), arr.end());
			//for(int j=0; j <= arr.size()/2; j++)
				//swap(arr[j], arr[arr.size()-j-1]);
			if(arr[0]==0)
			for(int j=0; j<arr.size(); j++)
				if(arr[j] != 0)
				{
					swap ( arr[0], arr[j]);
					break;
				}
			arr.insert(arr.begin()+1, 0);
		}
		out <<"Case #"<< i+1 <<": ";
		for(int j=0; j < arr.size(); j++)
			out<< arr[j];
		out<<endl;

	}

	

	return 0;
}

