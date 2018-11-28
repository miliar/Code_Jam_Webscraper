#include "iostream"
#include "cstdio"
#include "vector"
#include "string"
using namespace std;
struct combin
{
	char c1,c2;
	char cto;
};
struct oppose
{
	char left;
	char right;
	int nStartFlag;
};
int main()
{
	int T;
	int C,D,N;
	int i,j;
	char strIn[100],strOut[100];
	combin coList[40];
	oppose opList[60];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{
		memset(&strIn,0,sizeof(strIn));
		memset(coList,0,sizeof(coList));
		memset(opList,0,sizeof(opList));
		cin>>C;
		for(i = 0; i < C; i++)
		{
			cin>>coList[i].c1>>coList[i].c2>>coList[i].cto;
		}
		cin>>D;
		for(i = 0; i < D; i++)
		{
			cin>>opList[i].left>>opList[i].right;
			opList[D+i].left = opList[i].right;
			opList[D+i].right = opList[i].left;
		}
		cin>>N;
		for(i = 0; i < N; i++)
			cin>>strIn[i];

		for(i = 0; i < N; i++)
		{
			//检查组和替换字母
			if(i > 0)
			{
				for(j = 0; j < C; j++)
				{
					if( (coList[j].c1 == strIn[i] && coList[j].c2 == strIn[i-1])
						||(coList[j].c2 == strIn[i] && coList[j].c1 == strIn[i-1]) )
					{
						for(int k = 0; k < 2*D; k++)
						{
							if(strIn[i-1] == opList[k].left && opList[k].nStartFlag > 0)
								opList[k].nStartFlag--;
						}
						strIn[i] = 0;
						strIn[i-1] = coList[j].cto;
					}
						
				}
			}

			//检查消去字母
			for(j = 0; j < 2*D; j++)
			{
				if(opList[j].nStartFlag != 0 && opList[j].right == strIn[i])
				{
					for(int k = 0; k <= i; k++)
						strIn[k] = 0;
					for(int k = 0; k < 2*D; k++)
						opList[k].nStartFlag = 0;	
					
				}
			}
			for(j = 0; j < 2*D; j++)
			{
				if(opList[j].left == strIn[i])
				{
					opList[j].nStartFlag++;
				}
			}
		}
		
		int outNum = 0;
		for(i = 0; i < N; i++)
		{
			if(strIn[i] != 0)
				strOut[outNum++] = strIn[i];
		}		
		cout<<"Case #"<<caseID<<": [";
		for(i = 0; i < outNum - 1; i++)
			cout<<strOut[i]<<", ";
		if(outNum > 0)
			cout<<strOut[outNum - 1]<<"]";
		else
			cout<<"]";

		if(caseID != T)
			cout<<endl;
	}
	return 0;
}