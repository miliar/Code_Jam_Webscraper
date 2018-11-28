#include <iostream>
#include <vector>
#include <algorithm>

#include<cstdio>
#include<cstring>
#include<cmath>
int findans(int p,int q, int *qs, int i,int *selarray);
int answer;
using namespace std;

int main()
{int tempans;
	int nooftest,testcount;
	cin>>nooftest;

	for(testcount=1;testcount<=nooftest;testcount++)
	{
		int p,q;
		cin>>p>>q;
		answer=0;
		vector<int> qs;
		int t;
int i,j;
		for( i=0;i<q;i++)
		{cin>>t;qs.push_back(t);}

		int parray[102];
		sort(qs.begin(),qs.end());

		{
			parray[0]=0;
			for(i=1;i<=p;i++)
				parray[i]=1;
			parray[i]=0;
tempans=0;
			for(i=0;i<q;i++)
			{
				
				parray[qs[i]]=0;
				for( j=qs[i]-1;parray[j]!=0;j--)
					tempans++;
				for(j=qs[i]+1;parray[j]!=0;j++)
					tempans++;
			


			}
	answer=tempans;



		}
		while(next_permutation(qs.begin(),qs.end()))
		{
			parray[0]=0;
			for(i=1;i<=p;i++)
				parray[i]=1;
			parray[i]=0;
 tempans=0;
			for(i=0;i<q;i++)
			{
				
				parray[qs[i]]=0;
				for( j=qs[i]-1;parray[j]!=0;j--)
					tempans++;
				for(j=qs[i]+1;parray[j]!=0;j++)
					tempans++;
			


			}

				if(tempans<answer)
					answer=tempans;

		}




		cout<<"Case #"<<testcount<<": "<<answer<<endl;



	}
	return 0;
}


