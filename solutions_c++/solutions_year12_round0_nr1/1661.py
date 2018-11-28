#include <iostream>
#include <string.h>
#include <stdlib.h>
using namespace std;

int count()
{
	int round=0;
	char googlerese[100];
	char normal[100];
	char map[26];
	int num;
	memset(map,0,26);
	cin >>round;
	cin.ignore();
	for (int i=0;i<round;i++)
	{
		memset(googlerese,0,100);
		memset(normal,0,100);
		cin.getline(googlerese,100);
		cin.getline(normal,100);
		for(int j=0;j<100&&'\0'!=googlerese[j];j++)
		{
			num=googlerese[j]-'a';
			if(num>=0&&num<26)
			{
				if(0==map[num])
				{
					map[num]=normal[j];
				}
			}

		}
	}
	for (int i=0;i<26;i++)
		cout<<map[i]<<',';
	cout<<endl;
	return 0;
}

int main() {
	int round=0;
	char googlerese[101];
	char normal[101];
	char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int num=0;
	cin >>round;
	if(-1 == round)
	{
		count();
	}
	else
	{
		cin.ignore();
		for (int i=0;i<round;i++)
		{
			memset(googlerese,0,101);
			cin.getline(googlerese,101);
			memset(normal,0,101);
			for(int j=0;j<100&&'\0'!=googlerese[j];j++)
			{
				num=googlerese[j]-'a';
				if(num>=0&&num<26)
				{
					normal[j]=map[num];
				}
				else if(' '==googlerese[j])
				{
					normal[j]=googlerese[j];
				}

			}
			cout<<"Case #"<<i+1<<": "<<normal<<endl;
		}
	}
	return 0;
}
