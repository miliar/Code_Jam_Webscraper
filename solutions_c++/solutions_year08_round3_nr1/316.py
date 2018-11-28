#include <cstdlib>
#include <iostream>
#include<vector>
#include<algorithm>
#include<stack>


using namespace std;

int main(int argc, char *argv[])
{
	int nCases;
	cin>>nCases;

	int count = 0;
	while(count < nCases)
	{
		count++;
		int possible = 1;
		long long int maxl,nkey,nLetters;
		cin>>maxl>>nkey>>nLetters;

		vector<long long int> lVec;
		lVec.clear();
		
		for(long long int i=0;i<nLetters;i++)
		{
			long long int L;
			cin>>L;
			lVec.push_back(L);
		}	
	
		sort(lVec.begin(),lVec.end());
		reverse(lVec.begin(),lVec.end());
	
		//for (int i=0;i<(int)lVec.size();i++)
//			cout<<lVec[i]<<" ";
//		cout<<endl;

		
		long long int c = 1;
		long long int Res = 0;
		
		for(long long int i=0;i<nLetters;)
		{
			//cout<<c<<" "<<maxl<<" "<<lVec[i]<<" "<<endl;
			if(c > maxl)
				possible = 0;
			
			for(long long int j=0;j<nkey;j++)
			{
				Res += c*lVec[i];
				i++;	
				if(i >= nLetters)
					break;
			}
//			cout<<Res<<endl;
			c++;
			
		}
		if(possible)
			cout<<"Case #"<<count<<": "<<Res<<endl;
		else
			cout<<"Case #"<<count<<": "<<"Impossible"<<endl;
	}    

    return EXIT_SUCCESS;
}
