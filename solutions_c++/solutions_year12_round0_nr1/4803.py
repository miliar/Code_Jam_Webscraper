#include <iostream>
#include <string>
#include <map>
#include <vector>

using std::vector;
using std::map;
using std::string;
using std::cin;
using std::cout;
using std::endl;

void Initialize_Map(map<char,char> &MapIt,const string &InStr,const string &OutStr)
{
	for (string::size_type i=0;i!=InStr.size();i++)
	{
		MapIt[InStr[i]]=OutStr[i];
	}
}

int main()
{
	map<char,char> LanMap;
	string Inline,OutLine;
	vector<string> OutLines;
	int Num;

	string InStr1,InStr2,InStr3,OutStr1,OutStr2,OutStr3;
	InStr1	=	"ejp mysljylc kd kxveddknmc re jsicpdrysi";
	InStr2	=	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	InStr3	=	"de kr kd eoya kw aej tysr re ujdr lkgc jv";

	OutStr1	=	"our language is impossible to understand";
	OutStr2	=	"there are twenty six factorial possibilities";
	OutStr3	=	"so it is okay if you want to just give up";

	Initialize_Map(LanMap,InStr1,OutStr1);
	Initialize_Map(LanMap,InStr2,OutStr2);
	Initialize_Map(LanMap,InStr3,OutStr3);

	LanMap['q']='z';
	LanMap['z']='q';

	cin>>Num;
	cin.ignore(1000,'\n');
	for (unsigned i=0;i!=Num;i++)
	{
		getline(cin,Inline);
		for (string::size_type j=0;j!=Inline.size();j++)
		{
			OutLine+=LanMap[Inline[j]];
		}
		OutLines.push_back(OutLine);
		OutLine.clear();
	}

	for (unsigned i=0;i!=Num;i++)
	{
		cout<<"Case #"<<i+1<<": "<<OutLines[i]<<endl;
	}
	return 0;
}