#include <cstdio>
#include <string>
#include <algorithm>

using namespace std;

int nas[100];
int nae[100];
int nbs[100];
int nbe[100];

int partition(int data_array[],int start,int end)
{
	int x = data_array[end];
	int index = start -1;
	int help;
	//int j;
	for(int j=start; j<end; j++)
	{
		if(data_array[j] <= x)
		{
			index++;
			help = data_array[index];
			data_array[index] = data_array[j];
			data_array[j] = help;
		}
	}
	help = data_array[index+1];
	data_array[index+1] = data_array[end];
	data_array[end] = help;
	return index+1;
}

void quick_sort(int data_array[], int start, int end)
{
	if(start<end)
	{
		int p = partition(data_array,start,end);
		quick_sort(data_array,start,p-1);
		quick_sort(data_array,p+1,end);
	}
}

int count_num(int data[],int& begin,int n,int s,int e)
{
	int i=begin;
	int result = 0;
	for(;i<n;i++)
	{
		if(data[i]>s&&data[i]<=e)
			result++;
		if(data[i]>e)
			break;
	}
	begin = i;
	return result;
}

int count(int start[],int s,int end[],int e)
{
	int result =0;
	int i,j;
	int left=0;
	int help=-1;
	int begin =0;

	int temp;
	
	for(i=0;i<s;i++)
	{
		temp = count_num(end,begin,e,help,start[i]);
		if(temp+left ==0)
			result++;
		else if(temp+left-1 >=0)
			left = temp+left-1;
		else
			left = 0;
		help = start[i];
	}
	return result;
}

int main()
{
	int N;
	int T;
	int NA,NB;
	int i,j;
	int h,m;

	int a,b;

	scanf("%d",&N);

	for(i=0;i<N;i++)
	{
		scanf("%d%d%d",&T,&NA,&NB);

		for(j=0;j<NA;j++)
		{
 			scanf("%d:%d",&h,&m);
			nas[j]=h*60+m;
			scanf("%d:%d",&h,&m);
			nae[j]=h*60+m+T;
		}
		for(j=0;j<NB;j++)
		{
			scanf("%d:%d",&h,&m);
			nbs[j]=h*60+m;
			scanf("%d:%d",&h,&m);
			nbe[j]=h*60+m+T;
		}

		quick_sort(nas,0,NA-1);
		quick_sort(nae,0,NA-1);
		quick_sort(nbs,0,NB-1);
		quick_sort(nbe,0,NB-1);
		
		a = count(nas,NA,nbe,NB);
		b = count(nbs,NB,nae,NA);

		printf("Case #%d: %d %d\n",i+1,a,b);

		
	}

}