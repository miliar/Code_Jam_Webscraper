#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;
const int N = 110;
int main()	{
	int rounds, p, googs, surps, scores[N], above_surp, above_possible, tot;
	cin >> rounds;
	for(int i = 0; i < rounds; i++)	{
		cin >> googs >> surps >> p;
		tot = 0;
		above_surp = ((3*p) - 2);
		above_possible = ((3*p) - 4);
		for(int j = 0; j < googs; j++)	cin >> scores[j];
		for(int j = 0; j < googs; j++)	{
			if(scores[j] && scores[j] >= above_surp)	tot++;
			else if(scores[j] && scores[j] >= above_possible && surps > 0)	{
				surps--;	tot++;
			}
			else if(scores[j] == 0 && above_surp <= 0)	tot++;
		}
		cout <<"Case #"<<i+1 <<": " << tot <<'\n';
	}
	return 0;
}
