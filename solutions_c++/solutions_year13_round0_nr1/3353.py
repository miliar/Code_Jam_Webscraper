#include<cstdio>

char table[20];

int main()
{
	int T; scanf("%d",&T);
	for(int ii = 0; ii < T; ii++)
	{
		bool found = false;
		for(int i = 0; i < 4; i++)
			scanf("%s",table+i*4);
		//rows
		for(int i = 0; i < 4; i++)
		{
			int j = 1;
			char c = table[i*4];
			if(c == 'T')
				{ j++; c = table[i*4+1]; }
			if(c == '.') continue;
			bool good = true;
			for(; j < 4; j++)
				if(table[i*4+j] != c && table[i*4+j] != 'T')
					{ good = false; break; }
			if(good)
			{
				printf("Case #%d: %c won\n",ii+1,c);
				found = true;
				break;
			}
		}
		if(found) continue;
		//cols
		for(int i = 0; i < 4; i++)
		{
			int j = 1;
			char c = table[i];
			if(c == 'T')
				{ j++; c = table[i+4]; }
			if(c == '.') continue;
			bool good = true;
			for(; j < 4; j++)
				if(table[i+j*4] != c && table[i+j*4] != 'T')
					{ good = false; break; }
			if(good)
			{
				printf("Case #%d: %c won\n",ii+1,c);
				found = true;
				break;
			}
		}
		if(found) continue;
		//diags
		for(int i = 3; i <= 5; i+=2)
		{
			int j = 1;
			char c = table[i%5];
			if(c == 'T')
				{ j++; c = table[i%5+i]; }
			if(c == '.') continue;
			bool good = true;
			for(; j < 4; j++)
				if(table[i%5+j*i] != c && table[i%5+j*i] != 'T')
					{ good = false; break; }
			if(good)
			{
				printf("Case #%d: %c won\n",ii+1,c);
				found = true;
				break;
			}
		}
		if(found) continue;
		for(int i = 0; i < 16; i++)
			if(table[i] == '.')
			{
				printf("Case #%d: Game has not completed\n",ii+1);
				found = true;
				break;
			}
		if(!found)
			printf("Case #%d: Draw\n",ii+1);
	}
	return 0;
}
