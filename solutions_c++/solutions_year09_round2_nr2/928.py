#include<stdio.h>
#include<algorithm>
#include<string>
#include<vector>

using namespace std;

bool perm(vector<int> &num)
{
	int maxi=-1,maxj=-1;
	for(int i=0;i<24;i++) if(num[i] < num[i+1]) maxi = i;
	if(maxi == -1) return false;
	for(int i=0;i<25;i++) if(num[maxi] < num[i]) maxj = i;
	swap(num[maxi],num[maxj]);
	reverse(num.begin()+maxi+1,num.end());
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int round=0;round<T;round++)
	{
		vector<int> num;
		num.assign(25,0);
		char temp[25];
		scanf("%s",temp);
		int l = strlen(temp);
		for(int i=0;i<l;i++)
			num[24-i] = temp[l-i-1] - '0';
		perm(num);
		printf("Case #%d: ",round+1);
		int j=0;
		for(;j<25;j++) if(num[j] != 0) break;
		for(;j<25;j++) printf("%d",num[j]);
		printf("\n");
	}
	return 0;
}
