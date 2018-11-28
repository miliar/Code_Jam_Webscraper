#include<iostream>
#include <vector>
#include <stack>
#include <map>
#include <queue>
#include <list>
#include <algorithm>
#include <set>
#include <cstring>
#include<string.h>
#include <cmath>
#include<math.h>
#include <cassert>
#include <sstream>
#include <climits>
#include <deque>
#include <fstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()
{
	int noi;
	scanf("%d",&noi);
	getchar();
	for(int i=1;i<=noi;i++){
		long int time=0,mul=1;
		char Script[65];
		gets(Script);
		int len,length=0,Base=0;
		len=strlen(Script);
		int arr[len];
		char Mark[len];
		for(int j=0;j<len;j++){
			if(j==0){
				arr[length]=1;
				Mark[length++]=Script[j];
			}
			else{
				bool found=false;
				for(int k=0;k<length;k++){
					if(Mark[k]==Script[j]){
						Mark[length]=Script[j];
						arr[length++]=arr[k];
						found=true;
						break;
					}
				}
				if(not found){
					Mark[length]=Script[j];
					arr[length++]=Base++;
					if(Base==1)
						Base=2;
				}
			}
		}
		if(Base==0)
			Base=2;
		printf("Case #%d: ",i);
		for(int j=length-1;j>=0;j--){
			time+=arr[j]*mul;
			mul*=Base;
		}
		printf("%ld\n",time);
	}
}
