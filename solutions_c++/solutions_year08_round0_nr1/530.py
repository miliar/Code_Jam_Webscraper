#include <stdio.h>
#include <stdlib.h>

#include <string>
#include <iostream>

//#include <backward/hash_map>
//using namespace __gnu_cxx;

#include <map>

using namespace std;

int main()
{
	int i,j,k,l,m,n;
	int testId, nTests;

	scanf("%d", &nTests);
	for(testId=1;testId<=nTests;testId++)
	{
		//scanf("%s %s", p1, p2);
		//XXX  -- Read input --  XXX
		int nEngines;
		scanf("%d", &nEngines);
		map<string,int> e;
		string *eng[nEngines];

	    char str[1024];

        char *tstr;


		for(i=0;i<nEngines;i++)
		{
        	gets(str);
        	if (str[0]=='\0')
            	gets(str);
			eng[i]=new string(str);
			//e[*eng[i]]=0;
			e[str]=0;
		}

		#ifdef DEBUG
		for(i=0;i<nEngines;i++)
			cout << *eng[i] << endl;
		#endif

		int nQueries;
		scanf("%d", &nQueries);
		string *que[nQueries];
		
		//char prevEngine[1024];
		//prevEngine[0]='\0';
		string prevEngine("");
		int nDone=0;
		int nSwitches=0;
		for(i=0;i<nQueries;i++)
		{
        	gets(str);
        	if (str[0]=='\0')
            	gets(str);
			que[i]=new string(str);

			//cout << *que[i] << endl;
			e[*que[i]]++;
			if(e[*que[i]] == 1)
				nDone++;
			if(nDone == nEngines)
			{
				nSwitches++;
				prevEngine=*que[i];
				//cout << "nDone " << nDone << ":" << prevEngine << endl;
				
				nDone=0;
				for(j=0;j<nEngines;j++)
					e[*eng[j]] = 0;
				e[*que[i]]++;
				if(e[*que[i]] == 1)
					nDone++;
			}

		}
		//XXX  -- Process input --  XXX







		//XXX  -- Print output --  XXX
		printf("Case #%d: %d\n",testId, nSwitches);

	}

	return 0;
}
