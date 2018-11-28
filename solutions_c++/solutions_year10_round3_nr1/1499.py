/*
 *  main.cpp
 *  
 *  Created by Jack Cohen on 22/05/
*/

#include <utility>
#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>


using namespace std;

int main()
{	

	int T;
	cin >> T;
	
	//cases
	for (int k=1; k<=T; k++)
	{	
		int crosses = 0;
		
		vector<int> straight;
		vector<pair<int, int> > slant;
		vector<pair<int, int> > slant2;		
		int N;
		cin >> N;
		// read in wires
		for (int n=0; n<N; n++)
		{
			int A, B;
			cin >> A;
			cin >> B;
//			cout << A << ", " << B << endl;
			if (A==B)
				straight.push_back(A);
			else
			{
				pair <int, int> range;
				pair <int, int> range2;
				
				range2.first = A;
				range2.second = B;
				
				if (A < B)
				{
					range.first = A;
					range.second = B;
				} else
				{
					range.first = B;
					range.second = A;
				}
				
				slant.push_back(range);
				slant2.push_back(range2);
			}
		}
		
		// check straight crossings
		for (int i=0; i<straight.size(); i++)
		{
			for (int j=0; j<slant.size(); j++)
			{
				//cout << slant[j].first << ", " << straight[i] << ", " << slant[j].second << endl;
				if ( slant[j].first < straight[i] && straight[i] < slant[j].second )
					crosses++;
			}
		}
		
		//check slant crossings;
		vector<pair<int, int> > seen;
		for (int i=0; i<slant2.size(); i++)
			for (int j=0; j<slant2.size(); j++)
			{
				if (i==j)
					continue;
				
				bool skip = false;
				for (int k=0; k<seen.size();k++)
				{
					if (i==seen[k].first && j==seen[k].second || j==seen[k].first && i==seen[k].second)
					{
						skip = true;
					}
				}
				
				if (skip)
					continue;
				
				int da = slant2[i].second - slant2[i].first;
				int db = slant2[j].second - slant2[j].first;
				
				float x = (float)(slant2[j].first - slant2[i].first)/(float)(da-db);
				if (x > 0 && x < 1)
				{
					pair<int, int> rec;
					rec.first = i;
					rec.second = j;
					seen.push_back(rec);
					crosses++;
					//cout << "slant" << endl;
				}
			}


			cout << "Case #" << k << ": " << crosses << endl;
	}
	
	return 0;
}
