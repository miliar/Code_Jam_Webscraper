#include<iostream>
#include<algorithm>
using namespace std;

struct node{
	int data[3];
	bool used;
};

int main()
{
	int t[200];
	node NData[200];
	int T,N,S,P;
	cin>>T;
	int num=1;
	while(T--)
	{
		
		cin>>N>>S>>P;
		for(int i=0;i<N;i++)
		{
			cin>>t[i];
		}
		for(int i=0;i<N;i++)
		{
			NData[i].data[0]=t[i]/3;
			NData[i].data[1]=(t[i]-t[i]/3)/2;
			NData[i].data[2]=t[i]-NData[i].data[0]-NData[i].data[1];
			NData[i].used=false;
		}
		for(int i=0;i<N;i++)
		{
			if((NData[i].data[2]-NData[i].data[0]==1)&&(NData[i].data[1]-NData[i].data[0]==0))
			{
				NData[i].used=true;
			}
		}
		bool noChange=false;
		while(S>0&&!noChange)
		{
			int maxAAA=-1,maxPosAAA=-1,maxABB=-1,maxPosABB=-1;
			noChange=true;
			for(int i=0;i<N;i++)
			{
				if(NData[i].used==false)
				{
					noChange=false;
					if(NData[i].data[0]==NData[i].data[1])//AAA
					{
						if(NData[i].data[2]>maxAAA)
						{
							maxAAA=NData[i].data[2];
							maxPosAAA=i;
						}
					}
					else	//A(A+1)(A+1)
					{
						if(NData[i].data[2]>maxABB)
						{
							maxABB=NData[i].data[2];
							maxPosABB=i;
						}
					}
				}
			}
			//�ҵ���AAAģʽ������ѡ��A(A+1)(A+1)ģʽ������ѡ
			if(maxAAA>=P)//�Ѿ��������账��
			{
				NData[maxPosAAA].used=true;
				continue;
			}
			if(maxABB>=P)
			{
				NData[maxPosABB].used=true;
				continue;
			}
			if(noChange)
			{
				break;
			}
			//��û��ֱ�ӿ��Լ���Ķ���ʱ������Surprising�����ø���⼰��
			if(maxAAA+1>=maxABB+1)//AAAģʽ�ɱ�Ϊ(A-1)(A)(A+1):(A�������1),A(A+1)(A+1)�ɱ�ΪAA(A+2)
			{
				if(NData[maxPosAAA].data[0]>=1)
				{
					NData[maxPosAAA].data[0]-=1;
					NData[maxPosAAA].data[2]+=1;
					NData[maxPosAAA].used=true;
					S--;
				}
				else//��ֵ�޷�ת�������趨Ϊused
				{
					NData[maxPosAAA].used=true;
				}
			}
			else
			{
				NData[maxPosABB].data[1]-=1;
				NData[maxPosABB].data[2]+=1;
				NData[maxPosABB].used=true;
				S--;
			}
		}

		//ͳ�ƽ��
		int res=0;
		for(int i=0;i<N;i++)
		{
			if(NData[i].data[2]>=P)
				res++;
		}
		printf("Case #%d: %d\n",num++,res);
	}
	return 0;
}