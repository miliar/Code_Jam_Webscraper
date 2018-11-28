#include <cstdio>
#include <cstring>

int combine[26][26];
int clear[26][26];

int base[26];

char res[400];

void test();


void read_test()
{
	int T,i = 0;
	for(scanf("%d", &T); i < T; i++)
	{
		test();
		printf("Case #%d: %s\n", i+1, res);
	}
}

void test()
{
	int i = 0, cur =-1;
	char str[4], ch, result[110];
// clearing the combine
	for(i = 0; i < 26; i++)
	{
		for(int j = 0; j < 26; j++)
		{
			combine[i][j] = -1;
		}
	}

// resetting the clear
	for(i = 0; i < 26; i++)
	{
		for(int j = 0; j < 26; j++)
		{
			clear[i][j] = 0;
		}
	}

// resetting base array
	for(i = 0; i < 26; i++)
	{
		base[i] = 0;
	}

	int C, D, N;
	scanf("%d", &C);
	for(i = 0; i < C; i++)
	{
		scanf(" %s",str);
		combine[str[0]-'A'][str[1]-'A'] = str[2]-'A';
		combine[str[1]-'A'][str[0]-'A'] = str[2]-'A';
	}
	scanf("%d", &D);
	for(i = 0; i < D; i++)
	{
		scanf(" %s",str);
		clear[str[0]-'A'][str[1]-'A'] = 1;
		clear[str[1]-'A'][str[0]-'A'] = 1;
	}
	scanf("%d ", &N);
	for(i = 0; i < N; i++)
	{
		scanf("%c", &ch);
		result[++cur] = ch;
		if((cur != 0) && (combine[result[cur - 1] - 'A'][ch - 'A'] != -1))
		{
			//printf( "Value of combined:%d char:%c char:%c ", result[cur-1]-'A',ch - 'A');
			char ch_temp = result[cur-1];
			//printf("Combined:%d Temp: %c %c",combine[result[cur - 1] - 'A'][ch - 'A'], ch_temp, ch);
			result[cur-1] = combine[ch_temp - 'A'][ch - 'A'] + 'A';
			cur--;
			base[ch_temp - 'A'] -= 1;
			if(base[ch_temp - 'A'] < 0)
			{
				base[ch_temp - 'A'] = 0;
			}

		}
		else
		{
			if((base['Q' - 'A'] && clear['Q' - 'A'][ch - 'A']) || 
			   (base['W' - 'A'] && clear['W' - 'A'][ch - 'A']) ||
			   (base['E' - 'A'] && clear['E' - 'A'][ch - 'A']) ||
			   (base['R' - 'A'] && clear['R' - 'A'][ch - 'A']) ||
			   (base['A' - 'A'] && clear['A' - 'A'][ch - 'A']) ||
			   (base['S' - 'A'] && clear['S' - 'A'][ch - 'A']) ||
			   (base['D' - 'A'] && clear['D' - 'A'][ch - 'A']) ||
			   (base['F' - 'A'] && clear['F' - 'A'][ch - 'A']))
			{
				cur = -1;
				base['Q' - 'A'] = 0;	
				base['W' - 'A'] = 0;	
				base['E' - 'A'] = 0;	
				base['R' - 'A'] = 0;	
				base['A' - 'A'] = 0;	
				base['S' - 'A'] = 0;	
				base['D' - 'A'] = 0;	
				base['F' - 'A'] = 0;	
			}
			else
			{
				base[ch - 'A'] += 1;
			}
		}
	}
	//format the output
	res[0] = '[';
	int current = 0;
	for(i = 0; i <= cur  ; i++)
	{
		if(i)
		{
			res[++current] = ',';
			res[++current] = ' ';
		}
		res[++current] = result[i];
	}
	res[++current] = ']';
	res[++current] = '\0';
}

int main()
{
	read_test();		

    	return 0;
}
