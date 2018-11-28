#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <stack>
#include <string>
using namespace std;


typedef long long cybers ;


#define MAX_SIZE 1000
#define INFINITY 1000000000
#define PI 3.1415926

#define PRT_F(a,b) cout<<"Case #"<<a<<": "<<b<<endl;


int main()
{
	char tchar;
	int tvalue;

	freopen("B-large.in","rt",stdin); freopen("B-large.out","wt",stdout);
	
	int amount = 0;
	cin>>amount;
	int p = 0;
	char COMBINES[40][3];
	char OPPOSED[30][2];
	char MAINSTRING[105];
	char ISINSTRING[30];
	int ISINSTRINGPOS[30];
	int selectedlast;
	while (p<amount)
		{
		if (p == 59)
			{
			int t=0;
			}
		memset(MAINSTRING,0,sizeof(MAINSTRING));
		memset(ISINSTRING,0,sizeof(ISINSTRING));
		memset(ISINSTRINGPOS,0,sizeof(ISINSTRINGPOS));
		int CombineElementCount = 0;
		int OpposedElementCount = 0;
		int GeneralStringElement = 0;
		cin>>CombineElementCount;
		for (int i=0;i<CombineElementCount;++i)
			{
			cin>>COMBINES[i][0]>>COMBINES[i][1]>>COMBINES[i][2];
			}
		cin>>OpposedElementCount;
		for (int i=0;i<OpposedElementCount;++i)
			{
			cin>>OPPOSED[i][0]>>OPPOSED[i][1];
			}
		cin>>GeneralStringElement;
		for (int i=0;i<GeneralStringElement;++i)
			{
			cin>>MAINSTRING[i];
			}
		MAINSTRING[GeneralStringElement] = '\0';

		string workingstr(MAINSTRING);
		string result="";
		int currentpointer = 0;
		while (currentpointer<GeneralStringElement)
			{
			
			bool stopflag = false;
			if (result.size()>0)
				for (int i=0;i<CombineElementCount;i++)
				{
					char lastres = result[result.size()-1];
					if (workingstr[currentpointer] == COMBINES[i][0] && lastres == COMBINES[i][1]||
							lastres == COMBINES[i][0] && workingstr[currentpointer] == COMBINES[i][1])
							{
							
							result.erase((result.end()-1));
							for (int k = 0;k < OpposedElementCount; k++)
								if (ISINSTRING[k] == lastres && (ISINSTRINGPOS[k] -1 == int (result.size()) ))  
									{
										ISINSTRING[k] = '\0';
										ISINSTRINGPOS[k] = 0;
									}//*/
							result.push_back(COMBINES[i][2]);
							currentpointer++;
							stopflag = true;
							break;
							}

					
				//if (stopflag) continue;
				
				}
			/////////////////////
				if (!stopflag)
				{
				for (int i=0;i<OpposedElementCount;i++)
					{
					if (workingstr[currentpointer] == OPPOSED[i][0])
						{
							if (ISINSTRING[i]==OPPOSED[i][1])
								{
								result.clear();
								currentpointer++;
								memset(ISINSTRING,0,sizeof(ISINSTRING));
								memset(ISINSTRINGPOS,0,sizeof(ISINSTRINGPOS));
								stopflag = true;
								break;
								}
							else
								if (ISINSTRING[i]=='\0')
								{
									ISINSTRING[i]=OPPOSED[i][0];
									ISINSTRINGPOS[i] = result.size() + 1;

								}
						}
					if (workingstr[currentpointer] == OPPOSED[i][1])
						{
							if (ISINSTRING[i]==OPPOSED[i][0])
								{
								result.clear();
								currentpointer++;
								memset(ISINSTRING,0,sizeof(ISINSTRING));
								memset(ISINSTRINGPOS,0,sizeof(ISINSTRINGPOS));
								stopflag = true;
								break;
								}
							else
								if (ISINSTRING[i]=='\0')
								{
									ISINSTRING[i]=OPPOSED[i][1];
									ISINSTRINGPOS[i] = result.size() +1;
								}
						}

					}
			/////////////////////
				if (!stopflag)
					{
						result.push_back(workingstr[currentpointer]);
						currentpointer++;
					}
				}
			}

		p++;
		cout<<"Case #"<<p<<": [";
		 if (result[0]!='\0') cout<<result[0];
		for (int i=1;i<result.size();++i)
			 if (result[i]!='\0') cout<<", "<<result[i];
		cout<<"]"<<endl;
		//out result
		}
}

