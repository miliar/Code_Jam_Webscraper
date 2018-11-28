#include <iostream>
#include <stdio.h>
using namespace std;

char table[] = {-24,-6,-2,-15,-10,3,-15,-16,5,-11,2,5,1,12,4,-2,-9,-2,5,-3,11,6,17,11,24,9};

int main()
{
  int N; cin >> N;
	int caseNum = 1;
	char s[200];
	gets(s);
	
	while(N > 0)
	{
		gets(s);
		for(int i=0;i<200;i++)
		{
			if(s[i] == 0) break;
			if(s[i] > 32) s[i] -= table[s[i]-97];
		}
		cout << "Case #" << caseNum << ": "; 
		for(int i=0;i<200;i++)
		{
			if(s[i] == 0) break;
			cout << s[i] ;
		}
		cout << endl;
		caseNum++;
		N--;
	}

  return 0;
}
