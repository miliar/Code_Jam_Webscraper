#include <iostream>
using namespace std;
#define MOD 10000
int main ()
{
	char word[1010];
	int num[25], i, test, cas = 1;
	//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
	//w e l c o m e   t  o    c  o  d  e     j  a  m
	freopen ("C-large.in", "r", stdin);
	freopen ("C-large.out", "w", stdout);
	scanf ("%d", &test);
	getchar();
	while (test --){
		memset(num, 0, sizeof (num));
		memset(word, 0, sizeof (word));
		//getchar();
		gets(word);
		int len = strlen (word);
		for (i = 0; i < len; i ++){
			if (word[i] == 'w'){
				num[1] ++;
				num[1] %= MOD;
			}else if (word[i] == 'e'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[2] += num[1];
				num[2] %= MOD;
				num[7] += num[6];
				num[7] %= MOD;
				num[15] += num[14];
				num[15] %= MOD;
			}else if (word[i] == 'l'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[3] += num[2];
				num[3] %= MOD;
			}else if (word[i] == 'c'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[4] += num[3];
				num[4] %= MOD;
				num[12] += num[11];
				num[12] %= MOD;
			}else if (word[i] == 'o'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[5] += num[4];
				num[5] %= MOD;
				num[10] += num[9];
				num[10] %= MOD;
				num[13] += num[12];
				num[13] %= MOD;
			}
			else if (word[i] == 'm'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[6] += num[5];
				num[6] %= MOD;
				num[19] += num[18];
				num[19] %= MOD;
			}
			else if (word[i] == ' '){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[8] += num[7];
				num[8] %= MOD;
				num[11] += num[10];
				num[1] %= MOD;
				num[16] += num[15];
				num[16] %= MOD;
			}
			else if (word[i] == 't'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[9] += num[8];
				num[9] %= MOD;
			}
			else if (word[i] == 'd'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[14] += num[13];
				num[14] %= MOD;
			}
			else if (word[i] == 'j'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[17] += num[16];
				num[17] %= MOD;
			}
			else if (word[i] == 'a'){
				//1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
				//w e l c o m e   t  o    c  o  d  e     j  a  m
				num[18] += num[17];
				num[18] %= MOD;
			}
		}
		printf ("Case #%d: %04d\n", cas ++, num[19]);
	}
	return 0;
}