#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <iterator>
#include <iostream>
#include <functional>
#include <sstream>
#include <numeric>
#include <list>
#include <map>

using namespace std;

int main()
{
	FILE *in=fopen("S:/input.in.txt","r");
    FILE *out=fopen("S:/output.txt","w");
	int T = 0;
    fscanf(in,"%d",&T); 
	
    for (int ii=0;ii < T ;ii++)
    {
		vector<string> v;
		bool isEnd = false;
		for (int i=0;i<4; i++)
		{
			//string s;
			char s1[5];
			fscanf(in,"%s",s1);
			s1[4]='\0';
			if ( isEnd ) continue;
			string s = s1;
			if ( s == "XXXX" || s == "XXXT" || s=="XXTX" || s=="XTXX" || s=="TXXX" )
			{
				fprintf(out,"Case #%d: X won\n",ii+1); 
				isEnd = true;
			}
			else if ( s == "OOOO" || s == "OOOT" || s=="OOTO" || s=="OTOO" || s=="TOOO"  )
			{
				fprintf(out,"Case #%d: O won\n",ii+1); 
				isEnd = true;
			}
			v.push_back(s);
		}
		if ( isEnd ) continue;

		bool isDot=false;
		for (int i=0;i<4 && !isEnd;i++)
		{
			string s;
			for (int j=0;j<4 && !isEnd;j++)
			{
				if ( v[j][i] == '.' )
				{
					isDot = true;
					break;
				}
				s.push_back(v[j][i]);
			}
			if ( s == "XXXX" || s == "XXXT" || s=="XXTX" || s=="XTXX" || s=="TXXX" )
			{
				fprintf(out,"Case #%d: X won\n",ii+1); 
				isEnd = true;
				break;
			}
			else if ( s == "OOOO" || s == "OOOT" || s=="OOTO" || s=="OTOO" || s=="TOOO"  )
			{
				fprintf(out,"Case #%d: O won\n",ii+1); 
				isEnd = true;
				break;
			}
		}
		if ( isEnd ) continue;
		char s1[5];
		s1[0]= v[0][0]; s1[1]=v[1][1];	s1[2]=v[2][2];	s1[3]=v[3][3];
		s1[4]='\0';
		string s = s1;
		if ( s == "XXXX" || s == "XXXT" || s=="XXTX" || s=="XTXX" || s=="TXXX" )
		{
				fprintf(out,"Case #%d: X won\n",ii+1); 
				continue;
		}
		if ( s == "OOOO" || s == "OOOT" || s=="OOTO" || s=="OTOO" || s=="TOOO"  )
		{
				fprintf(out,"Case #%d: O won\n",ii+1); 
				continue;
		}			
		s = "";
		s1[0] = v[3][0]; s1[1]= v[2][1]; s1[2]=v[1][2]; s1[3]=v[0][3];s1[4]='\0';
		s=s1;
		if ( s == "XXXX" || s == "XXXT" || s=="XXTX" || s=="XTXX" || s=="TXXX" )
		{
				fprintf(out,"Case #%d: X won\n",ii+1); 
				continue;
		}
		if ( s == "OOOO" || s == "OOOT" || s=="OOTO" || s=="OTOO" || s=="TOOO"  )
		{
				fprintf(out,"Case #%d: O won\n",ii+1); 
				continue;
		}		
		if ( isDot )	fprintf(out,"Case #%d: Game has not completed\n",ii+1); 
		else fprintf(out,"Case #%d: Draw\n",ii+1);
	}
}