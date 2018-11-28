#include<algorithm>
#include<vector>
#include<string.h>
#include<sstream>
#include<iostream>
#include<cstring>
#include<fstream>
using namespace std;

int main(void)
{
int caseno=0,hr=0,min=0,N=0,DELAY=0,ntA=0,ntB=0,countA=0,countB=0;
char ch;
string str;
vector <int> aaa,aab,dfa,dfb;
ifstream file("input.in");
ofstream outputfile("output");

if(file.is_open())
	{	file>>N;
		getline(file,str);//<<endl;					//reads in no of test cases....then endl.....
		
//file>>hr>>ch>>min;
//cout<<((hr*60)+min);
	while((++caseno)<=N)
		{
		file>>DELAY;
		file>>ntA>>ntB;
			for(int ii=0;ii<ntA;ii++)
				{
				file>>hr>>ch>>min;
				dfa.push_back((hr*60)+min);
				file>>hr>>ch>>min;
				aab.push_back((hr*60)+DELAY+min);
				}
			for(int ii=0;ii<ntB;ii++)
				{
				file>>hr>>ch>>min;
				dfb.push_back((hr*60)+min);
				file>>hr>>ch>>min;
				aaa.push_back((hr*60)+DELAY+min);
				}
			countA=ntA;
			countB=ntB;
		
			sort(dfa.begin(),dfa.end());
			sort(aaa.begin(),aaa.end());
			sort(dfb.begin(),dfb.end());
			sort(aab.begin(),aab.end());
		
				for(int jj=0,kk=0;(jj<dfa.size())&&(kk<aaa.size());jj++)
				{
					if((dfa[jj])>=aaa[kk])
					{
						countA--;
						kk++;
//						dfa.erase(dfa.begin()+jj,dfa.begin()+jj+1);	
//						aaa.erase(aaa.begin()+kk,aaa.begin()+kk+1);
					}	
				}
				for(int jj=0,kk=0;(jj<dfb.size())&&(kk<aab.size());jj++)
				{
					if((dfb[jj])>=aab[kk])
					{
						countB--;
						kk++;
//						dfb.erase(dfb.begin()+jj,dfb.begin()+jj+1);	
//						aab.erase(aab.begin()+kk,aab.begin()+kk+1);
					}	
				}

		outputfile<<"Case #"<<caseno<<": "<<countA<<" "<<countB<<"\n";
		aaa.clear();
		aab.clear();
		dfa.clear();
		dfb.clear();	
		}//end of while
	}
file.close();
outputfile.close();
return 0;
}
