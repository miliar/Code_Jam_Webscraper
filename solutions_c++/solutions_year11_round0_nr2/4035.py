#include <iostream>
#include <fstream>
#include <algorithm>
#include <list>
#include <vector>
#include <stdlib.h>

using namespace std;

char mainS[100], replS[36][3], termS[28][2], rezS[100];

int mainN, replN, termN;
int rezCur=0;

int checkRepl()
{
	if(rezCur>1 && replN!=0)
		for(int i=0;i<replN;i++)
			if(((rezS[rezCur-2]==replS[i][0]) && (rezS[rezCur-1]==replS[i][1])) || ((rezS[rezCur-2]==replS[i][1]) && (rezS[rezCur-1]==replS[i][0])))
			{
				rezS[rezCur-1]=0;
				rezS[rezCur-2]=replS[i][2];
				rezCur--;
				return 1;
			}

	return 0;
}

int checkTerm()
{
	if(termN!=0)
		for(int i=0;i<rezCur-1;i++)
			for(int j=0;j<termN;j++)
				if((rezS[i]==termS[j][0] && rezS[rezCur-1]==termS[j][1]) || (rezS[i]==termS[j][1] && rezS[rezCur-1]==termS[j][0]) )
				{
					memset(rezS,0,100);
					rezCur=0;
					return 1;
				}

	return 1;
}

int main()
{
	int tn;
	ifstream in("c:\\B-small-attempt0.in");
	ofstream out("c:\\B-small.out");

	in>>tn;
	for(int test=0;test<tn;test++)
	{
		memset(rezS,0,100);
		rezCur=0;

		in>>replN;
		for(int i=0;i<replN;i++)
			in>>replS[i];

		in>>termN;
		for(int i=0;i<termN;i++)
			in>>termS[i];

		in>>mainN;
		//for(int i=0;i<replN;i++)
		in>>mainS;


		//rezS[rezCur++]=mainS[0];
		
		for(int i=0;i<mainN;i++)
		{
			if(rezCur==0)
			{
				rezS[rezCur++]=mainS[i];
				continue;
			}

			rezS[rezCur++]=mainS[i];

			while(checkRepl());
			checkTerm();
		}

		if(rezCur==0)
			out<<"Case #"<<test+1<<": []"<<endl;
		if(rezCur==1)
			out<<"Case #"<<test+1<<": ["<<rezS[0]<<"]"<<endl;
		if(rezCur>1)
		{
			out<<"Case #"<<test+1<<": [";
			for(int j=0;j<rezCur-1;j++)
				out<<rezS[j]<<", ";
			out<<rezS[rezCur-1]<<"]"<<endl;
		}

	}
	

	return 0;
}