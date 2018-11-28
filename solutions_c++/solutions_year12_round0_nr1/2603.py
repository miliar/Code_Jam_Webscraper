#include <iostream>
#include <string>

using namespace std;

char Map[26];

void Pre()
{
	Map[0] = 'y'; Map[1] = 'h'; Map[2] = 'e'; Map[3] = 's'; Map[4] = 'o';
	Map[5] = 'c'; Map[6] = 'v'; Map[7] = 'x'; Map[8] = 'd'; Map[9] = 'u';
	Map[10] = 'i'; Map[11] = 'g'; Map[12] = 'l'; Map[13] = 'b'; Map[14] = 'k';
	Map[15] = 'r'; Map[16] = 'z'; Map[17] = 't'; Map[18] = 'n'; Map[19] = 'w';
	Map[20] = 'j'; Map[21] = 'p'; Map[22] = 'f'; Map[23] = 'm'; Map[24] = 'a';
	Map[25] = 'q';

}
int main()
{
	Pre();
	int T;
	scanf("%d\n",&T);

	for(int i = 1; i<= T; ++i)
	{
		string str;
		getline(cin,str);
		for(int j = 0; j< str.length(); ++j)
		{
			if(str[j] != ' ') str[j] = Map[str[j] - 'a'];
		}
		printf("Case #%d: %s\n",i,str.c_str());
	}
}