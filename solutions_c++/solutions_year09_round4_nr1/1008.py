#include <cstdio>
#include <vector>

using namespace std;

unsigned f(unsigned b, vector<int>& vi)
{
    if (vi.size() == 0)
	return 0;
    for (unsigned i = 0; i < vi.size(); ++i)
    {
	if (vi[i] <= b) {
	    vi.erase(vi.begin() + i);
	    return i + f(b + 1, vi);
	}
    }
    return -1;
}

int main()
{
    int nCase;
    scanf("%d", &nCase);
    for (int iCase = 1; iCase <= nCase; ++iCase)
    {
	int n;
	scanf("%d\n", &n);
	vector<int> vi;
	for (int i = 0; i < n; ++i)
	{
	    int m = 0;
	    char buf[1024];
	    gets(buf);
	    for (int j = 0; j < n; ++j)
	    {
		if (buf[j] == '1')
		    m = j + 1;
	    }
	    vi.push_back(m);
	}
	unsigned r = f(1, vi);
	printf("Case #%d: %u\n", iCase, r);
    }
    return 0;
}
