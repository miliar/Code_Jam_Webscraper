#include <stdio.h>
#include <algorithm>

using namespace std;

class time
{
public:
	int hour,minute;
	bool operator < (const time & s);
};

bool time::operator <(const time & t)
{ 
	if(hour<t.hour)	return true;
	if(hour==t.hour&&minute<t.minute)	return true;
	return false;
}

class node
{
public:
	time begin,end;
	int flag;			//0: A->B 1:B->A
};

bool cmp( node &s , node & t)
{
	return s.begin<t.begin;
}

node array[300];
time queA[200],queB[200];
int lenA,lenB;

int main()
{
//	freopen("small.txt","w",stdout);
	freopen("large.txt","w",stdout);
	int i,j,k,n,turn;
	scanf("%d",&n);
	for(int N=1;N<=n;N++)
	{
		scanf("%d",&turn);
		int na,nb;
		scanf("%d %d ",&na,&nb);
		for(i=0;i<na;i++)
		{
			scanf("%d:%d %d:%d",&array[i].begin.hour,&array[i].begin.minute,&array[i].end.hour,&array[i].end.minute);
			array[i].flag=0;
		}
		for(i=na;i<na+nb;i++)
		{
			scanf("%d:%d %d:%d",&array[i].begin .hour,&array[i].begin.minute,&array[i].end.hour,&array[i].end.minute);
			array[i].flag=1;
		}
		sort(array,array+na+nb,cmp);
		lenA=lenB=0;
		int numA=0,
			numB=0;
		for(i=0;i<na+nb;i++)
		{
			int found=false;
			if(array[i].flag==0)	//A->B
			{
				for(j=0;j<lenA;j++)
				{
					if(!(array[i].begin<queA[j]))
					{
						for(k=j;k<lenA-1;k++)
							queA[k]=queA[k+1];
						lenA--;
						found=true;
						break;
					}
				}
				if(!found)
					numA++;
				array[i].end.minute+=turn;
				if(array[i].end.minute>=60)
				{
					array[i].end.minute-=60;
					array[i].end.hour+=1;
				}
				queB[lenB++]=array[i].end;
			}
			else
			{
				for(j=0;j<lenB;j++)
				{
					if(!(array[i].begin<queB[j]))
					{
						for(k=j;k<lenB-1;k++)
							queB[k]=queB[k+1];
						lenB--;
						found=true;
						break;
					}
				}
				if(!found)
					numB++;
				array[i].end.minute+=turn;
				if(array[i].end.minute>=60)
				{
					array[i].end.minute-=60;
					array[i].end.hour+=1;
				}
				queA[lenA++]=array[i].end;
			}
		}
		printf("Case #%d: %d %d\n",N,numA,numB);
	}
	return 0;
}