#include <windows.h>
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>

#define MAX_BUFFER_LENGTH 65536

struct COUNTER
{
   int pos;
   int count;
   COUNTER(int a, int b){pos = a; count = b;}
};

typedef std::vector<COUNTER> COUNTERS;

void SUM(int& a, int b)
{
   a += b;
   while (a >= 10000)
      a -= 10000;
}

int search_str2(char* str, char* tmpl)
{
   COUNTERS g_cnt1;
   COUNTERS g_cnt2;
   COUNTERS* g_pCur = &g_cnt1;
   COUNTERS* g_pTemp = &g_cnt2;

   int tmpl_max_pos = strlen(tmpl) - 1;

   // Set basic counters to 1 for the last char in template
   for (int i = 0; i < strlen(str); i++)
   {
      if (str[i] == tmpl[tmpl_max_pos])
         g_pCur->push_back(COUNTER(i, 1));
   }

   // Iterate through all chars in template backward starting from the one last but one
   for (int iTmpl = tmpl_max_pos - 1; iTmpl >= 0; iTmpl--)
   {
      g_pTemp->clear();

      // Find all occurrences in the string
      for (int iStr = 0; iStr < strlen(str); iStr++)
      {
         if (str[iStr] == tmpl[iTmpl])
         {
            // Sum all counters for this char, which pos is greater than pos of this char in the string
            COUNTER c(iStr, 0);
            for (int k = 0; k < g_pCur->size(); k++)
            {
               if (c.pos < (*g_pCur)[k].pos)
                  SUM(c.count, (*g_pCur)[k].count);
            }
            g_pTemp->push_back(c);
         }
      }

      // Use latest calculated sums as current data
      COUNTERS* p1 = g_pCur;
      g_pCur = g_pTemp;
      g_pTemp = p1;
   }

   // Sum last counters
   int counter = 0;
   for (int k = 0; k < g_pCur->size(); k++)
      SUM(counter, (*g_pCur)[k].count);
   return counter;
}

int main(int argc, char* argv[])
{
	if (argc < 2)
		return 0;

	FILE* hFile = fopen(argv[1], "r");
	if (!hFile)
		return 0;

	char buf[MAX_BUFFER_LENGTH];

	if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
		return 0;

	int nCount = atoi(buf);
	int numCase = 1;
	while (numCase <= nCount)
	{
      if (!fgets(buf, MAX_BUFFER_LENGTH, hFile))
         return 0;

      int n = search_str2(buf, "welcome to code jam");
		printf("Case #%d: %4.4d\n", numCase, n);

		numCase++;
	}
	return 0;
}
