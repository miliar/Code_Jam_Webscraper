// Dancing With the Googlers.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;
int main()
{
	fstream in;
	in.open("input.txt");
	int cases;
	int googlers;
	int surprised;
	int p;
	vector<int> scores;
	int it = 0;
	in>>cases;
	while ( it != cases )
	{
		in>>googlers;
		in>>surprised;
		in>>p;
		int num = 0;
		for ( int i = 0; i<googlers; i++ )
		{
			int x;
			in>>x;
			scores.push_back(x);

			int result = -1;
			int first = p;
			//int s = surprised;
			bool flag = true;
			while ( (result != scores[i]) && (scores[i] >= p) )
			{
				vector <int> v;
				
				int rest2 = scores[i] - first;
				int sec_third,diff,diff1;
				if ( rest2 %2 == 0 )
				{
					sec_third = rest2/2;
					diff = first - sec_third;
					if ( diff < 2 && diff > -2 )
						result = first + sec_third + sec_third;
					else if ( diff <= -2 && first < 10 )
					{
						first += 1;
					}
					else if (diff == 2 && surprised > 0)
					{
						surprised -= 1;
						result = first + sec_third + sec_third;
					}
					else
					{
						flag = false;
						break;
					}
				}
				else 
				{
					sec_third = (rest2+1)/2;
					diff = first - sec_third;
					int n = sec_third -1;
					diff1 = first - n;
					if ( (diff < 2 && diff > -2)  && (diff1 < 2 && diff1 > -2))
						result = first + sec_third +sec_third -1;
					else if (((diff <= -2 ) ||( diff1 <= -2 )) && first < 10)
					{
						first += 1;
					}
					else if (((diff == 2 && diff1 <= 2)  ||( diff1 == 2 && diff <= 2) ) && surprised > 0)
					{
						surprised -= 1;
						result = first + sec_third + sec_third-1;
					}
					else
					{
						flag = false;
						break;
					}
				}
			}
			if ( flag == true && result >= p )
				num +=1;
		}
		scores.clear();
		fstream out;
		out.open("output.txt",ios::app);
		cout<<"Case #"<<it+1<<": "<<num<<endl;
		if ( it+1 == cases )
			out<<"Case #"<<it+1<<": "<<num;
		else
			out<<"Case #"<<it+1<<": "<<num<<endl;
		out.close();
		it += 1;
		
	}

	in.close();


	system("pause");
	return 0;
}

