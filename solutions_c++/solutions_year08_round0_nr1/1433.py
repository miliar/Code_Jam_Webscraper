#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <math.h>
#include <cstdlib>
#include <ctime>

using namespace std;

int DP[1000][100];

int main()
{
    fstream in,out;
    in.open("largeinputA.txt",ios::in);
    out.open("largeoutputA.txt",ios::out);
    
    /*problem specific code starts here*/
    
    int N;
    in>>N;
    
    for(int i=0;i<N;i++)
    {
		int S, Q, res=0, min;
		char temp[1000];
		vector<string> engines, queries;
		
		in>>S;
		in.getline(temp,120,'\n');
		for(int j=0;j<S;j++)
		{
			in.getline(temp,120,'\n');
			engines.push_back(temp);
		}
		
		in>>Q;
		in.getline(temp,120,'\n');
		for(int j=0;j<Q;j++)
		{
			in.getline(temp,120,'\n');
			queries.push_back(temp);
		}
		
		if(queries.size() != 0)
		{	
			for(int k=0;k<S;k++)
				if(engines[k] == queries[0])
					DP[0][k] = -1;
				else
					DP[0][k] = 0;
			
			
			for(int j=1;j<Q;j++)
			{
				for(int k=0;k<S;k++)
					if(engines[k] == queries[j])
						DP[j][k] = -1;
					else if(DP[j-1][k] != -1)
						DP[j][k] = DP[j-1][k];
					else
					{
						min = 100001;
						for(int m=0;m<S;m++)
						{
							if(m != k)
							{
								if(DP[j-1][m] != -1)
								//if(engines[m] == queries[j])
									if(min > DP[j-1][m]+1)
										min = DP[j-1][m]+1;
							}
							//else
							//	if(DP[j-1][m] != -1)
							//		if(min > DP[j-1][m])
							//			min = DP[j-1][m];
						}
										
						if(min == 100001)
							DP[j][k] = -1;
						else
							DP[j][k] = min;
					}
			}
			
			min = 100001;	
			for(int k=0;k<S;k++)
				if(DP[Q-1][k] != -1 && DP[Q-1][k]<min)
					min = DP[Q-1][k];
			
			res = min;
		}
		
		out<<"Case #"<<i+1<<": "<<res<<endl; 
	}
    
    /*problem specific code ends here*/
    
    in.close();
    out.close();
    
    return 0;
}
