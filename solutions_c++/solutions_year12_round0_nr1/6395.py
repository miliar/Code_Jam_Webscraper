#include<iostream>
#include<fstream>
#include<string>
using namespace std;
string Example[2][4];
char Code[26];
char Input[30][101];
int N;

void DoMeAFavor(string ToCode,string Coded)
{
	int length=Coded.size();
	for(int i=0;i<length;i++)
		Code[ToCode[i]-'a']= Coded[i];
}
char DecodeIt(char c)
{
	if(c==' ')return c;
	return Code[c-'a'];
}
int main()
{
	freopen("A-small-attempt3.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	Code[25]='q';
	
	Example[0][0]="y qee";
	Example[1][0]="a zoo";

	DoMeAFavor(Example[0][0],Example[1][0]);

	Example[0][1]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
	Example[1][1]="our language is impossible to understand";
	
	DoMeAFavor(Example[0][1],Example[1][1]);

	Example[0][2]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	Example[1][2]="there are twenty six factorial possibilities";

	DoMeAFavor(Example[0][2],Example[1][2]);

	Example[0][3]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	Example[1][3]="so it is okay if you want to just give up";

	DoMeAFavor(Example[0][3],Example[1][3]);
	cin>>N;
	
	char c;
	int j;
	for(int i=0;i<N+1;i++)
	{
		j=0;
		scanf("%c",&c);
		while(c!='\n')
		{
			Input[i-1][j]=c;
			j++;
			scanf("%c",&c);
		}
	}
	int length;
	char d;
	for(int i=0;i<N;i++)
	{
		cout<<"Case #"<<i+1<<": ";
		for(int j=0;j<100;j++)
		{
			if(Input[i][j]==0)break;
			d=DecodeIt(Input[i][j]);
			cout<<d;
		}
		cout<<endl;
	}
	
	
	
	return 0;
}
