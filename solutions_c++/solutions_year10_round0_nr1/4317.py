#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <cmath>
using namespace std;
typedef struct snapper{
	bool isPower;
	bool isOn;
}Snapper;
////
int testcase;
int N;
int K;
Snapper snappers[30];
void snap(){
	int i=0;
	for (i=0;i<N;i++)
	{
		if (snappers[i].isPower)
		{
			snappers[i].isOn=!snappers[i].isOn;
		}
	}
	for (i=1;i<N;i++)
	{
		if (snappers[i-1].isOn&&snappers[i-1].isPower)
		{
			snappers[i].isPower=true;
		}else{
			snappers[i].isPower=false;
		}
	}
}
bool Light(){
	bool isLight=true;
	int i=0;
	for (i=0;i<N;i++)
	{
		isLight=isLight&&(snappers[i].isOn);
	}
	return isLight;
}
int main(){
	int i;
	int j;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("snapper.out","wt",stdout);
	scanf("%d",&testcase);
	//printf("%d\n",testcase);
	for (i=0;i<testcase;i++)
	{
		scanf("%d %d",&N,&K);
		for (j=0;j<N;j++)
		{//init
			snappers[j].isOn=false;
			snappers[j].isPower=false;
			if (j==0)
			{
				snappers[j].isPower=true;
			}
		}
		for (j=0;j<K;j++)
		{
			snap();
		}
		printf("Case #%d: ",i+1);
		if (Light())
		{
			printf("ON\n");
		}else{
			printf("OFF\n");
		}
	}
	return 0;
}