#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>


using namespace std;
ifstream fin;
ofstream fout;
struct TIME
{
	int hour,minute;
};

struct TRAIN
{
	int flag;
	TIME arrive,depart;
};
void BSort(TRAIN a[],int num)
{
	int i,j;
	TRAIN temp;
	for(j=num-1;j>0;j--)
	{
		for(i=0;i<j;i++)
		{
			if(a[i].depart.hour>a[i+1].depart.hour||
				(a[i].depart.hour==a[i+1].depart.hour&&
				a[i].depart.minute>a[i+1].depart.minute))
			{
				temp=a[i];
				a[i]=a[i+1];
				a[i+1]=temp;
			}

		}
	}
}
int main(void)
{
	int i,j,k,l,N,NA,NB,RA,RB;
	fin.open("input.in");
	fout.open("output.out");
	fin>>N;
//	fin>>noskipws;
//	fin>>skipws;
	TIME T;
	TRAIN TA[150],TB[150];
	string s,s1;
	TIME tmp;
	for(i=1;i<=N;i++)
	{
		fin>>T.minute;
		T.hour=0;
		if(T.minute==60)
		{
			T.hour=1;
			T.minute=0;
		}
		fin>>NA>>NB;
		for(j=0;j<NA;j++)
		{
			TA[j].flag=1;
			fin>>s;
			s1=s[0];
			s1+=s[1];
			TA[j].depart.hour=atoi(s1.c_str());
			s1=s[3];
			s1+=s[4];
			TA[j].depart.minute=atoi(s1.c_str());

			fin>>s;
			s1=s[0];
			s1+=s[1];
			TA[j].arrive.hour=atoi(s1.c_str());
			s1=s[3];
			s1+=s[4];
			TA[j].arrive.minute=atoi(s1.c_str());
		}
		for(j=0;j<NB;j++)
		{
			TB[j].flag=1;
			fin>>s;
			s1=s[0];
			s1+=s[1];
			TB[j].depart.hour=atoi(s1.c_str());
			s1=s[3];
			s1+=s[4];
			TB[j].depart.minute=atoi(s1.c_str());
			fin>>s;
			s1=s[0];
			s1+=s[1];
			TB[j].arrive.hour=atoi(s1.c_str());
			s1=s[3];
			s1+=s[4];
			TB[j].arrive.minute=atoi(s1.c_str());
		}
		BSort(TA,NA);
		BSort(TB,NB);
		for(j=0;j<NA;j++)
		{
			for(k=0;k<NB;k++)
			{
				tmp.hour=TA[j].arrive.hour+T.hour;
				tmp.minute=TA[j].arrive.minute+T.minute;

				if(TB[k].flag==1&&(tmp.hour<TB[k].depart.hour||
					(tmp.hour==TB[k].depart.hour&&
					tmp.minute<=TB[k].depart.minute)))
				{
					TB[k].flag=0;
					break;
				}
			}
		}
		for(j=0;j<NB;j++)
		{
			for(k=0;k<NA;k++)
			{
				tmp.hour=TB[j].arrive.hour+T.hour;
				tmp.minute=TB[j].arrive.minute+T.minute;

				if(TA[k].flag==1&&(tmp.hour<TA[k].depart.hour||
					(tmp.hour==TA[k].depart.hour&&
					tmp.minute<=TA[k].depart.minute)))
				{
					TA[k].flag=0;
					break;
				}
			}
		}
		RA=RB=0;
		for(j=0;j<NA;j++)
		{
			if(TA[j].flag==1)
				RA++;
		}
		for(j=0;j<NB;j++)
		{
			if(TB[j].flag==1)
				RB++;
		}
		fout<<"Case #"<<i<<": "<<RA<<" "<<RB<<endl;
	}
    fin.close();
	fout.close();
	return 0;
}
