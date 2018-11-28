#include <iostream>
#include<string>
#include<iostream> 
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<set>
#include<sstream>
#include<cstring>
#include<string>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;

int main()
{
	freopen("d://A-large.in", "r", stdin);
	freopen("d://A-large.out", "w", stdout);
	pair<string, int> each;
	vector< pair<string, int> > list;
    vector<int> OList, BList;
    
    int T, t, N, n, P;
    int i, j, dif;
    string R;
    int posO, posB;
    string now;
    int time, pastTime;
    cin >> T;
    
    for(t=1;t<=T;t++)
    {
		cout << "Case #" << t <<": ";// << endl;    
	    cin >> N;
	    time = pastTime = 0;

		list.clear();
		OList.clear();
		BList.clear();

	    for(n=1;n<=N;n++)
	    {
			cin >> R >> P;
			each.first = R;
			each.second = P;
			if(R == "O")
				OList.push_back(P);
			if(R == "B")
				BList.push_back(P);
			list.push_back(each);
		}
	   	
		posO = posB = 1;
		i = j = 0;

		for(n=0;n<list.size();n++)
		{
			if(list[n].first == "O")
			{
				i++;
				pastTime = time;
				time+=(abs(list[n].second - posO)+1);
				if(j<BList.size())
				{
					if(BList[j] < posB)
					{
						dif = time-pastTime;
						posB -= dif;
						if(posB < BList[j])
							posB = BList[j];
					}
					else
					{
						dif = time-pastTime;
						posB += dif;
						if(posB > BList[j])
							posB = BList[j];
					}
				}
				posO = list[n].second;
			}
			else
			{
				j++;
				pastTime = time;
				time+=(abs(list[n].second - posB)+1);
				if(i<OList.size())
				{
					if(OList[i] < posO)
					{
						dif = time-pastTime;
						posO -= dif;
						if(OList[i] > posO)
							posO = OList[i];
					}
					else
					{
						dif = time-pastTime;
						posO += dif;
						if(posO >OList[i])
							posO = OList[i];
					}
				}
				posB = list[n].second;
			}

			//cout << list[n].first << " " << list[n].second << "\tposO:" << posO << "\t: posB:" << posB << endl;
		}

		
		cout << time << endl;
		//cout << "------------------------" << endl;
	}
    return 0;
}
