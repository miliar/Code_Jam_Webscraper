#include <list>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
struct Node
{
	int m_nStartTime;
	int m_nEndTime;
	int m_nType;
};
bool operator<(const Node & n1,const Node & n2)
{
	return n1.m_nStartTime < n2.m_nStartTime;

}

typedef vector<Node> NodeArray;
typedef list<int> IntArray;
void TrainTimetable(int &a,int &b)
{
	a = 0;
	b = 0;
	NodeArray NAArray;
	//NodeArray NBArray;

	IntArray NAReady;
	IntArray NBReady;

	int t;
	scanf("%d\n",&t);

	int na,nb;
	scanf("%d %d\n",&na,&nb);
	for(int i = 0;i<na + nb;i++)
	{
		int stm,sts,etm,ets;
		scanf("%d:%d %d:%d",&stm,&sts,&etm,&ets);
		Node node;
		node.m_nStartTime = stm*60 + sts;
		node.m_nEndTime = etm*60 + ets; 

		if(i<na)
		{
			node.m_nType = 0;


		}
		else
		{
			node.m_nType = 1;
		}
		NAArray.push_back(node);

	}

	std::sort(NAArray.begin(),NAArray.end());

	for(int i = 0;i!=NAArray.size();i++)
	{
		if(NAArray[i].m_nType == 0)
		{
			bool bNeed = true;

			for(IntArray::iterator iter = NAReady.begin();iter!= NAReady.end();iter++)
			{
				if(*iter <= NAArray[i].m_nStartTime)
				{

					bNeed = false;
					NAReady.erase(iter);
					break;

				}
			}
			if(bNeed){ a++;}
			NBReady.push_back(NAArray[i].m_nEndTime + t);

		}
		



		else
		{
			bool bNeed = true;
			for(IntArray::iterator iter = NBReady.begin();iter!= NBReady.end();iter++)
			{
				if(*iter <= NAArray[i].m_nStartTime)
				{

					bNeed = false;
					NBReady.erase(iter);
					break;

				}
			}


			if(bNeed){ b++;}
			NAReady.push_back(NAArray[i].m_nEndTime + t);

		}


	}

}
int _tmain(int argc, _TCHAR* argv[])
{
	int nCaseNumber = 0;
	freopen("f:\\input2.txt","r",stdin);
	scanf("%d",&nCaseNumber);
	FILE *file = fopen("f:\\Output2.txt","w+");

	for(int i = 0;i<nCaseNumber;i++)
	{
		int a,b;
		TrainTimetable(a,b);
		fprintf(file,"Case #%d: %d %d\n",i+1,a,b);
		//printf("Case #%d: %d\n",i+1,SaveUniverse());
	}


	fclose(file);
	return 0;
}