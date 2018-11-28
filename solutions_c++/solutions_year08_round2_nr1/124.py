#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <cmath> 
#include <queue>
#include <fstream>
#include <map>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int testCases; string temporary; getline(in,temporary); stringstream sinple(temporary); sinple>>testCases;
	for(int tst=0; tst<testCases; tst++)
	{
		long long n, A, B, C, D, x0, y0, M;
		in >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
		vector <long long> blank(3,0); vector<vector<long long> > mod(3,blank);
		// vector <pair<long long, long long> > tri;
		long long X = x0; long long Y = y0;
		mod[X%3][Y%3]++;
		// tri.push_back(make_pair(X,Y));
		for(int i=1; i<n; i++)
		{
		
			X = (A*X+B) % M;
			Y = (C*Y+D) % M;
			mod[X%3][Y%3]++;
			//tri.push_back(make_pair(X,Y));
		}
		long long retSame = 0; long long retDif = 0;
		vector <pair<int,int> > m;
		for(int i=0; i<3; i++) { for(int j=0; j<3; j++) { m.push_back(make_pair(i,j)); } }
		
		for(int i=0; i<m.size(); i++) { retSame += (long long)(mod[m[i].first][m[i].second]*(mod[m[i].first][m[i].second]-1)*(mod[m[i].first][m[i].second]-2))/6; }
		
		
		for(int i=0; i<m.size(); i++)
		{
			for(int j=i+1; j<m.size(); j++)
			{
				for(int k=j+1; k<m.size(); k++)
				{
					if((m[i].first+m[j].first+m[k].first)%3==0&&(m[i].second+m[j].second+m[k].second)%3==0)
					{
						retDif += (long long)mod[m[i].first][m[i].second]*mod[m[j].first][m[j].second]*mod[m[k].first][m[k].second];
					}
				}
				
			}
		}
		
		
		
		
		long long ret = retSame+retDif;
	
	
	
		
	
	out << "Case #" << tst+1 << ": " << ret << endl; //complete here
	}
	
	return -1;
}
