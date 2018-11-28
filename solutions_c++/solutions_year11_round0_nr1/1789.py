#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	char P[110][3];
	int R[110];
	int T,N;
	scanf("%d",&T);
	int i;
	for(i=1;i<=T;i++)
	{
		cin>>N;
		int j;
		int freetime=0;
		char lastchar='T',nowchar;
		int timeuse=0;
		int nowlocO=1;
		int nowlocB=1;
		for(j=1;j<=N;j++)
		{
			scanf("%s %d",P[j],&R[j]);
			nowchar=P[j][0];
			int temp;
			if(P[j][0]=='O')
			{
				temp=1+abs(R[j]-nowlocO);
			}
			else
			{
				temp=1+abs(R[j]-nowlocB);
			}
			if(lastchar!=nowchar)
			{
				
				if(freetime>=temp)
				{
					freetime=1;
					lastchar=nowchar;
					timeuse+=1;
				}
				else if(freetime<temp)
				{
					freetime=temp-freetime;
					lastchar=nowchar;
					timeuse+=freetime;
				}
				
			}
			else
			{
				
				freetime+=temp;
				timeuse+=temp;
			}
			if(P[j][0]=='O')
			{
				nowlocO=R[j];
			}
			else
			{
				nowlocB=R[j];
			}
			//cout<<j<<"time use:"<<timeuse<<"  freetime:"<<freetime<<"locO:"<<nowlocO<<"locB"<<nowlocB<<"lastchar:"<<lastchar<<endl;
		}
			cout<<"Case #"<<i<<": "<<timeuse<<endl;

	}

		
	
return 0;
}