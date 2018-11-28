#include<iostream>
#include<vector>

using namespace std;

struct time1{
int S,E;
};

int sort(vector <struct time1> &V)
{
	for (int i =0;i<(int)V.size()-1;i++)
	{
		for(int j=i+1;j<(int)V.size();j++)
		{
			if( V[i].E > V[j].E)
			{
					struct time1 temp;
					temp = V[i];
					V[i] = V[j];
					V[j] = temp;				
			}
		}
	}
}	

int sorts(vector <struct time1> &V)
{
	for (int i =0;i<(int)V.size()-1;i++)
	{
		for(int j=i+1;j<(int)V.size();j++)
		{
			if( V[i].S > V[j].S)
			{
					struct time1 temp;
					temp = V[i];
					V[i] = V[j];
					V[j] = temp;				
			}
		}
	}
}

int convert2int(char* ch)
{
	int H, M;
	H = atoi(ch);
	
	while(*ch!=':')
		ch++;
	ch++;
	
	M = atoi(ch);
	return(H*60+M);
	
}
	
	

int main()
{
	int testCases;
	cin>>testCases;

	int count = 1;
	while(count<=testCases)
	{
		int T, NA,NB;
		cin>>T>>NA>>NB;
	
		vector<struct time1> NAT;
		vector<struct time1> NBT;
		vector <int> flag1, flag2;
		flag1.clear();flag2.clear();
		NAT.clear(); NBT.clear();

		for (int i=0;i<NA;i++)
		{
			
			struct time1 temp;
			//int SH, SM, EH, EM;
			//cin>>SH>>SM>>EH>>EM;
			//temp.S = SH*60+SM;
			//temp.E = EH*60+EM;
			
			char str[100];	
			cin>>str;
			temp.S = convert2int(str);
			
			cin>>str;
			temp.E = convert2int(str);
				
			NAT.push_back(temp);
			flag1.push_back(1);
		}
	
		for (int i=0;i<NB;i++)
		{
			struct time1 temp;
			char str[100];	
			cin>>str;
			temp.S = convert2int(str);
			
			cin>>str;
			
			temp.E = convert2int(str);
			
			//int SH, SM, EH, EM;
				
			//cin>>SH>>SM>>EH>>EM;
			///temp.S = SH*60+SM;
			//temp.E = EH*60+EM;
			
			NBT.push_back(temp);
			flag2.push_back(1);
		}

		
		// sort according to reach time
		// we need all the trains those start from there before that time
		// do the same thing for the BA train too
		// Keep adding number of trains till every flag is zero 
		
		
		vector<struct time1> NAT1,NBT1;
		NAT1.clear(); NBT1.clear();
		
		NAT1 = NAT;
		NBT1 = NBT;
						
		sort(NAT);
		sort(NBT);

		sorts(NAT1);
		sorts(NBT1);

		
		
	/*	
	 if(count == 13)	
	 {	cout<<T<<NA<<NB<<endl;
		for (int i =0;i<(int)NAT.size();i++)
		{
			cout<<NAT1[i].S<<" "<<NAT1[i].E<<endl;	
		}	
		
		cout << "      \n\n\n";
		for (int i =0;i<(int)NBT.size();i++)
		{
			cout<<NBT[i].S<<" "<<NBT[i].E<<endl;	
		}	
	
	*/		
		
		int cancel1 =0;
		int last = -1;
		
		for (int i =0;i<(int)NAT.size();i++)
		{
			for (int j=last+1;j<(int)NBT1.size();j++)
			{
				if(flag2[j] && NAT[i].E + T <= NBT1[j].S)
				{	
					cancel1++;
					flag2[j]=0;
					last = j;	
					break;
				}
			}
		}
	
		int cancel2 = 0;
		last =-1;
		for (int i =0;i<(int)NBT.size();i++)
		{
			for (int j =last+1;j<(int)NAT1.size();j++)
			{
				if(flag1[j] && NBT[i].E + T <= NAT1[j].S)
				{	
					cancel2++;
					flag1[j]=0;
					last = j;
					break;
				}
			}
			//cout<<last<<" "<<NBT[i].E+T<<" "<<NAT1[last].S<<endl;
		}
		
		cout<<"Case #"<<count<<": "<<NA-cancel2<<" "<<NB-cancel1<<endl;
				
	    			
		count++;
	    	
	}
}
