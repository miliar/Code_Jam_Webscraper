#include <iostream>
#include <vector>
#include <string>
#include <list>

using namespace std;

int main(int argc, char** args)
{
	unsigned int T;
	cin >> T;
	
	for (unsigned int t = 0; t < T; t++)
	{		
		string	temp;
		
		unsigned int C;
		cin >> C;
		
		vector<string>	combineList;
		combineList.reserve(C);
		for (unsigned int c = 0; c < C; c++)
		{
			cin >> temp;
			combineList.push_back(temp);
		}
		
		unsigned int D;
		cin >> D;
		
		vector<string>	opposeList;
		opposeList.reserve(D);
		for (unsigned int d = 0; d < D; d++)
		{
			cin >> temp;
			opposeList.push_back(temp);
		}
		
		unsigned int N;
		cin >> N;
		
		string invokations;
		cin >> invokations;
		
		list<char>	elementList;
		for (unsigned int i = 0; i < N; i++)
		{
			char last = elementList.empty() ? '-' : elementList.back();
			char invk = invokations[i];			
			elementList.push_back(invk);
			
			bool	done = false;
			for (unsigned int c = 0; c < combineList.size(); c++)
			{	
				string cs = combineList[c];
				if (((cs[0] == last) && (cs[1] == invk)) || ((cs[1] == last) && (cs[0] == invk)))
				{
					elementList.pop_back();
					elementList.pop_back();	
					elementList.push_back(cs[2]);
					done = true;
					break;
				}
			}
			
			if (done) continue;
			
			for (unsigned int d = 0; d < opposeList.size(); d++)
			{	
				string	oc = opposeList[d];
				int		check = (oc[0] == invk) ? 1 : ( (oc[1] == invk) ? 0 : -1);
				if (check == -1) continue;
				
				for (list<char>::iterator it = elementList.begin(); it != elementList.end(); it++)
					if (*it == oc[check])
					{
						check = -2;
						elementList.clear();
						break;
					}
					
				if (check == -2) break;
			}	
		}
		
		cout << "Case #" << (t+1) << ": [";
		if (!elementList.empty())
		{
			list<char>::iterator iter = elementList.begin();
			cout << *iter;
		
			for (iter++; iter != elementList.end(); iter++)
				cout << ", " << *iter;
		}
		cout << "]" << endl;
	}
}

