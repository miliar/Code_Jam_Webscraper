#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

char vals[26];

void setvals(string s1, string s2)
{
	stringstream sin1(s1);
	stringstream sin2(s2);
	
	char a,b;
	
	while(sin1 >> a)
	{
		sin2 >> b;
		
		vals[a-'a']=b;
	}
	
	return;
	
}

void makevals()
{
	string s1= "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	string s2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	string s3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	string t1= "our language is impossible to understand";
	string t2="there are twenty six factorial possibilities";
	string t3="so it is okay if you want to just give up";
	
	setvals(s1,t1);
	setvals(s2,t2);
	setvals(s3,t3);
	setvals("q","z");
	
	setvals("z","q"); //only possible left
	
	for(int i=0; i<26; i++)
	{
		if(vals[i]==0)
		{
			cout << i << " ";
		}
	}
	cout << endl;
	
	for(int i=0; i<26; i++)
	{
		int j=0;
		for(j=0; j<26; j++)
		{
			if(vals[j]=='a'+i)
				break;
		}
		if(j==26)
		{
			cout << i << " ";
		}
	}
	cout << endl;
}	


int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	makevals();
	getline(fin,s);
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		int m;
		
		
		getline(fin,s);
		
		string ans(s.size(),' ');
		
		
		for(i=0; i<s.size(); i++)
		{
			if(s[i]!=' ')
			{
				ans[i]=vals[s[i]-'a'];
			}
		}
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

