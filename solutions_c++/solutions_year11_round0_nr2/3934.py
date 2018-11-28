#include<iostream>
#include<vector>
using namespace std;

int arr[128][128];
int arr2[128][128];


string convert(string current)
{
	if(current.size() <= 1)
		return current;
	
	string newString;
	int pos = current.size()-1;
	if( arr[current[pos]][current[pos-1]] > 0)
	{
		newString = current.substr(0,pos-1);
		newString.push_back( (char) arr[current[pos]][current[pos-1]]);
		
		return convert(newString);
	}
	
	for(int i = 0; i < pos;i++)
	{
		if( arr2[current[pos]][current[i]] == -1)
			return "";
	}
	
	return current;
	


}



int main()
{
	int T;
	cin >> T;
	for(int testCase = 0; testCase < T;testCase++)
	{
		
		memset(arr,0,sizeof(arr));
		memset(arr2,0,sizeof(arr2));
		int c;
		cin >> c;
		for(int i = 0; i < c;i++)
		{
			string g;
			cin >> g;
			char x,y,z;
			x = g[0];
			y = g[1];
			z = g[2];
			arr[x][y] = z;
			arr[y][x] = z;
		}
		
		int d;
		cin >> d;
		for(int i = 0; i < d;i++)
		{
			string g;
			cin >> g;
			char x = g[0];
			char y = g[1];
			arr2[x][y] = -1;
			arr2[y][x] = -1;
		}
		int N;
		cin >> N;
		string input;
		cin >> input;
		//cout << "input is " << input << endl;
		string current = "";
		for(int i = 0; i < input.size();i++)
		{
			current += input[i];
			current = convert(current);
			//cout << "current is " << current << endl;
		}
		
		cout << "Case #" << testCase+1 << ": ";
		if(current.size() == 0)
		{
			cout << "[]" << endl;
		}
		else
		{
			cout << "[";
			for(int i = 0; i < current.size()-1;i++)
			{
				cout << current[i] << ", ";
			}
			cout << current[current.size()-1] << "]" << endl;
		}
		
		
	}
	
}