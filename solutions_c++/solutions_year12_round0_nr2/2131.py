#include <stdio.h>
#include <map>

int main()
{
	int N;
	scanf("%d", &N);
	for(int i=0;i<N;i++)
	{
		int num;
		scanf("%d", &num);
		int surpallowed;
		scanf("%d", &surpallowed);
		int min;
		scanf("%d", &min);
		int sure = 0;
		for(int k=0;k<num;k++)
		{
			int val;
			scanf("%d", &val);
			if(min == 0)
			{
				sure++;
			}
			else if (min == 1 && val > 0)
			{
				sure++;
			}
			else if(val >= min*3-2)
			{
				sure++;
			}
			else if(surpallowed > 0 && val >= min*3-4 && (min*3-4) > 0)
			{
				surpallowed--;
				sure++;
			}
		}
		printf("Case #%d: %d\n", i+1, sure);
	}

	/*
	std::map<char, char> m;
	m.insert(std::make_pair('y', 'a')); 
	m.insert(std::make_pair('n', 'b'));
	m.insert(std::make_pair('f', 'c'));
	m.insert(std::make_pair('i', 'd'));
	m.insert(std::make_pair('c', 'e'));
	m.insert(std::make_pair('w', 'f'));
	m.insert(std::make_pair('l', 'g'));
	m.insert(std::make_pair('b', 'h'));
	m.insert(std::make_pair('k', 'i'));
	m.insert(std::make_pair('u', 'j'));
	m.insert(std::make_pair('o', 'k'));
	m.insert(std::make_pair('m', 'l'));
	m.insert(std::make_pair('x', 'm'));
	m.insert(std::make_pair('s', 'n'));
	m.insert(std::make_pair('e', 'o'));
	m.insert(std::make_pair('v', 'p'));
	m.insert(std::make_pair('z', 'q'));
	m.insert(std::make_pair('p', 'r'));
	m.insert(std::make_pair('d', 's'));
	m.insert(std::make_pair('r', 't'));
	m.insert(std::make_pair('j', 'u'));
	m.insert(std::make_pair('g', 'v'));
	m.insert(std::make_pair('t', 'w'));
	m.insert(std::make_pair('h', 'x'));
	m.insert(std::make_pair('a', 'y'));
	m.insert(std::make_pair('q', 'z'));
	m.insert(std::make_pair(' ', ' '));

	int N;
	scanf("%d", &N);
	char buf[101];
	gets(buf);
	for(int i =0;i<N;i++)
	{
		gets(buf);
		size_t len = strlen(buf);
		printf("Case #%d: ", i+1);
		for(int k=0;k<len;k++)
		{
			printf("%c", m[buf[k]]);
		}
		printf("\n");
	}*/

	return 0;
}