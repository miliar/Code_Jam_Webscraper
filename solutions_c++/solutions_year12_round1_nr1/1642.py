//#include <stdio.h>
//#include "../ProcNetInclude.h"
//
//class CResponseNode:public CProcNode
//{
//	CResponseNode(const CResponseNode&);
//	CResponseNode& operator=(const CResponseNode&);
//public:
//	CResponseNode() { ; }
//	~CResponseNode() { ; }
//public:
//	virtual void OnReceiveMessage(LPCBYTE pData,DWORD dwLen)
//	{
//		printf("ReceiveMessage At CResponseNode:\n");
//		for(DWORD i = 0;i < dwLen;++i) printf("%02x ",pData[i]);
//		printf("\n");
//	}
//public:
//	BOOL Start(DWORD module)
//	{
//		BOOL bRet = CProcNode::Start(module);
//		printf("CResponseNode Init %s.\n",bRet?"Success":"Failed");
//		if(!bRet) return FALSE;
//		DWORD id =  CProcNode::GetID();
//		printf("CResponseNode ID = %u\n",id);
//		return TRUE;
//	}
//};
//
////////////////////////////////////////////////////////////////////////////
//
//int main()
//{
//	CResponseNode node;
//	if(node.Start(1))
//	{
//		while(1)
//		{
//			Sleep(3000);
//		}
//		node.Stop();
//	}
//	system("pause");
//	return 0;
//}

#include <stdio.h>
#include <vector>
using std::vector;

int main()
{
	freopen("c:\\A-small-attempt0.in","r",stdin);
	freopen("c:\\sample.out","w+",stdout);

	unsigned int nCases = 0;scanf("%d",&nCases);
	for(int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int a = 0,b = 0;scanf("%d%d",&a,&b);
		vector<float> correct_probs(a,0.0);
		for(unsigned int i = 0;i < a;++i) scanf("%f",&correct_probs[i]);
		// 左起第一个错误的位置的概览
		vector<double> probs(a+1,1.0);
		double product = 1.0;
		for(unsigned int i = 0;i < a;++i)
		{
			probs[i] = product*(1-correct_probs[i]);
			product *= correct_probs[i];
		}
		probs[a] = product;
		vector<double> accu_probs(a+1,0.0);
		accu_probs[0] = 0;
		for(int i = 1;i <= a;++i) accu_probs[i] = accu_probs[i-1]+probs[i-1];

		double min_expected = b + 2;					// give up
		for(unsigned int i = 0;i <= a;++i)				// backspace
		{
			// [0..a-i)		->		b - a + 2*i + 1
			// [a-i,a]		->		b - a + 2*i + 1 + b + 1
			double expected = b - a + 2*i + 1;
			expected += (b + 1)*accu_probs[a-i];
			
			//for(unsigned int k = 0;k <= a;++k)
			//{
			//	unsigned int count = b - a + 2*i + 1;
			//	if(i < a - k) count += b + 1;
			//	//printf("backspace = %u,count = %u\n",i,count);
			//	expected += count*probs[k];
			//}
			//printf("backspace = %u,prob = %.6f\n",i,expected);
			if(expected < min_expected) min_expected = expected;
		}
		printf("Case #%u: %.6f%\n",iCases,min_expected);
	}
	return 0;
}