#include <iostream>
#include <cstdio>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

struct scores{
	int a;
	int b;
	int c;
	int mod;
	int total;
};

int main()
{

	int cases;
	cin >> cases;
	cin >> ws;

	for(int i=0; i<cases; ++i)
	{
		int N;
		cin >> N;

		int S;
		cin >> S;

		int p;
		cin >> p;

		//int totals[N];
		int result = 0;
		vector<scores> scorelist;
		for(int j=0; j<N; ++j)
		{
			//cin >> totals[j];
			int score;
			cin >> score;

			int a = 0;
			scores s;
			if(score  > 2)
			{
				a = score/3;
				s.a = a;
				s.b = a;
				s.c = a;
				s.mod = score%3;
			}else if(score == 2){
				s.a = 1;
				s.b = 1;
				s.c = 0;
				s.mod = 0;
			}else if(score == 1){
				s.a = 1;
				s.b = 0;
				s.c = 0;
				s.mod = 0;
			}else if(score == 0){
				s.a = 0;
				s.b = 0;
				s.c = 0;
				s.mod = 0;
			}
				
			
			s.total = score;
			
			scorelist.push_back(s);
		}

		for(int j=0; j<N; ++j)
		{

			scores s = scorelist.at(j);
			//cout << s.total << " " << s.a << " " << s.b << " " << s.c << endl;
			if( s.a < p && s.a > 0)
			{
				if(s.mod == 1 ) s.a += 1;
				else if(s.mod == 2 && S > 0 && s.a+2 >= p){
					s.a += 2;
					S--;
				}
				else if(s.mod == 2 && S == 0){
					s.a += 1;
				}
				else if(s.mod == 0 && S > 0 && s.a+1 >= p ){
					s.a += 1;
					S--;
				}
			} 

			

			if(s.a >= p){
				++result;
			}

			//cout << s.a << endl;

		}
		//cout  << "S " << S << endl;
		cout << "Case #" << i+1 << ": " << result << endl;


	}

}