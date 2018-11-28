#include <stdio.h>
#include <sstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <iomanip>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <cassert>
#include <string.h>
using namespace std;
#pragma comment(linker, "/STACK:20000000")

typedef vector<int> vi; 
#define sz(a) int((a).size()) 
#define all(c) (c).begin(),(c).end() 

string problem_name = "A-large(2)";

void init(){
  freopen((problem_name+".in").c_str(),"rt",stdin);
  freopen((problem_name+".out").c_str(),"wt",stdout);
}

int u[256],mas[200];
char s[100];

int main()
{

	init();

	int n;
	scanf("%d\n",&n);
	int cas=1;

	for (int i=0;i<n;i++)
	{
		gets(s);
		int len=strlen(s);
		int z=0,mx=1;
		memset(u,-1,sizeof(u));
		for (int i=0;i<len;i++)
		{
			if (u[s[i]]!=-1) mas[i]=u[s[i]]; else
			{
				if (i && !z)
				{
					z=1;
					u[s[i]]=0;
					mas[i]=0;
				} else
				{
					u[s[i]]=mx;
					mas[i]=mx;
					mx++;				
				}			
			}		
		}
		if(mx==1) mx++;
		long long res=0;
		for (int i=0;i<len;i++)
			res=res*mx + mas[i];
		printf("Case #%d: %lld\n",cas,res);
		cas++;

	
	}


  

   return 0; 
}
