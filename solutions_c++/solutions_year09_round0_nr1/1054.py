#include <iostream>
#include <fstream>

using namespace std;

inline bool compare(char * str ,int StrLen, char *Token)
{
	bool jg = true;

	for(int i = 0,j=0; i < StrLen; ++i )
	{
		if(Token[j] == '\0')
		{
				jg = false;
				break;	
		}

		if(Token[j] == '(')
		{
			++j;
			while(Token[j] != str[i] && Token[j] !=')' )
			{
				++j;
			}
			if(Token[j] ==')')
			{
				jg = false;
				break;
			}
			else
			{
				while(Token[j] !=')')
				{
					++j;
				}
				++j;
			}
		
		}
		else
		{
			if(Token[j] != str[i])
			{
				jg = false;
				break;
			}
			++j;
		}
	}
	return jg;
}

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("a.out");

	int c,d,n;

	char str[5010][16];
	char token[512];

	fin >> c >> d >> n;

	for(int i = 0 ; i < d; ++i)
	{
		//fin.getline(str[i], 16);
		fin>> str[i];
	}
	for(int j = 0 ; j < n ;++j)
	{
		int js = 0;

		//fin.getline(token, 512);
		fin >> token;
	
		for(int k = 0 ; k < d;++k)
		{
			if(compare(str[k] ,c, token))
			{
				++js;
			}
		}
		fout <<"Case #"<< (j+1) <<": " << js <<endl;
	}

	return 0;

}