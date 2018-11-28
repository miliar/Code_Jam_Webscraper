#include <iostream>
#include <list>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>

#define ASCII_SPACE 32
#define ASCII_NEWLINE 10


using namespace std;




#define PRINT_TOKEN(token)\
	do{\
		cout<<#token<<" is "<<token<<endl; \
	}while(0)


#define READ(arg)\
	do{\
		long long arg;\
		cin>>arg;\
	}while(0)

//#define PRINT_ARR()
typedef long long ll;

#define BASE 'a'
int main()
{
	long long T;
	char tab[26];
	cin>>T;
	
	tab[0] = 'y';
	tab[1] = 'h';
	tab[2] = 'e';
	tab[3] = 's';
	tab[4] = 'o';
	tab[5] = 'c';
	tab[6] = 'v';
	tab[7] = 'x';
	tab[8] = 'd';
	tab[9] = 'u';
	tab[10] = 'i';
	tab[11] = 'g';
	tab[12] = 'l';
	tab[13] = 'b';
	tab[14] = 'k';
	tab[15] = 'r';
	tab[16] = 'z';
	tab[17] = 't';
	tab[18] = 'n';
	tab[19] = 'w';
	tab[20] = 'j';
	tab[21] = 'p';
	tab[22] = 'f';
	tab[23] = 'm';
	tab[24] = 'a';
	tab[25] = 'q';
	
	char str[256];

	cin.getline(str,256);
	for(long long i=0;i<T;i++){

		long long result ;
		char str2[256];
		cin.getline(str2,256);
		for(int a=0; str2[a] != '\0';a++){
			int idx = str2[a] - 'a';
			if(str2[a] == ' ') continue;
			str2[a] = tab[ idx ];
		}
		cout<<"Case "<<"#"<<i+1<<": "<<str2;
		cout<<endl;

	}
	return 0;
}


