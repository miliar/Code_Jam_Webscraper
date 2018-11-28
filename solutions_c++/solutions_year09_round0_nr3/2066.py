// GoogleCode3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <vector>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	vector <char> s;
	int n,N,i,ss,j;
	long int sum;
	char c,sc;
	char ts[501];
	char *welcstr="welcome to code jam";
	int *WA;
	FILE* f;
	FILE* g;
	fopen_s(&f,"C-small.in","r");
	fopen_s(&g,"C-small.out","w");
	fscanf_s(f,"%d",&N);
	fgets(ts,501,f);
	for (n=0; n<N; ++n) {
		fgets(ts,501,f);
		for (i=0; (unsigned)i<strlen(ts); ++i) {
			c=ts[i];
			if (c=='a' || c=='c' || c=='d' || c=='e' || c=='j' || c=='l' || c=='m' || c=='o' || c=='t' || c=='w' || c==' ')
				s.push_back(c);
			/*if (c=='A' || c=='C' || c=='D' || c=='E' || c=='J' || c=='L' || c=='M' || c=='O' || c=='T' || c=='W')
				s.push_back(c+32);*/
		}
		ss=s.size();
		WA=new int[ss];
		for (j=ss-1; j>=0; --j)
			WA[j]=0;
		for (j=ss-1; j>=0; --j)
			if (s.at(j)=='m')
				WA[j]=1;
		for (i=strlen(welcstr)-2; i>=0; --i) {
			sc=welcstr[i];
			sum=0;
			for (j=ss-1; j>=0; --j) {
				sum+=WA[j];
				sum=sum%10000;
				if (s.at(j)==sc)
					WA[j]=sum;
				else
					WA[j]=0;
			}
		}
		sum=0;
		for (j=ss-1; j>=0; --j)
			sum+=WA[j];
		fprintf(g,"Case #%d: %04ld\n",n+1,sum%10000);
		delete WA;
		s.empty();
		s.clear();
	}
	fclose(f);
	fclose(g);
	return 0;
}