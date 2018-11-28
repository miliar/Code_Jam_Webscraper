#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<stack>
#include<queue>
#include<vector>
#include<sstream>
#include<utility>
#include<string>
using namespace std;

char arr[52][52];
int r,c;
bool fil(int i,int j)
{	
	if(i+1<r&&arr[i+1][j]=='#'){arr[i+1][j]='\\';}
	else{return false;}
	if(j+1<c&&arr[i][j+1]=='#'){arr[i][j+1]='\\';}
	else{return false;}
	if(i+1<r&&j+1<c&&arr[i+1][j+1]=='#'){arr[i+1][j+1]='/';}
    else{return false;}
	return true;
}

int main()
{
	int t,cas=0,i,j,flag;
	bool istrue;
//	freopen("A-large.in","r",stdin);
//	freopen("a.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&r,&c);
		for(i=0;i<r;i++){scanf("%s",arr[i]);}
		flag=1;
		istrue=true;
		for(i=0;i<r;i++)
		{
			for(j=0;j<c;j++)
			{
				if(arr[i][j]=='#'){arr[i][j]='/';istrue=fil(i,j);}
				if(istrue==false){flag=0;break;}
			}
			if(istrue==false){break;}
		}
		printf("Case #%d:\n",++cas);
		if(flag==0){printf("Impossible\n");}
		else
		{
			for(i=0;i<r;i++){printf("%s\n",arr[i]);}
		}
	}
	return 0;
}