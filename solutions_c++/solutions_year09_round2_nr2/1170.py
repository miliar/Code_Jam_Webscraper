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
	int Test;
	scanf("%d",&Test);
	getchar();
	for(int i=1;i<=Test;i++){
		char input[22];
		gets(input);
		printf("Case #%d: ",i);
		int num[21],len;
		len=strlen(input);
		for(int j=len-1;j>=0;j--)
			num[j]=(int)(input[j])-48;
		bool found=false;
		for(int j=len-1;j>0;j--){
			if(num[j]>num[j-1]){
				sort(num+j,num+len);
				for(int k=j;k<len;k++){
					if(num[k]>num[j-1]){
						int temp=num[k];
						num[k]=num[j-1];
						num[j-1]=temp;
						break;
					}
				}
				found=true;
				break;
			}
		}
		if(found){
			for(int j=0;j<len;j++)
				printf("%d",num[j]);
		}
		else{
			sort(num,num+len);
			int pos=0;
			for(int j=0;j<len;j++){
				if(num[j]!=0)
					break;
				pos++;
			}
			printf("%d0",num[pos]);
			for(int j=0;j<pos;j++)
				printf("0");
			for(int j=pos+1;j<len;j++)
				printf("%d",num[j]);
		}
		cout<<endl;
	}
}
