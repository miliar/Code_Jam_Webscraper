#include <iostream>
using namespace std;


#define BYTE_BITS 8

static unsigned char BitRay[8] = { 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80 };

struct AdiBitField
{
	int AllocatedBytes;
	int ByteCount;		// in use
	int BitCount;		// in use
	unsigned char * BitField;
};

AdiBitField * AdiBitFieldAllocate(int NumberOfBits) 
{
	AdiBitField * ABF;

	ABF = (AdiBitField *) malloc(sizeof(AdiBitField));
	if (ABF) {
		ABF->BitCount = NumberOfBits;
		ABF->AllocatedBytes = ABF->ByteCount = (NumberOfBits + 7) / BYTE_BITS;
		ABF->BitField = (unsigned char *) malloc(ABF->ByteCount);
		if (!ABF->BitField) {
			free(ABF);
			ABF = NULL;
		}
	}
	return ABF;
}

int AdiBitFieldTestBit(const AdiBitField *ABF, int BitNumber)
{
	return ((ABF->BitField[BitNumber / BYTE_BITS]) & (BitRay[BitNumber & 7]));
}

void AdiBitFieldSetBit(AdiBitField * ABF, int BitNumber)
{
	ABF->BitField[BitNumber / BYTE_BITS] |= BitRay[BitNumber & 7];
}

void AdiBitFieldClearBit(AdiBitField * ABF, int BitNumber)
{
	ABF->BitField[BitNumber / BYTE_BITS] &= ~BitRay[BitNumber & 7];
}

void AdiBitFieldClearAllBits(AdiBitField * ABF)
{
	memset(ABF->BitField, 0, ABF->ByteCount);
}

void main()
{
	int T = 0;
	int N = 0;
	int No = 0;
	freopen("A-small-attempt0.in","r",stdin);
	cin >> No;
	for(int ii =0; ii< No; ii++)
	{
		cin >> N;
		cin >> T;
		unsigned long bnArrayToggle = 0x0000;
		AdiBitField * pAbf = AdiBitFieldAllocate(N+1);
		AdiBitFieldClearAllBits(pAbf );
		bool bOn = true;

		for(int it = 0; it < T; it++)
		{
			bool power = true;
			for(int in = 1; in<=N; in++ )
			{
				if (power)
				{
					if( AdiBitFieldTestBit(pAbf,in))
					{
						power = true;
						AdiBitFieldClearBit(pAbf,in);
					}
					else
					{
						power = false;
						AdiBitFieldSetBit(pAbf,in);
					}					
				}
			}
			if(it == T-1)
			{
				if(power)
				{
					bOn = true;					
				}
				else
				{
					bOn = false;										
				}
			}			
		}
		bOn = true;
		for (int j = N; j > 0; j--)
		{
			if (AdiBitFieldTestBit(pAbf,j))
			{
				
			}
			else
				bOn = false;
		}
		if( bOn )
		{
			printf("Case #%d: ON\n",ii+1);
		}
		else
		{
			printf("Case #%d: OFF\n",ii+1);
		}
		
	}
}