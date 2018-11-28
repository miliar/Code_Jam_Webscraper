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
int main()
{
freopen("out.txt","w",stdout);
freopen("in.txt","r",stdin);
int t;

scanf("%d",&t);

int n,tmp;
float z;
for(int j=1; j<=t; j++){
z=0;
scanf("%d",&n);
for(int i=1;i<=n;i++){
	cin>>tmp;
	if(i!=tmp)z++;}
printf("Case #%d: %.6f\n",j,z);
}
return 0;}
