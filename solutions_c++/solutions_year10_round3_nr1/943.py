#include<iostream>
#include <map>
#include <vector>
#include <string>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int tc;
	cin >> tc;
	for(unsigned int i=0;i<tc;i++)
	{
		int numWires;
		vector <int> leftHeight;
		vector <int> rightHeight;
		cin >> numWires;

		for(int j=0;j<numWires;j++)
		{
			int v;
			cin >> v;
			leftHeight.push_back(v);
			cin >> v;
			rightHeight.push_back(v);
		}

		int numdots = 0;
		for(int j=0;j<numWires;j++)
		{
			for(int k=j;k<numWires;k++)
			{
				if(j==k)
					continue;
				if((leftHeight[j]>leftHeight[k]) && (rightHeight[j]<rightHeight[k]))
					numdots++;
				else
				if((leftHeight[j]<leftHeight[k]) && (rightHeight[j]>rightHeight[k]))
					numdots++;
			}
		}
		cout << "Case #"<<i+1<<": "<<numdots<<endl;
	}
	return 0;
}
