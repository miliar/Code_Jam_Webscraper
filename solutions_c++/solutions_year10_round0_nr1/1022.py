#include <stdio.h>
#include <stdlib.h>

void main()
{
	int c[30];

	c[0] = 2;
	c[1] = 4;
	c[2] = 8;
	c[3] = 16;
	c[4] = 32;
	c[5] = 64;
	c[6] = 128;
	c[7] = 256;
	c[8] = 512;
	c[9] = 1024;
	c[10] = 2048;
	c[11] = 4096;
	c[12] = 8192;
	c[13] = 16384;
	c[14] = 32768;
	c[15] = 65536;
	c[16] = 131072;
	c[17] = 262144;
	c[18] = 524288;
	c[19] = 1048576;
	c[20] = 2097152;
	c[21] = 4194304;
	c[22] = 8388608;
	c[23] = 16777216;
	c[24] = 33554432;
	c[25] = 67108864;
	c[26] = 134217728;
	c[27] = 268435456;
	c[28] = 536870912;
	c[29] = 1073741824;

	FILE* in = ::fopen("a.in", "r");
	FILE* out = ::fopen("a.out", "w");

	int t;

	::fscanf(in, "%d", &t);
	for(int i = 0; i < t; ++i)
	{
		int n, k;

		::fscanf(in, "%d%d", &n, &k);

		bool s[30];
		for(int j = 0; j < 30; ++j)
			s[j] = false;

		k %= c[n - 1];

		for(int j = 0; j < k; ++j)
		{		
			bool p = true;

			for(register int l = 0; l < n; ++l)
			{	
				p = s[l];
				s[l] = !s[l];

				if(!p)
					break;
			}
		}

		register int j = -1;
		while(++j < n && s[j]);

		::fprintf(out, "Case #%d: %s\n", i + 1, j == n? "ON": "OFF");
	}

	::fclose(out);
	::fclose(in);
}