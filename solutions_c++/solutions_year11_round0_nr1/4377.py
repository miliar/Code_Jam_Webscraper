#include<iostream>
 
using namespace std;


int main()
{
	int t=0;
	cin>>t;


	
	for(int z=1;z<=t;z++)
	{
		
		bool turn[100]={false};
		int button[100]={0};
		char ch;
		int n;
		cin>>n;
		int otcount=1,btcount=1;//total number of o turns and b turns
		int ocp=1,bcp=1;//o,b current position bot 

		int ot[100]={0},bt[100]={0};
		for(int i=1;i<=n;i++)
		{
			cin>>ch;
			turn[i]=((ch=='O'||ch=='o') ? true : false );//true for o false for b
			cin>>button[i];
			if(turn[i])
				ot[otcount++]=button[i];
			else 
				bt[btcount++]=button[i];
			
		}
		int sequence=1;//loop variable for all button press
		int time=0;	
		int otc=1,btc=1;//loop variables to cover all the elements
		
		while (sequence<=n)
		{
			++time;
			int flag=0;
			if(turn[sequence])
			{
				if(ot[otc]>ocp)
				{
					ocp++;	
					//cout<<"\nMove O to "<<ocp<<"\ttime"<<time;
				}
				else if(ot[otc]<ocp)
					ocp--;
				else if(ot[otc]==ocp)
				{
					otc++;
					flag=1;
					//cout<<"\nPush O  "<<ocp<<"\ttime"<<time;
				}
				if(bt[btc]>bcp)
				{
					bcp++;
					//cout<<"\nMove to B "<<bcp<<"\ttime"<<time;
				}
				else if (bt[btc]<bcp)
					bcp--;				
				else if(bt[btc]==bcp)
				{
					//DO NOTHING					
					//cout<<"\n B Stay at "<<bcp<<"\ttime"<<time;;
				}
				
			}
			else//if blue bot	
			{
				if(bt[btc]>bcp)
				{
					bcp++;
					//cout<<"\nMove to B "<<bcp<<"\ttime"<<time;;	
				}
				//else if(ot[otc]>ocp)
				//	ocp++;
				else if (bt[btc]<bcp)
					bcp--;	
				else if(bt[btc]==bcp)
				{
					btc++;
					//cout<<"\nPush  B "<<bcp<<"\ttime"<<time;;
					flag=1;
				}
				if(ot[otc]>ocp)
				{
					ocp++;
					//cout<<"\nMove O to "<<ocp;
				//else if(ot[otc]>ocp)
				//	ocp++;
				}
				else if(ot[otc]<ocp)
					ocp--;
				else if(ot[otc]==ocp)
				{
					//DO NOTHING 
					//cout<<"\n O Stay at "<<ocp<<"\ttime"<<time;;
				}
//				cout<<"\n\n";
			}
			if(flag)
				sequence++;
		
		}		
		cout<<"Case #"<<z<<": "<<time<<endl;
	}//end of ultimate while
	return 0;
}		

		
								



