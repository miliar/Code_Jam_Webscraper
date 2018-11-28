#include "iostream"
#include "cstdio"
#include "vector"
using namespace std;
#define FOR(i,n) for(i = 0; i < n; i++)
struct step{
int robort; //0-O,1-B
int button;
};
struct robertStep{
int step;
int button;
};
int main()
{
	int T,N;
	int i,j;
	char ctmp;
	int ntmp;
	int oPos,bPos,nStep;
	int moveStep;
	step s[100];
	vector <robertStep> vo,vb;
	robertStep tmpStep,oStep,bStep;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin>>T;
	for(int caseID = 1; caseID <= T; caseID++)
	{
		oPos = 1;
		bPos = 1;
		nStep = 0;
		memset(s,0,sizeof(s));
		cin>>N;
		for(i = 0; i < N; i++)
		{
			cin>>ctmp>>ntmp;
			s[i].button = ntmp;
			if(ctmp == 'O')
			{
				s[i].robort = 0;
				tmpStep.step = i;
				tmpStep.button = ntmp;
				vo.insert(vo.begin(),tmpStep);
//				vo.push_back(tmpStep);
			}
			else
			{
				s[i].button = 1;
				tmpStep.step = i;
				tmpStep.button = ntmp;
				vb.insert(vb.begin(),tmpStep);
//				vb.push_back(tmpStep);
			}
		}

		for(i = 0; i < N; i++)
		{
			if(!vo.empty())
				oStep =  vo.back();
			if(!vb.empty())
				bStep = vb.back();
			//黄色机器人
			if(!vo.empty() && (vb.empty() || oStep.step < bStep.step))
			{
				vo.pop_back();
				moveStep = abs(oStep.button - oPos) + 1;
				nStep += moveStep;
				oPos = oStep.button;
				if(abs(bStep.button - bPos) <= moveStep)
				{
					bPos = bStep.button;
				}
				else if(bStep.button - bPos > 0)
					bPos += moveStep;
				else
					bPos -= moveStep;
			}
			//蓝色机器人
			else
			{
				vb.pop_back();
				moveStep = abs(bStep.button - bPos) + 1;
				nStep += moveStep;
				bPos = bStep.button;
				if(abs(oStep.button - oPos) <= moveStep)
				{
					oPos = oStep.button;
				}
				else if(oStep.button - oPos > 0)
					oPos += moveStep;
				else
					oPos -= moveStep;
			}
			
		}
		
		cout<<"Case #"<<caseID<<": "<<nStep;
		if(caseID != T)
			cout<<endl;
	}
	return 0;
}