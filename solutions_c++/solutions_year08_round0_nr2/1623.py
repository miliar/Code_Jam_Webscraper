#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

using namespace std;

int gettime(string a)
{
	return 600*(a[0]-'0') + 60*(a[1]-'0') + 10*(a[3]-'0') + a[4]-'0';
}

bool runs(int NA, int NB, vector <vector <int> > trains)
{
	for(int i=0; i<trains.size(); i++)
	{
		
		if(trains[i][1]==0) NA++;
		if(trains[i][1]==1) NB++;
		if(trains[i][1]==2) { if(NA<=0){ return false; } NA--; }
		if(trains[i][1]==3) { if(NB<=0){ return false; } NB--; }
	}
	return true;
}
// 0 is arriv a, 1 is arriv b, 2 is leav a, 3 is leav b

int main(void)
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int N; in >> N;
		for(int tst=0; tst<N; tst++)
		{
			vector <vector <int> > trains;
			int A = 0; int B = 0;
			int T; in >> T;
			int NA, NB; in >> NA >> NB;
			
			for(int i=0; i<NA; i++)
			{
				string a, b;
				in >> a >> b;

				int atime = gettime(a);
				int btime = T+gettime(b);

				vector <int> aa; aa.push_back(atime); aa.push_back(2); trains.push_back(aa);  
				vector <int> bb; bb.push_back(btime); bb.push_back(1); trains.push_back(bb);
			}


			for(int i=0; i<NB; i++)
			{
				
				string a, b;
				in >> a >> b;
				int atime = gettime(a);
				int btime = T+gettime(b);
				vector <int> aa; aa.push_back(atime); aa.push_back(3); trains.push_back(aa);  
				vector <int> bb; bb.push_back(btime); bb.push_back(0); trains.push_back(bb);
			}
			
			for(int i=0; i<trains.size(); i++)
			{
				for(int j=0; j<trains.size(); j++)
				{
				if(trains[i][0]<trains[j][0]||(trains[i][0]==trains[j][0]&&trains[i][1]<trains[j][1]))
					{
					swap(trains[i],trains[j]);
					}
				}
			}
		

			int aMax = 0; int bMax = 0;
			int aBest = 10000; int bBest = 10000;
			bool done=false;
			/*for(int i = 0; i<201; i++)
			{
				if(done) break;
				for(int j=0; j<201; j++)
				{
					if(runs(i,j,trains))
					{
						out << "Case #" << tst+1 << ": " << i << " " << j << endl; done=true; break;
					}
				}

			}*/ NA = 0; NB = 0;
			for(int i=0; i<trains.size(); i++)
			{
				if(trains[i][1]==3) { NB++; bMax = max(bMax,NB); }
				if(trains[i][1]==2) { NA++; aMax = max(aMax,NA); }
				if(trains[i][1]==1) { NB--; }
				if(trains[i][1]==0) { NA--; }
			}

			// cout << "Case #" << tst+1 << ": " << aMax << " " << bMax << endl;
		
			
			 out << "Case #" << tst+1 << ": " << aMax << " " << bMax << endl;
		
		}
	
	
	return -1;
}

