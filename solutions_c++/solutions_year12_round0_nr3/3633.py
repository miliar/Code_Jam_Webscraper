#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
	int a,b,t,i,j,k;
	int count;
	string num, comp;
	stringstream ss;
	
	cin >> t;
	
	for(i=0; i<t; i++)
	{
		cin >> a;
		cin >> b;
		count = 0;
		for(j=a; j<b; j++)
		{
			ss.str( std::string() );
			ss.clear();

			ss << j;
			num = ss.str();
			for(k = 1; k<num.size(); k++)
			{
				if(num[k] == '0') continue;
				comp.clear();
				comp = num.substr(k, num.size()-k);
				comp += num.substr(0, k);
				if(atoi(comp.c_str()) > atoi(num.c_str()) && atoi(comp.c_str()) <= b)
					count++;
			}				
		}
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	
	return 0;
}	
