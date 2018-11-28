#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <cstdio>
#include <climits>
#include <cmath>
using namespace std;

bool search(char field[51][51],int R,int C)
{
	for(int j=0;j<R-1;j++)
	{
		for(int i=0;i<C-1;i++)
		{
			if(field[j][i]!='#')
				continue;
			
			if(field[j  ][i  ]!='#') return false;
			if(field[j  ][i+1]!='#') return false;
			if(field[j+1][i  ]!='#') return false;
			if(field[j+1][i+1]!='#') return false;
			
			field[j  ][i  ]='/';
			field[j  ][i+1]='\\';
			field[j+1][i  ]='\\';
			field[j+1][i+1]='/';
		}
	}
	for(int j=0;j<R;j++)
	for(int i=0;i<C;i++)
		if(field[j][i]=='#')
			return false;
	return true;
}

int main()
{
	int T; cin>>T;
	for(int ds=1;ds<=T;ds++)
	{
		int R,C; cin>>R>>C;
		
		char field[51][51]={0};
		for(int j=0;j<R;j++)
		for(int i=0;i<C;i++)
			cin>>field[j][i];
		
		bool ans=search(field,R,C);
		printf("Case #%d:\n",ds);
		if(ans==false)
		{
			printf("Impossible\n");
			continue;
		}
		
		for(int j=0;j<R;j++)
		{
			for(int i=0;i<C;i++)
				printf("%c",field[j][i]);
			printf("\n");
		}
	}
	return 0;
}
