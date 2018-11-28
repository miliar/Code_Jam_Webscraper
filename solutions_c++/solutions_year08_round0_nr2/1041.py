#include<iostream>
#include<string>
#include<fstream>
#include<algorithm>
	using namespace std;

int caseCnt;
int NA;
int NB;	
int T;

struct TNode
{
	int leave;
	int time;
};

bool operator < (TNode a,TNode b)
{
	return (a.time<b.time||(a.time==b.time&&a.leave==0));
};

TNode TA[200];

TNode TB[200];

int ta;
int tb;

int TFA;
int TFB;


int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	
	fin>>caseCnt;

	int i;
	for(i=0;i<caseCnt;i++)
	{
		
		fin>>T;
		fin>>NA;
		fin>>NB;
		ta=0;
		tb=0;
		int j;
		for(j=0;j<NA;j++)
		{
			int a,b;
			char ch;

			fin>>a>>ch>>b;
			TA[ta].time=a*60+b;
			TA[ta].leave=1;
			ta++;
		
			fin>>a>>ch>>b;
			TB[tb].time=a*60+b;
			TB[tb].leave=0;
			tb++;
			
			
		}
		for(j=0;j<NB;j++)
		{
			int a,b;
			char ch;
			
			fin>>a>>ch>>b;
			TB[tb].time=a*60+b;
			TB[tb].leave=1;
			tb++;
			fin>>a>>ch>>b;
			TA[ta].time=a*60+b;
			TA[ta].leave=0;
			ta++;			
		}

		
		sort(&TA[0],&TA[0+ta]);
		sort(&TB[0],&TB[0+tb]);
				
		TFA=0;
		TFB=0;

		int W=0;
		int fla=-1;
		int iss=0;
		for(iss=0;iss<ta;iss++)
		{
			if(TA[iss].leave!=1)
			{
				if(fla==-1)fla=iss;
				W++;
			}
			else 
			{
				if(W<=0)TFA++;
				else
				{
					if(TA[fla].time+T>TA[iss].time)TFA++;
					else
					{
						W--;
						if(W>0)
						{
							int sf;
							for(sf=fla+1;sf<iss;sf++)
							{
								if(TA[sf].leave!=1)
								{
									fla=sf;
									break;
								}
								
							}
						}
						else 

						{
							fla=-1;
						}
					}
				}				
			}
		}
	

		 W=0;
		 fla=-1;
		 iss=0;
		for(iss=0;iss<tb;iss++)
		{
			if(TB[iss].leave!=1)
			{
				if(fla==-1)fla=iss;
				W++;
			}
			else 
			{
				if(W<=0)TFB++;
				else
				{
					if(TB[fla].time+T>TB[iss].time)TFB++;
					else
					{
						W--;
						if(W>0)
						{
							int sf;
							for(sf=fla+1;sf<iss;sf++)
							{
								if(TB[sf].leave!=1)
								{
									fla=sf;
									break;
								}
							}

						}
						else 

						{
							fla=-1;
						}
					}
				}				
			}
		}
		
		fout<<"Case #"<<(i+1)<<": "<<TFA<<" "<<TFB<<endl;

	}

	fin.close();
	fout.close();

	return 0;
}

