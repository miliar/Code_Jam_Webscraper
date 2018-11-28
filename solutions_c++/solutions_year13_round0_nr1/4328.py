#include<cstdio>
#include<cstring>

char tab[4][4];

int main()
{
	int n;
	scanf("%d", &n);
	for (int c = 1; c <= n; ++c)
	{
		for(int i = 0; i < 4; ++i)
		{
			scanf("%s", tab[i]);
		}
		//for(int i = 0; i < 4; ++i)
		//{
		//	for(int j = 0; j < 4; ++j)
		//	{
		//		printf("%c", tab[i][j]);
		//	}
		//	printf("\n");
		//}
		int x = 0, o = 0, t = 0;
		bool xwin = false, owin = false;

		//sprawdzanie w poziomie
		for(int i = 0; i < 4; ++i)
		{
			x = 0;
			o = 0;
			t = 0;
			for(int j = 0; j < 4; ++j)
			{
				switch(tab[i][j])
				{
					case 'X':
						x++;
						break;
					case 'O':
						o++;
						break;
					case 'T':
						t++;
						break;
				}
				if (x == 4 || (x == 3 && t == 1))
					xwin = true;
				if (o == 4 || (o == 3 && t == 1))
					owin = true;
			}
		}


		//sprawdzanie w pionie
		for(int i = 0; i < 4; ++i)
		{
			x = 0;
			o = 0;
			t = 0;
			for(int j = 0; j < 4; ++j)
			{
				switch(tab[j][i])
				{
					case 'X':
						x++;
						break;
					case 'O':
						o++;
						break;
					case 'T':
						t++;
						break;
				}
				if (x == 4 || (x == 3 && t == 1))
					xwin = true;
				if (o == 4 || (o == 3 && t == 1))
					owin = true;
			}
		}

		//przekatna 1.
		x = 0;
		o = 0;
		t = 0;
		for(int i = 0; i < 4; ++i)
		{
			switch(tab[i][i])
			{
				case 'X':
					x++;
					break;
				case 'O':
					o++;
					break;
				case 'T':
					t++;
					break;
			}
			if (x == 4 || (x == 3 && t == 1))
				xwin = true;
			if (o == 4 || (o == 3 && t == 1))
				owin = true;
		}

		//przekatna 2.
		x = 0;
		o = 0;
		t = 0;
		for(int i = 0; i < 4; ++i)
		{
			switch(tab[i][3-i])
			{
				case 'X':
					x++;
					break;
				case 'O':
					o++;
					break;
				case 'T':
					t++;
					break;
			}
			if (x == 4 || (x == 3 && t == 1))
				xwin = true;
			if (o == 4 || (o == 3 && t == 1))
				owin = true;
		}



		bool draw = true;
		if(xwin == false && owin == false)
		{
			for(int i = 0; i < 4; ++i)
				for(int j = 0; j < 4; ++j)
					if(tab[i][j] == '.')
						draw = false;
			if(draw == true)
				printf("Case #%d: Draw\n", c);
			else
				printf("Case #%d: Game has not completed\n", c);
		}

		if(xwin == true)
			printf("Case #%d: X won\n", c);
		if(owin == true)
			printf("Case #%d: O won\n", c);
	}
	return 0;
}