#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int i;
	for(i=1;i<=t;i++)
	{
		int c,d,n;
		scanf("%d",&c);
		char invoke[30][30];
		int opposed[30][30];
		int appear[30];
		int o; for(o=0;o<30;o++) appear[o]=0;
		int j,k;
		for(j=0;j<=27;j++)
			for(k=0;k<=27;k++)
				invoke[j][k]='*';
		for(j=0;j<=27;j++)
			for(k=0;k<=27;k++)
				opposed[j][k]=0;
		for(j=1;j<=c;j++)
		{
			char ch[10];
			scanf("%s",ch);
			invoke[ch[0]-'A'][ch[1]-'A']=ch[2];
			invoke[ch[1]-'A'][ch[0]-'A']=ch[2];
		}
		scanf("%d",&d);
		for(j=1;j<=d;j++)
		{
			char ch[10];
			scanf("%s",ch);
			opposed[ch[0]-'A'][ch[1]-'A']=1;
			opposed[ch[1]-'A'][ch[0]-'A']=1;
		}
		scanf("%d",&n);
		char ch[200];
		char answer[200];
		char lastchar='Z'+1;
		int ansn=0;
		scanf("%s",ch);
		for(j=0;j<n;j++)
		{
			if(ansn==0)
			{
				answer[ansn++]=ch[j];
				lastchar=ch[j];
				appear[ch[j]-'A']=1;
			//	cout<<"zhengchang"<<endl;
				continue;
			}
			if(invoke[lastchar-'A'][ch[j]-'A']!='*' || invoke[ch[j]-'A'][lastchar-'A']!='*')
			{
				answer[ansn-1]=invoke[lastchar-'A'][ch[j]-'A'];
				appear[lastchar-'A']--;
				lastchar=answer[ansn-1];
			//	cout<<"HEFING"<<endl;
			}
			else
			{
				if(opposed[ch[j]-'A']['Q'-'A']==1 && appear['Q'-'A']>=1)
				{
					
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
					//	cout<<"asd"<<endl;
					

				}
				else if(opposed[ch[j]-'A']['W'-'A']==1 && appear['W'-'A']>=1)
				{
					
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else if(opposed[ch[j]-'A']['E'-'A']==1 && appear['E'-'A']>=1)
				{
				
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else if(opposed[ch[j]-'A']['R'-'A']==1 && appear['R'-'A']>=1)
				{
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
				}
				else if(opposed[ch[j]-'A']['A'-'A']==1 && appear['A'-'A']>=1)
				{
					
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else if(opposed[ch[j]-'A']['S'-'A']==1 && appear['S'-'A']>=1)
				{
				
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else if(opposed[ch[j]-'A']['D'-'A']==1 && appear['D'-'A']>=1)
				{
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else if(opposed[ch[j]-'A']['F'-'A']==1 && appear['F'-'A']>=1)
				{
			
						int o;
						for(o=0;o<30;o++) appear[o]=0;
						ansn=0;
						lastchar='Z'+1;
						//cout<<"asd"<<endl;
					
				}
				else
				{
					answer[ansn++]=ch[j];
					appear[ch[j]-'A']++;
					lastchar=ch[j];
					//cout<<"zhengchang"<<endl;
				}
			}
		

		}
			cout<<"Case #"<<i<<": [";
			for(j=0;j<ansn;j++) 
			{
				printf("%c",answer[j]);
				if(j!=ansn-1) cout<<", ";
			}
			cout<<"]"<<endl;




	}
	return 0;
}