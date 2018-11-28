#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <string>
using namespace std;
void main()
{
	int T;
	int i,j;
	string S[40];
	string Q="yhesocvxduiglbkrztnwjpfmaq";
	scanf("%d",&T);
	getline(cin,S[0]);
	for (i=0;i<T;i++) getline(cin,S[i]);
	for (i=0;i<T;i++) for (j=0;j<S[i].size();j++)
	{
		if (S[i][j]>='a' && S[i][j]<='z') S[i][j]=Q[S[i][j]-'a'];
	}
	for (i=0;i<T;i++) printf("Case #%d: %s\n",i+1,S[i].c_str());
	getch();
}