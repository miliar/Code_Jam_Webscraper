#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define db(x) cout<< #x << " : " <<x <<endl;
#define pb push_back
#define mp make_pair

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int,int> ii;

void PV(vector<int> v)
{
	cout << "\n";
	for(int i=0; i<v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}
int mod(int x)
{
	return max(x,-x);
}

int main()
{
	
	int t;
	
	cin >> t;
	
	for(int z=1; z<=t; z++)
	{
		int N;
		cin >> N;
		
		int currO, currB;
		
		currO = currB = 1;
		
		char R;
		int P;
		int secs = 0;
		int lastO = 0, lastB = 0;
		int distToMove, idleTime;
		
		while(N--)
		{
			cin >> R >> P;
			
			if(R == 'B')
			{
				distToMove = mod(currB-P);
				idleTime = (secs - lastB);
				
				if(idleTime > distToMove)
					distToMove = 0;
				else
					distToMove -= idleTime;
					
				secs += (distToMove + 1);
				
				lastB = secs;
				currB = P;
			}
			else
			{
				distToMove = mod(currO-P);
				idleTime = (secs - lastO);
				
				if(idleTime > distToMove)
					distToMove = 0;
				else
					distToMove -= idleTime;
					
				secs += (distToMove + 1);
				
				lastO = secs;
				currO = P;
			}
			
		}
		
		
		cout << "Case #" << z << ": " << secs << endl;
		
	}
	

    return 0;
}
