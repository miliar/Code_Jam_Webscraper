#include <iostream>
#include <string>
using namespace std;

#define MAX_LEN	512

//#define DBGOUT printf
 void DBGOUT(...) { }

const char *welcome = "welcome to code jam";


int get_Count(const char* givenStr, const char* findStr, int depth)
{
	int	count = 0;
	const char* pos = givenStr;


	if (!givenStr || !findStr || *givenStr == 0x0 || *findStr == 0x0)
		return 0;

	if (!strcmp(givenStr, findStr))
	{
		DBGOUT("matched\n");
		return 1;
	}

	if (strchr(givenStr, *findStr) == NULL || strlen(givenStr) <= strlen(findStr))
		return 0;

	// find first letter
	while(*pos != 0x0 && *pos != *findStr)
		pos++;

	while(strlen(pos) >= strlen(findStr))
	{
		if (*pos == *findStr)
		{
			if (strlen(findStr) == 1)
			{
				while(*pos)
				{
					if (*pos == *findStr)
						count++;
					pos++;
				} 
					
				DBGOUT("%d char matched\n", count);

				return count;
			}

			DBGOUT("%c[%d]:", *pos, pos - givenStr);
			count += get_Count(pos + 1, findStr + 1, depth + 1);
		}
		pos++;
	}
	
	return count;
}

int main()
{
	int		tcase_cnt;
	int		result;
	string	lineBuf;
	char	buf[MAX_LEN] = "";

	getline(cin, lineBuf);
	tcase_cnt = atoi(lineBuf.c_str());

	for (int i = 0; i < tcase_cnt; i++)
	{
		if (!getline(cin, lineBuf))
			break;

		strcpy(buf, lineBuf.c_str());

		// trim Right
		int len = strlen(buf);
		for (int j = len - 1; j >= 0; j--)
		{
			if (buf[j] == ' ' || buf[j] == '\n')
				buf[j] = 0x0;
			else
				break;
		}

		result = get_Count(buf, welcome, 0);

		printf("Case #%d: %04d\n", i + 1, result % 10000);
	}
}
