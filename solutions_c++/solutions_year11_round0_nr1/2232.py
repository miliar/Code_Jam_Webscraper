#include<iostream>
#include<vector>
#include<sstream>
#include<algorithm>
using namespace std;
int main()
{
	int cases;
	cin>>cases;
	for(int numCase=1;numCase<=cases;numCase++)
	{
		int buttons;
		cin>>buttons;
		int time=0;
		vector<char> a(buttons);
		vector<int> b(buttons);
		
		//Getting Input part.
		for(int i=0;i<buttons;i++)
			cin>>a[i]>>b[i];
		
		//Declaring variables for keeping track of state
		int prevtime=0,opos=1,bpos=1;
		char prevchar=a[0];

		for(int i=0;i<buttons;i++)
		{
			int target=b[i];

			if(a[i]=='O')
			{
				
				if(prevchar!='O')
				{
					if(prevtime>=abs(target-opos))
						opos=target;
					else if(target>opos) { opos+=prevtime;}
					else if(target<opos) {	opos-=prevtime;}
					prevtime=0;
				}	

				time+=abs(target-opos);
				time++;
				prevtime+=abs(target-opos);
				prevtime++;
				opos=target;
				prevchar='O';
				
			}

			if(a[i]=='B')
			{
				
				if(prevchar!='B')
				{
					if(prevtime>=abs(target-bpos))
						bpos=target;
					else if(target>bpos) { bpos+=prevtime;}
					else if(target<bpos) {	bpos-=prevtime;}
					prevtime=0;				
				}	

				time+=abs(target-bpos);
				time++;
				prevtime+=abs(target-bpos);
				prevtime++;
				bpos=target;
				prevchar='B';
				
			}

			
		}
		
		cout<<"Case #"<<numCase<<": "<<time<<endl;
	}
	return 0;
}
