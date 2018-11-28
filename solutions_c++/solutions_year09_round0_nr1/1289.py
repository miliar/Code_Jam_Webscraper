#include<stdio.h>
#include<vector>

using namespace std;

typedef struct{
	char word[20];
}b_string;

int main()
{
	int L,D,N;
	vector<b_string> word_all;
	scanf("%d %d %d",&L,&D,&N);
	for(int i=0;i<D;i++)
	{
		b_string temp;
		scanf("%s",temp.word);
		word_all.push_back(temp);
	}
	for(int i=0;i<N;i++)
	{
		char pat[450];
		scanf("%s",pat);
		short patt[15][26]={0};
		short k = 0; 
		short p = 0;
		for(int j=0;pat[j] != '\0';j++)
		{
			if(pat[j] == '(')
				k = 1;
			else if(pat[j] == ')')
			{
				k = 0;p++;
			}
			else
			{
				patt[p][pat[j]-'a']++;
				if(k == 0) p++;
			}
		}
		//for(int j=0;j)
		int count = 0;
		for(int j=0;j<D;j++)
		{
			k = 0;
			for(int m=0;m<L;m++)
			{
				//printf("%d\n",patt[m][word_all[j].word[m]-'a']);
				if(patt[m][word_all[j].word[m]-'a'] == 0)
				{
				 k =1;	break;
				}
			}
			//printf("%d-- \n",k);
			if(k == 0)
				count++;
		}
		printf("Case #%d: %d\n",i+1,count);
	}
	return 0;
}
