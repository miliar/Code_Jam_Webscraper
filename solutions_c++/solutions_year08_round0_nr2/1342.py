//Visual Studio 2008 
#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<list>

using namespace std;

class Time
{
public:
	int H;
	int M;
public:
	Time(int h=0,int m=0):H(h),M(m){}
	operator int()
	{
		int answer= (H*60)+M;
		return answer;
	}
};


void main()
{
	ifstream inFile("In.in");
	ofstream outFile("Out.txt");
	
	int N=0;
	inFile>>N;
	char HourString[3];
	char MinuteString[3];
	for(int i=1;i<=N;i++)
	{
		int T=0,NA=0,NB=0;
		inFile>>T;
		inFile>>NA>>NB;
		inFile.getline(HourString,2);

		list<Time> Ato(0);
		list<Time> toB(0);
		for(int j=0;j<NA;j++)
		{

			inFile.get(HourString,3);
			HourString[2]='\0';
			inFile.ignore();
			inFile.get(MinuteString,3);
			MinuteString[2]='\0';
			inFile.ignore();
			Ato.insert(Ato.end(),Time(atoi(HourString),atoi(MinuteString)));

			inFile.get(HourString,3);
			HourString[2]='\0';
			inFile.ignore();
			inFile.get(MinuteString,3);
			MinuteString[2]='\0';
			toB.insert(toB.end(),Time(atoi(HourString),atoi(MinuteString)));
			inFile.getline(HourString,3);
		}
		Ato.sort();
		toB.sort();

/////////////////////////////////////////
		list<Time> Bto(0);
		list<Time> toA(0);
		for(int j=0;j<NB;j++)
		{

			inFile.get(HourString,3);
			HourString[2]='\0';
			inFile.ignore();
			inFile.get(MinuteString,3);
			MinuteString[2]='\0';
			inFile.ignore();
			Bto.insert(Bto.end(),Time(atoi(HourString),atoi(MinuteString)));

			inFile.get(HourString,3);
			HourString[2]='\0';
			inFile.ignore();
			inFile.get(MinuteString,3);
			MinuteString[2]='\0';
			toA.insert(toA.end(),Time(atoi(HourString),atoi(MinuteString)));
			inFile.getline(HourString,3);
		}
		Bto.sort();
		toA.sort();

////////////////////////////////////////////////
///////////////////////////////////////////////
	int RA=NA,RB=NB; 
		Time T1,T2;
	for(int j=0;!toB.empty() && !Bto.empty();j++)
	{
		T1=Bto.front();
		T2=toB.front();
		if(T+(int)T2<=(int)T1)
		{
			Bto.pop_front();
			toB.pop_front();
			RB--;
		}
		else
			Bto.pop_front();

	}
	for(int j=0;!toA.empty() && !Ato.empty();j++)
	{
		T1=Ato.front();
		T2=toA.front();
		if((int)T2+T<=(int)T1)
		{
			Ato.pop_front();
			toA.pop_front();
			RA--;
		}
		else
			Ato.pop_front();

	}
	outFile<<"Case #"<<i<<": "<<RA<<' '<<RB<<endl;

	}
	inFile.close();
	outFile.close();

}