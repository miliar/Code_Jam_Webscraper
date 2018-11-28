#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <algorithm>

using namespace std;

int main()
{
    freopen("C-small-attempt0.in","r",stdin);
	freopen("outputtttCCCC.txt","w",stdout);
    
    int T;
    cin>>T;
    int cas=1;
    while (T--)
    {
		int N,L,H;
		cin>>N>>L>>H;
		vector<int> v(N);
		for (int i=0; i<N; i++)
			cin>>v[i];
			
		int result = -1;
		
		for (int i=L; i<=H; i++)
		{
			int count = 0;
			for (int j=0; j<N; j++)
			{
				if (i%v[j] == 0 || v[j]%i == 0)
					count++;
			}
			if (count == N)
			{
				result = i;
				break;
			}
				
		}
		
		if (result == -1)
		 cout<<"Case #"<<cas<<": NO"<<endl;
		else
		 cout<<"Case #"<<cas<<": "<<result<<endl;
		cas++;
		
	}
	return 0;
}
