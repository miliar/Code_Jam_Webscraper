#include<iostream>
#include<vector>
using namespace std;

struct node{
	char ch;
	int pos;
};

node datain[101];

int main()
{
	int t;
	cin>>t;
	for(int i=1;i<=t;++i)
	{
		int res=0;
		int N;
		cin>>N;
		vector<int> BVec,OVec;
		for(int j=0;j<N;++j)
		{
			cin>>datain[j].ch>>datain[j].pos;
		}
		for(int j=0;j<N;++j)
		{
			if(datain[j].ch=='B')
			{
				BVec.push_back(datain[j].pos);
			}
			else
			{
				OVec.push_back(datain[j].pos);
			}
		}
		int BPos=1,BVecPos=0;
		int OPos=1,OVecPos=0;
		int posNow=0;
		while(posNow<N)
		{
			++res;
			if(datain[posNow].ch=='B')
			{
				if(BPos<BVec[BVecPos])
				{
					++BPos;
				}
				else if(BPos==BVec[BVecPos])
				{
					++posNow;
					++BVecPos;
				}
				else if(BPos>BVec[BVecPos])
				{
					--BPos;
				}

				if(OVecPos<OVec.size())
				{
					if(OPos<OVec[OVecPos])
					{
						++OPos;
					}
					else if(OPos==OVec[OVecPos])
					{
					}
					else if(OPos>OVec[OVecPos])
					{
						--OPos;
					}
				}
			}
			else
			{
				if(OPos<OVec[OVecPos])
				{
					++OPos;
				}
				else if(OPos==OVec[OVecPos])
				{
					++posNow;
					++OVecPos;
				}
				else if(OPos>OVec[OVecPos])
				{
					--OPos;
				}

				if(BVecPos<BVec.size())
				{
					if(BPos<BVec[BVecPos])
					{
						++BPos;
					}
					else if(BPos==BVec[BVecPos])
					{
					}
					else if(BPos>BVec[BVecPos])
					{
						--BPos;
					}
				}
			}
		}
		printf("Case #%d: %d\n",i,res);
	}
	return 0;
}