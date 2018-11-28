#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
using namespace std;
int mas[101][2];
int main()
{
freopen("out.txt","w",stdout);
freopen("in.txt","r",stdin);
int mas[101][2];
char ch;
int t;
scanf("%d",&t);
for(int j=1; j<=t; j++){
int n,res=0,poso=1,posb=1,ostep=0,bstep=0,tmp;
scanf("%d",&n);
for (int i=0; i<n; i++){
scanf(" %c %d",&ch,&tmp);
mas[i][0]=tmp;
if(ch=='O')mas[i][1]=2;
if(ch=='B')mas[i][1]=1;
}
for (int i=0; i<n; i++){
	if(mas[i][1]==1){
		if(bstep>=abs(mas[i][0]-posb)) bstep=abs(mas[i][0]-posb);
		res+=abs(mas[i][0]-posb)-bstep+1;
		ostep+=abs(mas[i][0]-posb)-bstep+1;
		bstep=0;
		posb=mas[i][0];}
	if(mas[i][1]==2){
		if(ostep>=abs(mas[i][0]-poso)) ostep=abs(mas[i][0]-poso);
		res+=abs(mas[i][0]-poso)-ostep+1;
		bstep+=abs(mas[i][0]-poso)-ostep+1;
		poso=mas[i][0];
		ostep=0;}	
}

printf("Case #%d: %d\n",j,res);}
 return 0;}
