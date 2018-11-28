#include<stdio.h>
#include<string>
#include<queue>
using namespace std;
int main()
{
	//FILE* in = fopen("A-large-practice.in","r");	//¶óÁö 
	FILE* in = fopen("C-small-attempt0.in","r");	//½º¸ô
	FILE* out = fopen("output.out","w");
	int t;
	fscanf(in,"%d",&t);
	for(int test = 1; test <= t;test++)
	{
		int R,K,G;
		int answer =0;
		queue<int> Queue;
		fscanf(in,"%d %d %d",&R,&K,&G);
		for(int i = 0; i< G;i++)
		{
			int temp;
			fscanf(in,"%d",&temp);
			Queue.push(temp);
		}
		for(int i = 0; i < R;i++)
		{
			int j = 0;
			int person = 0;
			while(j < G)
			{
				
				int temp = Queue.front();
				if(person + temp <= K)
				{
					person += temp;
					Queue.pop();
					Queue.push(temp);
				}
				else
					break;
				j++;
			}
			answer += person;
		}
		fprintf(out,"Case #%d: %d\n",test,answer);
	}
	fclose(in);
	fclose(out);
	return 0;
}