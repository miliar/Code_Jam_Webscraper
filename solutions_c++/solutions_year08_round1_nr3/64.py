//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Attention!!: 	
//	Created @ 2008_6
//
//////////
#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;
const int MAXN = 100;

int 	cas, T;

string 	a[50] = 
{
"001",
"005",
"027",
"143",
"751",
"935",

"607",
"903",
"991",
"335",
"047",

"943",
"471",
"055",
"447",
"463",
		// 15
		
"991",
"095",
"607",
"263",
"151",

	//21
"855",
"527",
"743",
"351",
"135",

	//26
"407",
"903",
"791",
"135",
"647"
};

int main()
{
	int 	i, j, k;

	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small.out", "w", stdout);

	
	for (scanf("%d", &cas); cas; cas--)
	{

		scanf("%d", &i);
		
		printf("Case #%d: ", ++T);
		cout << a[i] << endl;

	}

	return 0;
}
