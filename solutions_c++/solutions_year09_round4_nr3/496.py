#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

bool check(vector<int>& v1, vector<int>& v2)
{
	if( v1[0] - v2[0] == 0 )
		return false;
	int h = (v1[0] - v2[0])/ abs( v1[0] - v2[0]) ;
	for(int  i =1; i < v1.size() ; i++)
	{
		if( h* ( v1[i] - v2[i] ) <= 0)
			return false;
	}
	return true;
}
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int t;
	in >> t;
	for(int test = 0; test < t; test++)
	{
		int k, n;
		in >> n >> k;
		vector< vector<int> > vec(n);
		for(int i = 0; i < n; i++)
		{
			for(int j = 0 ; j < k ; j++)
			{
				int temp;
				in >> temp;
				vec[i].push_back(temp);
			}
		}
		int min = 9999999;
		for(int h = 0; h < 100; h++)
		{

			for(int i = 0; i < 1000; i ++  )
			{
				swap( vec[ rand()%n ], vec[ rand()%n] );
			}
			int alias[100];
			for(int i = 0; i < n; i++)
			{
				alias[i] = i;
			}
			swap(vec[0], vec[n-1]);
			for(int i = 0 ; i < n-1; i++)
			{

				for( int j = i+1;  j < n; j++)
				{
					if( alias[j] == j )
					{
						bool b = true;
						for(int k=0; k < n; k ++)
						{
							if( alias[k] == i)
							{
								if( ! check(vec[k], vec[j]) )
								{
									b = false;
									break;
								}

							}
						}
						if( b)
						{
							alias[j] = i;
						}
					}
				}

			}

			set<int> count;
			for(int i = 0; i < n; i++)
			{
				count.insert( alias[i]);
			}
			if( count.size() < min )
				min = count.size();
		}
		
		out<<"Case #"<<test+1<<": "<< min << endl;

	}
	return 0;
}