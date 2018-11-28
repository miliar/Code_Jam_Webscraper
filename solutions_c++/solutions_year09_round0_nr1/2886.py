#include <iostream>
#include <string>

int const L = 16;
int const D = 5010;
int const N = 510;

int l,d,n;
int a[D][L][26];
std::string s, ss[D];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    std::cin >> l >> d >> n;

    for (int i = 0; i < d; i++)
	std::cin >> ss[i];
	
    for (int i = 0; i < n; i++)
    {
	std::cin >> s;
	int cnt = 0;
	for (int j = 0; j < d; j++)
	{
	    bool ok = 1;
	    for (int k = 0, pos = 0; k < s.size(); k++, pos++)
	    {
		if (s[k] == '(')
		{
		    bool ok2 = 0;
		    for (; s[k] != ')'; k++)
			if (s[k] == ss[j][pos])
			    ok2 = 1;
			    
		    ok &= ok2;
		}
		else
		    ok &= (s[k] == ss[j][pos]);
	    }
	    cnt += ok;
	}
	std::cout << "Case #" << i+1 << ": " << cnt << "\n";
    }
    
    return 0;
}
