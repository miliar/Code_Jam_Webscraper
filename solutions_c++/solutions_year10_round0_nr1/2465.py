#include <iostream>
using namespace std;
unsigned long T;
unsigned long N,K;
unsigned long lookuptable[]=
{
	0,//0
	1,//1
	3,//2
	7,//3
	15,//4
	31,//5
	63,//6
	127,//7
	255,//8
	511,//9
	1023,//10
	2047,//11
	4095,//12
	8191,//13
	16383,//14
	32767,//15
	65535,//16
	131071,//17
	262143,//18
	524287,//19
	1048575,//20
	2097151,//21
	4194303,//22
	8388607,//23
	16777215,//24
	33554431,//25
	67108863,//26
	134217727,//27
	268435455,//28
	536870911,//29
	1073741823//30
};

int main()
{
	cin>>T;
	unsigned long test;
	for(unsigned int i=1;i<=T;i++)
	{
		cin>>N>>K;
		test=lookuptable[N]&K;
		test=test^lookuptable[N];
		cout<<"Case #"<<i<<": ";
		if(test)
			cout<<"OFF"<<endl;
		else
			cout<<"ON"<<endl;
	}
	return 0;
}
