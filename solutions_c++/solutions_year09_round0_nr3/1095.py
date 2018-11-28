#include <iostream>
#include <fstream>

#define COPY(j) ArryStr[i+1][j] = ArryStr[i][j]
#define ADD(j) ArryStr[i][j] += ArryStr[i][j-1]

using namespace std;

const int LENTH = 512;
const char org[] = "welcome to code jam";
const int SIZE = sizeof(org)-1;

//welcome to code jam
int seach(char * str)
{
	int ArryStr[LENTH][SIZE] ={0};

	int len = strlen(str);
	for(int i = 0 ; i < len; ++i)
	{
		switch(str[i])
		{
		case 'w':	ArryStr[i][0] ++; //w
					break;
		case 'e':	ADD(1); //we
					ADD(6);//welcome
					ADD(14);//welcome*to*code
					break;
		case 'l':	ADD(2); //wel
					break;
		case 'c':	ADD(3); //welc
					ADD(11);//welcome*to*c
					break;
		case 'o':	ADD(4);//welco
					ADD(9);//welcome*to
					ADD(12);//welcome*to*co
					break;
		case 'm':	ADD(5); //welcom
					ADD(18);//welcome*to*code*jam
					break;
		case ' ':	ADD(7);//welcome*
					ADD(10);//welcome*to*
					ADD(15);//welcome*to*code*
					break;
		case 't':	ADD(8); break;//welcome*t
		
		case 'd':	ADD(13);//welcome*to*cod
					break;
		case 'j': 
					ADD(16);//welcome*to*code*j
			break;
		case 'a': 
					ADD(17);//welcome*to*code*ja
					break;
		default:;
		}

		for(int j = 0; j < 19; ++j)
		{
			ArryStr[i+1][j] = ArryStr[i][j]%10000;
		}
	}
	return 	ArryStr[len][18];
}

int main()
{
	int T = 0;
	ifstream fin("C-large.in");
//	ifstream fin("C-small-attempt0.in");
	ofstream fout("C.out");
	int n = 0;

	char str[512] ;
	fin >> n;
	fin.getline(str,512);
	for(int i = 0 ; i < n ;++i)
	{
		fin.getline(str,512);
		//fin >> str;
		int t =seach( str);
		fout<<"Case #"<< (i+1) <<": ";
		if(t < 10)
		{
			fout << "000"<<t<<endl;
			continue;
		}
		if(t < 100)
		{
			fout << "00"<<t<<endl;
			continue;
		}
			if(t < 1000)
		{
			fout << "0"<<t<<endl;
			continue;
		}
		
		fout <<t<<endl;
	}
	
	return 0;
}