#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>

char engin[1005][102];
int enginNumber;
bool enginSearched[1005];

int hash[1005][1005];

unsigned long dwCryptTable[0x500];


char key[104];

void InitializeCryptTable()
{
    unsigned long seed   = 0x00100001;
    unsigned long index1 = 0;
    unsigned long index2 = 0;
    int   i;

    for (index1 = 0; index1 < 0x100; index1++)
    {
        for (index2 = index1, i = 0; i < 5; i++, index2 += 0x100)
        {
            unsigned long temp1, temp2;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp1 = (seed & 0xFFFF) << 0x10;

            seed  = (seed * 125 + 3) % 0x2AAAAB;
            temp2 = (seed & 0xFFFF);

            dwCryptTable[index2] = (temp1 | temp2);
        }
    }
}

unsigned long hashData( char *data,int length ){
	unsigned long seed1 = 0x7FED7FED;
	unsigned long seed2 = 0xEEEEEEEE;
	unsigned long shifted_type = (0 << 8);
	int ch;

	while (length > 0) {
		ch = *data++;

		seed1 = dwCryptTable[shifted_type + ch] ^ (seed1 + seed2);
		seed2 = ch + seed1 + seed2 + (seed2 << 5) + 3;
		length--;
	}

	return seed1;
}




int main(int argc, char * argv[])
{
//	freopen( "input","r",stdin );
	int n;
	std::cin>>n;
	InitializeCryptTable(  );
	for( int h = 0; h < n; h++ ){
		
		for( int g = 0; g < 1005; g++ ){
			hash[g][0] = -1;
		}
		memset(enginSearched, false, 1005);

		unsigned index;
		std::cin>>enginNumber;
		std::cin.getline( engin[0],102 );
		for( int k = 0; k < enginNumber; k++ ){
			std::cin.getline( engin[k],102 );
			index = ( unsigned )( hashData( engin[k],strlen( engin[k] ) ) )%1000;
			int d;
			for( d = 0; hash[index][d] != -1; d++ );
			hash[index][d] = k;
			hash[index][d+1] = -1;
		}

		int res;
		int input;
		int searched;
		std::cin>>input;
		std::cin.getline( key,100 );
		searched = 0;
		res = 0;
		for( int e = 0; e < input; e++ ){
			std::cin.getline( key,100 );
			index = ( unsigned )( hashData( key,strlen( key ) ) )%1000;
			for( int w = 0; hash[index][w] != -1; w++ ){
				if( strcmp( key,engin[hash[index][w]] ) == 0 ){
					if( enginSearched[hash[index][w]] == false ){
						enginSearched[hash[index][w]] = true;
						searched++;
					}
				}
				if( searched == enginNumber ){
					res++;
					memset(enginSearched, false, 1005);
					enginSearched[hash[index][w]] = true;
					searched = 1;
				}
			}
		}
		std::cout<<"Case #"<<h+1<<": "<<res<<std::endl;
	}
    return 0;
}
