/*
name:ProblemBMagicka
By Tony
2011-5-7 ионГ11:25:33
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <functional>
#include <string>
#include <cmath>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <vector>
#include <stack>
#include <queue>

using namespace std;\
const int maxn=110;

char cstr[50][10];
char dstr[50][10];
char nstr[maxn];
int st,ed;

char ansstr[maxn];


int finds(char x,char y,int sn,char str[50][10]){
	int i;
	for(i=0;i<sn;i++)
		if ( (x==str[i][0] && y==str[i][1])||
			 (x==str[i][1] && y==str[i][0])){
			return i;
		}
	return -1;
}



int main()
{
#ifndef ONLINE_JUDGE
    freopen("ProblemBMagicka","r",stdin);
    freopen("ProblemBMagicka.out","w",stdout);
#endif
    int cas,icas=0;
    int c,d,n;
    int i,j;
    cin>>cas;
    while(cas--){
    	icas++;
    	cin>>c;
    	for(i=0;i<c;i++)
    		cin>>cstr[i];
    	cin>>d;
    	for(i=0;i<d;i++)
    		cin>>dstr[i];
    	cin>>n;
    	cin>>nstr;

    	st=ed=0;
    	//combination & oppose
    	int fc;
    	//ansstr[ed++]=nstr[0];
    	for(i=0;i<n;i++)
    	{
    		if(ed==0){
    			ansstr[ed++]=nstr[i];
    			continue;
    		}


    		fc=finds(ansstr[ed-1],nstr[i],c,cstr);
    		if(fc==-1){
    			ansstr[ed++]=nstr[i];
    			for(j=0;j<ed-1;j++)
    				if(finds(ansstr[j],nstr[i],d,dstr)!=-1)
    				{
    					ed=0;
    					break;
    				}
    		}
    		else
    			ansstr[ed-1]=cstr[fc][2];




    	}



    	//output
    	printf("Case #%d: [",icas);
    	if(ed){
    	printf("%c",ansstr[st++]);  //Case #1: [E, A]
    	for(;st<ed;){
    		printf(", %c",ansstr[st++]);
    	}
    	}
    	printf("]\n");






    }


	return 0;
}
