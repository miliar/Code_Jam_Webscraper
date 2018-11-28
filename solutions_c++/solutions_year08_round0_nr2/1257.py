#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<conio.h>
#include<map>
using namespace std;

#define LABEL_A 0
#define LABEL_B 1



int main()
{
    int N,T,NA,NB;
    char s[100];
    fstream in("input1a.in",ios::in);
    fstream out("prabukjpoo.out",ios::out);
	
    in>>N;
    cout<<N<<endl;
	
    for(int n=0;n<N;n++)
    {
		double temp1=0,temp2=0;
		in>>T;
		in>>NA;
		in>>NB;
		
		cout<<T<<endl;
		cout<<NA<<"\t"<<NB<<endl;            
		
		
		vector<int>Ad(NA);
		vector<int>Aa(NA);
		vector<int>Bd(NB);
		vector<int>Ba(NB);
		int i;
		
		for(i=0;i<NA;++i)
		{                   
			in.getline((char *)s,2000,':');
			temp1=atoi(s);
			
			in.getline((char *)s,2000,' ');
			temp2=atoi(s);
			
			Ad[i]=(60*temp1)+temp2;              
			//cout<<"d value:"<<Ad[i]<<endl;
			
			in.getline((char *)s,2000,':');
			temp1=atoi(s);
			
			in.getline((char *)s,2000,'\n');
			temp2=atoi(s);
			
			Aa[i]=(60*temp1)+temp2;       
			//cout<<"a value:"<<Aa[i]<<endl;
		}
		
		for(i=0;i<NB;++i)
		{                   
			in.getline((char *)s,2000,':');
			temp1=atof(s);
			
			in.getline((char *)s,2000,' ');
			temp2=atof(s);
			
			Bd[i]=(60*temp1)+temp2;              
			//cout<<"d value:"<<Bd[i]<<endl;
			in.getline((char *)s,2000,':');
			temp1=atof(s);
			
			in.getline((char *)s,2000,'\n');
			temp2=atof(s);
			
			Ba[i]=(60*temp1)+temp2;       
			//cout<<"a value:"<<Ba[i]<<endl;
		}
		
		sort(Aa.begin(),Aa.end());
		sort(Ba.begin(),Ba.end());
		sort(Ad.begin(),Ad.end());
		sort(Bd.begin(),Bd.end());
		int countA=0,countB=0;

		if(NA==0)
		{
			countA = 0;
			countB = NB;
		}
		if(NB == 0)
		{
			countA = NA;
			countB = 0;
		}
		
		if(NA!=0 && NB!=0)
		{
			for(i=0; i<NA; i++)
			{
				for(int j=NB-1;j>=0;j--)
				{
					cout<<Ba[j]<<"\t"<<Ad[i];
					if((Ba[j]!=-1) && (Ba[j]+T<=Ad[i]))
					{
						cout<<"No new train\n";
						Ad[i]=-1;
						Ba[j]=-1;
						
					}
				}
				if(Ad[i]!=-1)
					countA++;
			}
			
			for(i=0; i<NB; i++)
			{
				for(int j=NA-1;j>=0;j--)
				{
					if((Aa[j]!=-1) && (Aa[j]+T<=Bd[i]))
					{
						Bd[i]=-1;
						Aa[j]=-1;
					}
				}
				if(Bd[i]!=-1)
					countB++;
			}
		}
		
		out<<"Case #"<<n+1<<": "<<countA<<"\t"<<countB<<endl;
		cout<<"Case #"<<n+1<<": "<<countA<<"\t"<<countB<<endl;
    }
    in.close();
    out.close();
	system("pause");
	return 0;
}
