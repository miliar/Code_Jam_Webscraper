#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
 
using namespace std;


void main()
{
//	string Ans,Ano,Anosys,Targetnosys;

//	Ans=findnumber("9","0123456789","oF8");

	ifstream input("1.txt");
	ofstream output;
	output.open("2.txt");

	//char s1[4000];
	string s1;

	vector<string> data;

//	input.getline(s1,'\n');
	//input.c
	while(!input.eof())
	{
		getline(input,s1);
		data.push_back(s1);
		
	}


	istringstream strin(data[0]);
	int Testcases;
	strin >> Testcases;
	int No_Search_engine[102];
	int No_of_Quary[1002];
	int i=0;
	int j=1;
	while(i<Testcases)
	{
		istringstream strin(data[j]);
		strin>>No_Search_engine[i];
		int searchptr=j+1;
		j=j+No_Search_engine[i]+1;
		
		istringstream strin1(data[j]);
		strin1>>No_of_Quary[i];

		int quaryptr=j+1;

		//Process the message

		string Ts1;
		string FS,TS;
		int flag=0,p=0;
		int Nooftimef=1002,Lastposf=0,length=0;
		for(int m=0;m<No_Search_engine[i];m++)
		{
			
			Ts1 = data[searchptr+m];
			int Nooftime=0,Lastpos=0;
			

			for(int n=0;n<No_of_Quary[i];n++)
			{
				if(Ts1==data[quaryptr+n])
				{
					Lastpos=n;


					if(n==0)Nooftime++;
					if((n!=0)&&Ts1!=data[quaryptr+n-1])
					{
					Nooftime++;
					}
									
				//	if(((n+1)!=No_of_Quary[i])&&(Ts1!=data[quaryptr+n+1]))
					if((n+1)!=No_of_Quary[i])
					{
					//select the next best engine
					for(p=0;p<No_Search_engine[i];p++)
					{
						TS=data[searchptr+p];
						int q=n,len=0;
						while(q<No_of_Quary[i])
						{
						if(TS!=data[quaryptr+q])
						{
							len++;
						}
						else{
							//stop
							break;
						}
						if(len>length)
						{
							length=len;
							Ts1=TS;
						}
						q++;
						}
					}
					length=0;


					}

				}
			}

			
			if(Nooftime<=Nooftimef)
			{
				if(Nooftime==Nooftimef)
				{
					if(Lastpos>Lastposf)
					{
						Lastposf=Lastpos;
						Nooftimef=Nooftime;
						FS=Ts1;
					}
				}
				else
				{
						Lastposf=Lastpos;
						Nooftimef=Nooftime;
						FS=Ts1;
				}

			}

		}
		

		output<<"Case #"<<i+1<<": "<<Nooftimef<<"\n";

		//cout<<Nooftimef;
		//dont alter i or j before
		j+=No_of_Quary[i]+1;
		i++;
	}
		



	output.close();
	input.close();
	

	//int a;
	//cin>>a;
};