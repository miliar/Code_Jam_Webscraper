#include <stdio.h>
#include <stdlib.h>
#include <list>
#include <string>
#include <vector>

using namespace std;

int main()
{
	vector<string> languageStr;
	vector<string> syntaxStr;

	char* mChar;

	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A-large.out","w",stdout);

	int L,D,N;

	scanf("%d %d %d",&L,&D,&N);

	char maxChar[400];
	for(int tmp=0;tmp<D;tmp++)
	{
		scanf("%s",&maxChar);
		string s = maxChar;
		languageStr.push_back(s);
	}

	for(int caseNum=0;caseNum<N;caseNum++)
	{
		mChar = maxChar;
		memset(mChar,0,100);
		scanf("%s",&maxChar);

		syntaxStr.clear();

		int tmp = 0;
		bool begin = false;
		
		while(mChar[tmp] != '\0')
		{
			if(mChar[tmp] == '(')
			{
				if(tmp == 0)
				{
					mChar++;
				}else
				{
					mChar[tmp] = '\0';
					string s = "1";
					s += mChar;
					syntaxStr.push_back(s);

					//mChar += s.length()+1;
					mChar += s.length();
					tmp = 0;
				}
			}else if(mChar[tmp] == ')')
			{
				if(tmp == 0)
				{
					mChar++;
				}else
				{
					mChar[tmp] = '\0';
					string s = "0";
					s += mChar;
					syntaxStr.push_back(s);

					//mChar += s.length()+1;
					mChar += s.length();
					tmp = 0;
				}
			}
			else
			{
				tmp++;
			}
		}

		if(tmp != 0)
		{
			string s = "1";
			s += mChar;
			syntaxStr.push_back(s);
		}

		int result = 0;

		for(int tmp=0;tmp<D;tmp++)
		{
			string s = languageStr[tmp];

			int tmpIdx = 0;
			int idx=0;
			for(;idx<L;)
			{
				if(syntaxStr[tmpIdx][0] == '0')
				{
					int tmps = 0;
					if((tmps = syntaxStr[tmpIdx].find(s[idx])) > 0)
					{
						idx++;
						tmpIdx++;
					}else
					{
						break;
					}
				}else
				{
					//syntaxStr[tmpIdx].compare(
					
					if(syntaxStr[tmpIdx].compare(1,syntaxStr[tmpIdx].length() - 1,s,idx,syntaxStr[tmpIdx].length() - 1) != 0)
					{
						break;
					}else
					{
						idx += syntaxStr[tmpIdx].length() - 1;
						tmpIdx ++;
					}
				}
			}

			if(idx == s.length())
			{
				result ++;
			}
		}

		printf("Case #%d: %d\n",caseNum+1,result);
	}

	fflush(stdout);
}