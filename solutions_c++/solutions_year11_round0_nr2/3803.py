#include "iostream"
#include "cstdio"
#include "vector"
using namespace std;
#define FOR(i,n) for(i = 0; i < n; i++)

char Element[100];
char Combin[36][3];
char Opp[28][2];


//����Ƿ��ǿ��Ժϲ�����ĸ
void checkCob(char target, char& cobin2, char& cobin3, int CombinNum)
{
	for(int k=0;k<CombinNum;k++)
	{
		if( target == Combin[k][0] )
		{
			cobin2 = Combin[k][1];
			cobin3 = Combin[k][2];
			break;
		}	
		else if( target == Combin[k][1] )
		{
			cobin2 = Combin[k][0];
			cobin3 = Combin[k][2];
			break;
		}
	}
}
	
int main()
{
	
	int CaseNum,CombinNum,OppNum,ElementsNum;
	int i,j,k,caseID,EleID,CobID,OppID,OppID2;
	char strtmp[100];
	
	char Cob1=0,Cob2=0,Cob3=0;
	char Opp1=0,Opp2=0,Opp3=0;
	
	
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	
	cin>>CaseNum;

	for(caseID=0;caseID<CaseNum;caseID++)
	{
		cin>>CombinNum;
		if(CombinNum!=0)
		{			
			for(i=0;i<CombinNum;i++)
				cin>>Combin[i];	
		}
		cin>>OppNum;
		if(OppNum!=0)
		{
			for(i=0;i<OppNum;i++)
				cin>>Opp[i];	
		}
		cin>>ElementsNum;
		cin>>Element;
		if(0 == CombinNum && 0 == OppNum)
		{
			cout<<"Case #"<<caseID+1<<": [";
			cout<<Element[0];
			for(i=1;i<ElementsNum;i++)
				cout<<", "<<Element[i];
			cout<<"]";
			cout<<endl;
			continue;
		}

		for(EleID=0;EleID<ElementsNum-1;EleID++)
		{
			//����Ƿ��ǿ��Ժϲ�����ĸ
			checkCob(Element[EleID],Cob2,Cob3,CombinNum);
			if(Cob2!=0)//���Ժϲ�����ĸ
			{
				if(Element[EleID+1]==Cob2)//�����ŵ��������Ժϲ�
				{
					Element[EleID]=	Cob3;
					for(j=EleID+1;j<ElementsNum-1;j++)
						Element[j]=Element[j+1];
					ElementsNum = ElementsNum-1;	
				}
			}
			Cob2=0;


			//�Ƿ������
			for(OppID=0;OppID<OppNum;OppID++)
			{
				if( Element[EleID] == Opp[OppID][0] )
				{
					Opp2 = Opp[OppID][1];
					break;
				}	
				else if( Element[EleID] == Opp[OppID][1] )
				{
					Opp2 = Opp[OppID][0];
					break;
				}				
			}
			if(Opp2!=0)
			{
				//��OppID2��������һ��
				for(OppID2=EleID+1;OppID2<ElementsNum;OppID2++)
				{
					if(Element[OppID2]==Opp2)//�ҵ���������
					{
						
						checkCob(Opp2,Cob2,Cob3,CombinNum);
						if(Cob2!=0 && Element[OppID2-1]==Cob2)//���Ժϲ�����ĸ ���� �����ŵ��������Ժϲ�
						{
							Element[OppID2-1] = Cob3;
							for(k=OppID2;k<ElementsNum-1;k++)
								Element[k]=Element[k+1];
							ElementsNum = ElementsNum-1;
							
						}
						else
						{
							for(k=EleID;k<ElementsNum-(OppID2-EleID+1);k++)
								Element[k]=Element[k+(OppID2-EleID+1)];
							ElementsNum = ElementsNum-(OppID2-EleID+1);
								EleID--;
						}
						break;//�ҵ������ұ� �ض��˳�
					}
				}
				
			}
		Opp2=0;
		Cob2=0;
		}
	

		
		
	cout<<"Case #"<<caseID+1<<": [";
	if(ElementsNum!=0)
	{
		cout<<Element[0];
	}
	for(i=1;i<ElementsNum;i++)
	{
		cout<<", "<<Element[i];
	}
	cout<<"]";
	cout<<endl;





	}
	return 0;
}