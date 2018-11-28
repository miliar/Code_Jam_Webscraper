#include<iostream>
#include<stdio.h>
#include<cmath>
#include<string.h>
#include<string>
#include<math.h>
#include<stdlib.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include <utility>
#include <bitset>
#define pb push_back

using namespace std;

int n,surprise,check;
int arr[105];
int DP[110][110];

int maximum_non_surprising(int total){
if(total%3==0)
return total/3;
else
return total/3+1;
}
int maximum_surprising(int total){

if(total%3==2)
return total/3+2;
else
return total/3+1;
}


int findbest(int index, int surprise_left){
if(index==0){
if(surprise_left==0 && maximum_non_surprising(arr[0])>=check )
return 1;
else if(surprise_left==1 && maximum_surprising(arr[0])>=check )
return 1;
else if(surprise_left>1)
return -999999;
else return 0; 
}
if(DP[index][surprise_left]!=-1) return DP[index][surprise_left];
int max1=0,max2=0;

if(maximum_non_surprising(arr[index])>=check)
max1=1+findbest(index-1,surprise_left);
else
max1=findbest(index-1,surprise_left); 

if(surprise_left>0 && arr[index]>=2){
if(maximum_surprising(arr[index])>=check)
max2=1+findbest(index-1,surprise_left-1);
else
max2=findbest(index-1,surprise_left-1);

}
return DP[index][surprise_left] = max(max1,max2);
}



int main(){
int i,j,t;
 freopen("B-large.in","r",stdin);
 freopen("outkarthiN.txt","w",stdout);
scanf("%d",&t);
for(i=1;i<=t;i++){
memset(DP,-1,sizeof DP);
printf("Case #%d: ",i);
scanf("%d %d %d",&n,&surprise,&check);
for(j=0;j<n;j++)
scanf("%d",&arr[j]);

printf("%d\n",findbest(n-1,surprise));

}
return 0;
}
