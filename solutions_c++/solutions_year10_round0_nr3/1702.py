#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("output.txt");
ifstream fin("input.txt");


long long sizes[1000];

long long tots[1000];
int times[1000];

int main(void)
{

	int ttt;
	cin >> ttt;
	int ct = 0;
	
	
	
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		
		int rides;
		int people;
		int n;
		cin >> rides >> people >> n;
		int i,j,k;
		for(i=0; i<n; i++)
		{
			cin >> sizes[i];
			tots[i]=times[i]=-1;
		}
		int tm = 0;
		long long ans = 0;
		int currat = 0;
		while(tm < rides)
		{
			if(times[currat]>=0 && ((rides-tm)%(tm-times[currat])==0))
			{
				
				int diff = tm-times[currat];
				cout << "PERIODIC AT " << currat << " with period " << diff << endl;
				long long diffval = ans-tots[currat];
				long long mult = (rides-tm)/(tm-times[currat]);
				ans += diffval*mult;
				tm=rides;
				break;
			}
			tots[currat]=ans;
			times[currat]=tm;
			int currtot = 0;
			int currstart = currat;
			currtot = sizes[currat];
			currat++;
			currat%=n;
			while( currtot + sizes[currat]<=people && currat!=currstart)
			{
				currtot+=sizes[currat];
				currat++;
				currat%=n;
			}
			ans+=currtot;
			tm++;
		}
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}

	
	return 0;
}

