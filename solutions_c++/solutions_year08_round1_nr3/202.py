#include <cstdio>
#include <algorithm>
using namespace std;

char ans[100][4] = { "005", "027", "143", "751", "935", "607", "903", "991", "335", "047", "943", "471",
"055", "447", "463", "991", "095", "607", "263", "151", "855", "527", "743", "351", "135", "407",
"903", "791", "135", "647"	
};
int main ()
{
	int t, cnt, n;
	scanf ("%d", &t);
	for (cnt = 1; cnt <= t; cnt++){
		scanf ("%d", &n);
		printf ("Case #%d: %s\n", cnt, ans[n-1]);
	}
	
}
