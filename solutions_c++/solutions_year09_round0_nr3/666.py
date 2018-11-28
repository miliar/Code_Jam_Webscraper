#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

int testCases;

using namespace std;

int main(void)
{
	ifstream in("B-small.in");
	ofstream out("B-output.out");
	string line;
	
	getline(in,line);
	
	stringstream s(line);
	
	s >> testCases;
	
	
	string target = "welcome to code jam";
	
	for(int tst=0; tst<testCases; tst++) {
		
			
			getline(in,line);
			
			int n = line.length();
			
			vector<int> blank(target.length(),0);
			vector < vector<int> > dp(n,blank);
			
			for(int i=0; i<n; i++)
				{
				for(int j=0; j<target.length(); j++)
					{
					if(i==0) 
						{
						if(line[0] == target[0])
							{
							dp[0][0] = 1;
							}
						if(j>0)
							{
							dp[0][j] = 0;
							}
						
						}
					
					if(i>0)
						{
						dp[i][j] = dp[i-1][j];
						
						if(line[i] == target[j])
							{
							if(j==0) dp[i][j]++;
							if(j>0) dp[i][j] += dp[i-1][j-1];
							}
						
						dp[i][j] = dp[i][j] % 10000;
						}
					}	
				}
				
			stringstream s(""); string ret;
			s << dp[n-1][target.length()-1]; s >> ret;
			
			while(ret.size() < 4) {
			ret = "0" + ret;
			}
		
			out << "Case #" << tst+1 << ": " << ret << endl;;
			
	}


}