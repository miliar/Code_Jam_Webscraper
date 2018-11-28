#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

//#define DEBUG

int cnt;

void Moving(int number, int start, int end);
int CountRecycledNumberPair(int start, int end);

#ifdef DEBUG

ofstream out("D:\\C-small_result.txt");
int temp;
#endif

int main()
{
	int i;
	ifstream in("D:\\C-small-attempt0.in");
	ofstream out("D:\\C-small_result.txt");


	int T, caseN = 1;
	int A, B;

	in >> T;
	while (T--)
	{
		in >> A >> B;

		cnt = 0;
#ifdef DEBUG

		temp = 1;
#endif

		for (i=A; i<=B; i++)
			Moving(i, A, B);

		out << "Case #" << caseN++ << ": " << cnt << endl;
	}
	
	return 0;
}


void Moving(int number, int start, int end)
{
	int i, j, k;
	char str[15], buffer[15];
	int len;
	int newnumber;

	len = sprintf(str, "%d", number); //sprintf返回的就是 字符串的长度

	for (i=1; i<len; i++)
	{
		if (str[i] == '0') continue; //pass leading zero

		for (j=i,k=0; j<len; j++, k++) buffer[k] = str[j];
		for (j=0; j<i; j++,k++) buffer[k] = str[j];
		buffer[k] = 0;

		sscanf(buffer, "%d", &newnumber);
		if (newnumber>number && newnumber<=end) 
		{

#ifdef DEBUG
out << temp++ << ": ( " << number << ", " << newnumber << " )" << endl;
#endif
			cnt++;
		}
	}
}