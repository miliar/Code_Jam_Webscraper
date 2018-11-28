//#pragma   warning(disable:4503   4511   4512   4514   4663   4786) 
#pragma   warning(disable:4786) 
#include <iostream>
#include <string>
#include <map>
#include <iterator>
#include <cctype>
using namespace std;
int main()
{
	string src("ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv");
	string des("our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up");
	map<char,char> gmap;
	int len=src.length();
	//string::itetator sit = src.begin();
	for(int i=0; i<len; i++)
	{
		char c = src[i];
		if(c != ' ')
			gmap[c]=des[i];
	}
	gmap['z']='q';
	gmap['q']='z';
	gmap[' ']=' ';
/*	map<char,char>::iterator mapit1 = gmap.begin();
	map<char,char>::iterator mapit2 = gmap.end();
	while(mapit1 != mapit2)
	{
		cout<<(*mapit1).first<<' '<<(*mapit1).second<<endl;
		mapit1++;
	}
	cout<<"map size is: "<<gmap.size()<<endl;
*/
	FILE *fpIn = fopen("A-small-attempt1.in","r");
	FILE *fpOut = fopen("1.out","w");
	char buf[120];
	int ilen;
	fgets(buf,sizeof(buf),fpIn);
	ilen = atoi(buf);
	for(i=0; i<ilen; i++)
	{
		int j=0;
		fgets(buf,sizeof(buf),fpIn);
		while(buf[j]!='\0')
		{
			buf[j] = gmap[buf[j]];
			j++;
		}
		fprintf(fpOut,"Case #%d: %s\n",i+1,buf);
		//cout<<buf<<endl;
	}
//	cout<<ilen<<endl;
	fclose(fpIn);
	fclose(fpOut);
	
	
	return 0;
}