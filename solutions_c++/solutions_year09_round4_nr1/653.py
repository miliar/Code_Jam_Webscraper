#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<sstream>
#include<set>

using namespace std;

bool isvalid(vector<int> & data)
{
	for(int i=0;i<data.size();i++)
	{
		if(data[i]>i)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int cases;
	cin >> cases;

	for(int n=1;n<=cases;n++)
	{
		int retval = 0;
		int size;
		cin >> size;
		vector<string> grid(size);
		for(int i=0;i<size;i++)
		{
			cin >> grid[i];
		}
		vector<int> minrow(size);
		for(int i=0;i<size;i++)
		{
			minrow[i] = grid[i].rfind("1");
			if(minrow[i]==-1)
			{
				minrow[i] = 0;
			}
#ifdef DEBUG
//			cout << "Row: " << i << ": " << grid[i] << " minrow: " << minrow[i] << endl;
#endif
		}

		while(!isvalid(minrow))
		{
			//find min that isn't in place
			//without equal above it.
			//move it up
#ifdef DEBUG
//			cout << "Attempt: " << retval+1 << endl;
#endif
			for(int i=0;i<minrow.size();i++)
			{
#ifdef DEBUG
//				cout << "Row: " << i << " with val: " << minrow[i] << endl;
//				cout << "Compared to: " << minrow[i] << ", " << minrow[i-1] << endl;
#endif
#if 1
				if(minrow[i]>i)
				{
					//need to move this
					for(int j=i+1;j<minrow.size();j++)
					{
						if(minrow[j]<=i)
						{
#ifdef DEBUG
							cout << "Swapped " << j-1 << ", " << j << ": " << minrow[j] << ", " << minrow[j-1] << endl;
#endif
							swap(minrow[j],minrow[j-1]);
							break;
						}
					}
					retval++;
					break;
				}
#endif
#if 0
				if(minrow[i]<i)
				{
					if(minrow[i-1]>minrow[i])
					{
#ifdef DEBUG
//						cout << "Swapped" << endl;
#endif
						swap(minrow[i],minrow[i-1]);
						retval++;	
						break;
					}
				}
#endif
			}
		}

		cout << "Case #" << n << ": ";
		cout << retval;
		cout << endl;
	}
	return 0;
}
