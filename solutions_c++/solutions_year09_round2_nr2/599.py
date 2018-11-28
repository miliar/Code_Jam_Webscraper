#include <iostream>
#include <algorithm>
#include <cstring>

char a[1111111];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int t;
    std::cin >> t;
    std::cin.ignore();
    for (int tt = 0; tt < t; tt++)
    {
	memset(a,0,sizeof(a));
	
	gets(a);
	int n = 0;
	for (; a[n]; n++);
	bool ok = 0;
	
	for (int i = n-1; i > 0 && !ok; i--)
	    if (a[i] > a[i-1])
	    {
		int best = i;
		for (int j = i+1; j < n; j++)
		    if (a[best] > a[j] && a[j] > a[i-1])
			best = j;
		std::swap(a[i-1], a[best]);
		std::sort(a+i,a+n);
		ok = 1;
	    }
	if (!ok)
	{
	    a[n++] = '0';
	    std::reverse(a,a+n);
	    for (int i = 1; ; i++)
		if (a[i] != '0')
		{
		    std::swap(a[0], a[i]);
		    break;
		}
	}
	
	std::cout << "Case #" << tt+1 << ": ";
	puts(a);
    }
    return 0;
}
