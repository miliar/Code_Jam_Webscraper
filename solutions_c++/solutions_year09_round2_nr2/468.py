#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <algorithm>
using namespace std;

int DigitsNum[9];
int DigitsNum2[9];

char buf[1280];


bool check(int x)
{
	for(int i = 0; i < 9; i++) DigitsNum2[i] = 0;
	while(x > 0)
	{
		int val = x%10;
		if(val > 0) DigitsNum2[val-1] ++;
		x /= 10;
	}
	for(int i = 0; i < 9; i++) if(DigitsNum2[i] != DigitsNum[i]) return false;
	return true;
}

int Naive(int x)
{
	x++;
	while(!check(x))
	{
		x++;
	}
	return x;
}

int main(void)
{
	//freopen("input.txt", "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin);
	//freopen("B-small-attempt1.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	
	freopen("outputB.txt", "wt+", stdout);


	int TestNum;
	scanf("%d", &TestNum);
	for(int Test = 0; Test < TestNum; Test++)
	{
		scanf("%s", buf);
		

		int len = strlen(buf);
		/*for(int i = 0; i < 9; i++) DigitsNum[i] = 0;
		for(int i = 0; i < len; i++)
		{
			if( buf[i] >= '1' && buf[i] <= '9')
			{
				DigitsNum[buf[i]-'1'] ++;
			}
		}

		int temp, naiveres;
		sscanf(buf, "%d", &temp);
		naiveres = Naive(temp);*/


		bool IsFound = false;
		char idmax = len-1, idmin = len-1;
		for(int i = len-1; i > 0; i--)
		{
			if(buf[i] > buf[i-1])
			{
				int idmin = i;
				for(int j = i; j < len; j++)
				{
					if(buf[j] > buf[i-1] && buf[j] < buf[idmin])
					{
						idmin = j;
					}
				}
				swap(buf[i-1], buf[idmin]);
				sort(buf+i, buf + len);
				IsFound = true;
				break;
				
			}
		}
		if(!IsFound)
		{
			int rightzero = len - 2;
			bool IsFoundNonZero = false;

			while(rightzero > 0 && !(buf[rightzero] == '0' && IsFoundNonZero))
			{
				if(buf[rightzero] != '0') IsFoundNonZero = true;
				rightzero--;
			}

			if(rightzero <= 0)
			{
				buf[len] = '0';
				buf[len+1] = 0;
				len++;
				sort(buf, buf+len);
				int i = 0;
				if(buf[0] == '0')
				{
					while(i < len && buf[i] == '0') i++;
					if(i != len) 
					{
						swap(buf[0], buf[i]);
					}
				}
			}
			else
			{
				char bestid = rightzero + 1;
				for(int i = rightzero + 2; i < len; i++)
				{
					if(buf[i] < buf[bestid]) bestid = i;
				}
				swap(buf[rightzero], buf[bestid]);
				sort(buf+rightzero+1, buf+len);
			}
		}
		/*char temps[512];
		sprintf(temps, "%d", naiveres);
		if(strcmp(buf, temps) != 0)
		{
			int a = 0;
		}

		printf("Case #%d: %s - %d\n", Test+1, buf, naiveres);*/
		printf("Case #%d: %s\n", Test+1, buf);
	}

	return 0;
}