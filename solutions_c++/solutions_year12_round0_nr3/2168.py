#include <stdio.h>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>

std::map<int, std::vector<std::pair<int, int> > > m;

int main()
{
	int N;

	for(int i=1;i<=6;i++)
	{
		int ndig = (int)pow(10.0,i);
		int ndigmax = 0;
		if(i==6)
			ndigmax = ndig*2;
		else
			ndigmax = ndig*10;

		std::vector<std::pair<int, int> > v;
		for(int k = ndig;  k < ndigmax; k++)
		{
			std::vector<int> v2;
			for(int digidx = 1; digidx < i+1; digidx++)
			{
				int ex = (int)pow(10.0, i-digidx);
				int ex1 = (int)pow(10.0, digidx);
				int curdig = (k/(ex)) %10;				
				if (curdig > 0 && (i < 6 || curdig == 1))
				{
					int a = k/(ex*10);
					int b = (k%(ex*10))*ex1;
					int fi = a + b;
					if (fi > k)
					{
						v2.push_back(fi);
					}
				}				
			}

			std::sort(v2.begin(), v2.end());
			v2.erase(std::unique(v2.begin(), v2.end()), v2.end());

			for(std::vector<int>::iterator it = v2.begin(); it != v2.end(); ++it)
			{
				v.push_back(std::make_pair(k, *it));
			}
		}
		m.insert(std::make_pair(i, v));
	}

	scanf("%d", &N);
	for(int i=0;i<N;i++)
	{
		int left, right;
		scanf("%d %d", &left, &right);
		int result = 0;
		if(left >= 10)
		{
			int index = (int)log10((double)left);
			std::vector<std::pair<int, int> > &v = m[index];
			for(std::vector<std::pair<int, int> >::iterator it = v.begin(); it != v.end(); ++it)
			{
				if(it->first > right)
					break;
				if(it->first >= left && it->second <=right)
				{
					//printf("(%d,%d)\n",it->first, it->second);
					result++;
				}
			}
		}
		printf("Case #%d: %d\n",i+1, result);
		/*int num;
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
		printf("Case #%d: %d\n", i+1, sure);*/
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