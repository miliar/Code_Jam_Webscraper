#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>

using namespace std;

//const int maxn = 1000;
//int numbers[maxn];
//int n;

int combs;
vector<char>comb1;
vector<char>comb2;
vector<char>combout;

int opps;
vector<char>opp1;
vector<char>opp2;

void reset()
{
	comb1.clear();
	comb2.clear();
	combout.clear();
	opp1.clear();
	opp2.clear();
}

void print(vector<char>&mylist)
{
	printf("[");
	if(mylist.size()>0)
	{
		printf("%c",mylist[0]);
        	for(int k=1;k<mylist.size();k++)
                	printf(", %c",mylist[k]);
 	}
        printf("]");
}
 
void read() {
	int k;
	char c;
	scanf("%d",&combs);
	for(k=0;k<combs;k++)
	{
		scanf("%c",&c);
		scanf("%c",&c);	
		comb1.push_back(c);
		scanf("%c",&c);
		comb2.push_back(c);
		scanf("%c",&c);
		combout.push_back(c);
	}
	scanf("%d",&opps);
	for(k=0;k<opps;k++)
	{
		scanf("%c",&c);
		scanf("%c",&c);
		opp1.push_back(c);
		scanf("%c",&c);
		opp2.push_back(c);
	}

//printf("n:%d\n",n);
//printf("i:%d numbers[i]:%d\n",i,numbers[i]);

//print(comb1);
//print(comb2);
//print(combout);
//print(opp1);
//print(opp2);
}

int contains(vector<char>&mylist, char &c)
{
	for(int k=0;k<mylist.size();k++)
		if(mylist[k]==c)
			return 1;
	return 0;
}

int main()
{
	int i,t;
	vector<char>list;
	char cur, last;
	int N, c;
	scanf("%d",&t);
	for(i = 1; i<=t; i++)
	{
		list.clear();
		reset();
		printf("Case #%d: ", i);
		read();
		scanf("%d", &N);
		scanf("%c", &cur); //throwaway space
		scanf("%c", &cur);
		list.push_back(cur);		
		for(int k=1;k<N;k++)
		{
			last = cur;
			scanf("%c", &cur);
			list.push_back(cur);
//printf("\n");
//print(list);
//printf("processing\n");
			//combine
			for(c=0;c<combs;c++)
			{
				if((comb1[c]==cur&&comb2[c]==last) ||
				   (comb1[c]==last&&comb2[c]==cur))
				{
					list.pop_back();
					list.pop_back();
					list.push_back(combout[c]);
					if(list.size()>0)
						cur = list.back();
					else
						cur = ' ';
				}

			}
			//opposed			
			for(c=0;c<opps;c++)
			{
			if(list.size()>0)
				if( (list.back()==opp1[c] && contains(list,opp2[c])) ||
				    (list.back()==opp2[c] && contains(list,opp1[c])) )
					{	
						list.clear();
						cur = ' ';
					}
			}
//print(list);
		}
		print(list);
		printf("\n");
	}
	return 0;
}
