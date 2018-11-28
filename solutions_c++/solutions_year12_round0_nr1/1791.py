#include <iostream>
#include <string>
#include <map>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main()
{
    map<char, char> charMap;
    string aa = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
    string AA = "our language is impossible to understand";
    for(int i=0;i<aa.length();i++)
    {
	if(aa[i]>='a'&&aa[i]<='z')
	   charMap.insert(pair<char,char>(aa[i],AA[i]));
    }

    aa = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    AA = "there are twenty six factorial possibilities";
    for(int i=0;i<aa.length();i++)
    {
	if(aa[i]>='a'&&aa[i]<='z')
	   charMap.insert(pair<char,char>(aa[i],AA[i]));
    }

    aa = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
    AA = "so it is okay if you want to just give up";
    for(int i=0;i<aa.length();i++)
    {
	if(aa[i]>='a'&&aa[i]<='z')
	    charMap.insert(pair<char,char>(aa[i],AA[i]));
    }
    charMap.insert(pair<char,char>('q','z'));
    charMap.insert(pair<char,char>('z','q'));
    //freopen("A-small-attempt3.in","r",stdin);
    //freopen("data.out","w",stdout);

    int T;
    getline(cin,aa);
    T = atoi(aa.c_str());
    for(int i=0;i<T;i++)
    {
	getline(cin,aa);
	AA = "";
	for(int j=0;j<aa.length();j++)
	{
	    if(aa[j]>='a'&&aa[j]<='z')
		AA += charMap[aa[j]];
	    else
		AA += aa[j];
	}
	cout <<"Case #"<<i+1<<": "<< AA <<endl;
    }
    //fclose(stdin);
    //fclose(stdout);
    return 0;
}
