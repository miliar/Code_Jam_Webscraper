#include <fstream>
#include <string>
#include <vector>
using namespace std;

char currentB[15][26];
bool legal[15][26];
int len, numD, numTest;
char used[18];
int total;
bool found;
bool found3;
int cnt;
char dict[5000][15];
bool works;
bool subWork;

bool check()
{
		
	for(int a=0; a<numD; a++)
	{
		found3=false;
		for(int b=0; b<len && found3==false; b++)
			if(used[b]!=dict[a][b])	
				found3=true;
		if(found3==false)
			return true;
	}
	return false;
}

void dfs(int a)
{
	if(a==len)
	{
		//for(int i=0; i<len; i++)
		//	printf("%c",used[i]);
		//printf("\n");
		if(check())
		{
			//printf("hurrah\n");
			total++;
		}
	}
	works = false;
	for(int i=0; i<numD && works == false; i++)
	{
		subWork=true;
		for(int j=0; j<a && subWork == true; j++)
		{
			if(dict[i][j]!=used[j])
			{
				subWork = false;
			}
		}
		if(subWork)
			works=true;
	}	

	if(works)
	{
		for(int i=0; i<26 && currentB[a][i]!='\0'; i++)
		{
			used[a]=currentB[a][i];
			dfs(a+1);
		
		}		
	}
}



int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small.out","w",stdout);
	
	scanf("%d %d %d", &len, &numD, &numTest);
	
	for(int a=0; a<15; a++)for(int b=0; b<26; b++)legal[a][b]=false;

	char temp;
	scanf("%c",&temp);
	for(int i=0; i<numD; i++)
		for(int a=0; a<len+1; a++)
			
			if(a<len)
			{
				scanf("%c",&dict[i][a]);
				legal[a][(int)(dict[i][a]-'a')]=true;
			}
			else
				scanf("%c",&temp);
	
	char current;
	
	
	bool found1,found2;


	for(int test=0; test<numTest; test++)
	{
		total=0;
		

		for(int a=0; a<len; a++)
			for(int let=0; let<26; let++)
				currentB[a][let]='\0';


		for(int a=0; a<len; a++)
		{
			cnt=0;
			found1 = false;
			found2 = false;
			while(found2!=true)
			{
				
				scanf("%c",&current);
				//printf("%c",current);
				if(current==')')
					found2=true;
				else if(current=='(')
					found1=true;
				else if(found1==false)
				{
					currentB[a][cnt]=current;
					found2=true;
				}
				else if(legal[a][(int)(current - 'a')])
				{
					currentB[a][cnt]=current;
					cnt++;
				}		
			}
			
		}
		dfs(0);
		//for(int a=0; a<len; a++)
		//{
		//	for(int b=0; b<26; b++)
		//		if(currentB[a][b]=='\0')
		//			printf("%d",b);
		//	printf("\n");		
		//}
		
		scanf("%c",&current);
		printf("Case #%d: %d\n",test+1,total);
	}
	return 0;
}





