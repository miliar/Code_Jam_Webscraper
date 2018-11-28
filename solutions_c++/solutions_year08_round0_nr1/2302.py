#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <assert.h>
#include <map>

using namespace std;
//#define MYDBG


	void delN(char *s)
	{
		int n=strlen(s);
		if(s[n-1]=='\n')
			s[n-1]=0;
	}

#define INITED 1
#define VISITED 2
	struct stStr
	{
		char s[101];
	};
	
	//return -1 error,0~n id
	int bStrIsInVec(const stStr * pstStr,const char * s,int V_Size)
	{
		for (int i=0;i<V_Size;i++)
		{
			//if(s.compare(vec_s[i]))
			if(strcmp(s,pstStr[i].s)==0)
				return i;
		}

		return -1;
	}

	int main()
	{
		int N,S,Q,i,j;
		char line[200];
		//map <string> map_s;
		char *pvisited;
		stStr * pstStr = 0;

		scanf("%d\n",&N);
		for (i=0;i<N;i++)
		{
			scanf("%d\n",&S);
#ifdef MYDBG
			printf("S %d\n",S);///
#endif
			//vec_s.resize(S);
			pstStr = new stStr[S];
			pvisited = new char[S];
			memset(pvisited,0,S*sizeof(char));

			for (j=0;j<S;j++)
			{
				fgets(line,101,stdin);
				delN(line);

				//map_s[line] = INITED;
				//vec_s.push_back(line);
#ifdef MYDBG
				assert(strlen(line)<100);
				printf("readline %s\n",line);
#endif
				strcpy(pstStr[j].s,line);
			}
			scanf("%d\n",&Q);
#ifdef MYDBG
			printf("Q %d\n",Q);///
#endif
			int Num = 0;
			int VisitNum = 0;
			for (j=0;j<Q;j++)
			{
				//for(int k=0;k)
				fgets(line,101,stdin);
				delN(line);
				int id = bStrIsInVec(pstStr,line,S);
#ifdef MYDBG
				assert(id>=0);
				printf("%s idx %d\n",line,id);
#endif
				if (!pvisited[id])
				{
					pvisited[id] = 1;
					VisitNum ++;
				}
				if(VisitNum == S)
				{
					Num ++;
					VisitNum = 1;
					memset(pvisited,0,S*sizeof(char));
					pvisited[id]=1;
#ifdef MYDBG
					printf("-----%d---\n",Num);
#endif
				}
			}
			
			printf("Case #%d: %d\n",i+1,Num);
			delete []pvisited;
			delete []pstStr;
		}
		return 0;
	}

