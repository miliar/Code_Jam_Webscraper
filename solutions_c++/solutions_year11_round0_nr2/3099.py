/*Written by Vladimir Ignatiev aka Neacher (neacher@gmail.com)*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(A=0;(int)A<(int)B;++A)
#define repi(A,I,B) for(A=I;(int)A<(int)B;++A)
#define repd(A,B) for(A=B-1;A>=0;--A)
#define repdi(A,I,B) for(A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);
#define mp make_pair

int C,D,N;
map<string,string> mapC;
multimap<char,char> mapD;

void f(string& str)
{	
	int i;
	map<string,string>::iterator posC;
	multimap<char,char>::iterator posD;
	
	char sstr[3];
	sstr[2]='\0';
	
	repi(i,1,str.length())
	{
		sstr[0]=str[i];
		sstr[1]=str[i-1];
		posC=mapC.find(sstr);
		if(posC!=mapC.end())
			str.replace(--i,2,posC->second);
		
		posD=mapD.find(str[i]);
		if(posD!=mapD.end())
			if(string::npos!=str.rfind(posD->second,i))
			{
				str.replace(0,i+1,"");
				i=0;
			}
	}
}

int main()
{
	FILE* In=fopen("B.in","r");if(!In) return 1;
	FILE* Out=fopen("B.res","w");if(!Out) return 2;

	int  nCount,i,j;
	char sstr[4]={'\0','\0','\0','\0'};

	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d%*[ ]",&C);
		mapC.clear();
		rep(j,C)
		{
			fscanf(In,"%c%c%c%*[ ]",sstr,sstr+1,sstr+3);
			mapC.insert(mp<string,string>(sstr,sstr+3));
			swap<char>(sstr[0],sstr[1]);
			mapC.insert(mp<string,string>(sstr,sstr+3));
		}

		fscanf(In,"%d%*[ ]",&D);
		mapD.clear();

		rep(j,D)
		{
			fscanf(In,"%c%c%*[ ]",sstr,sstr+1);
			mapD.insert(mp<char,char>(sstr[0],sstr[1]));
			mapD.insert(mp<char,char>(sstr[1],sstr[0]));
		}

		fscanf(In,"%d",&N);
		string str;
		str.resize(N);
		fscanf(In,"%s",str.c_str());
		f(str);

		fprintf(Out,"[");
		rep(j,str.length()-1) fprintf(Out,"%c, ",str[j]);
		if(str.length())
			fprintf(Out,"%c",str[str.length()-1]);
		fprintf(Out,"]\n");
	};
	fclose(In);
	fclose(Out);
	return 0;
}