#include "iostream"
#include "cstdio"
#include "vector"
using namespace std;
#define FOR(i,n) for(i = 0; i < n; i++)

char Element[100];
char Combin[36][3];
char Opp[28][2];
int CaseNum,CombinNum,OppNum,ElementsNum,ComThisCNum,OppThisCNum,comflag=0,Oppflag=0,candyID=0;
char Cob2[36],Cob3[36];
char Opp2[28];

int candyNum;
int candy[1000];


//¶ÁÈëÊý¾Ý
void readData(void)
{
	int i;
	cin>>candyNum;
	if(candyNum!=0)
	{			
		for(i=0;i<candyNum;i++)
			cin>>candy[i];	
	}
}

	
int main()
{
	
	
	int i,j,k,caseID,EleID,CobID,OppID,OppID2,tempID1,tempID;
	int temp,sum,temp2,temp3=1000000;


	freopen("C-large.in","r",stdin);
	freopen("C-small-attempt4.out","w",stdout);
	
	cin>>CaseNum;

	for(caseID=0;caseID<CaseNum;caseID++)
	{
		
		readData();
		temp3=1000000;
		temp=candy[0]^candy[1];
		sum=candy[0]+candy[1];
		if(candy[0]<=temp3)
			temp3=candy[0];
		if(candy[1]<=temp3)
			temp3=candy[1];

		for(candyID=2;candyID<candyNum;candyID++)
		{
			if(candy[candyID]<=temp3)
				temp3=candy[candyID];
			sum+=candy[candyID];
			temp=candy[candyID]^temp;

		}

		
		
		
		if(temp!=0)
		{
			cout<<"Case #"<<caseID+1<<": ";	
			cout<<"NO";
			cout<<endl;
		}
		else
		{
			temp2=sum-temp3;
			cout<<"Case #"<<caseID+1<<": ";	
			cout<<temp2;
			cout<<endl;
		}		
	}
	return 0;
}