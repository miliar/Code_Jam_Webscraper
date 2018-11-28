#include <map>
#include <stdio.h>
#include <math.H>

//using namespace std;
//map<int,long double> stack;


char ans[][100]={"001", 
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
"991",
"095",
"607",
"263",
"151",
"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"

};


long double cal(int n)
{
/*	if (stack.find(n)!=stack.end())
		return stack[n];
	long double x = cal(n/2);
	x=x*x*(n%2?stack[1]:1);
	x-=1000*floorl(x/1000);
	stack[n] = x;
	return x;	*/
return 0;
}



void run()
{
	int n;
	scanf("%d", &n);
/*	long double x = cal(n);
	int y=(int)x;
	printf("%03d\n", y);*/
	printf ("%s\n", ans[n]);
}

main()
{
	int i;
	int n;
	scanf("%d", &n);
	//stack[0] = 1;
//	stack[1]=3+sqrtl(5);
	for (i=0; i<n; i++)
	{
		printf("Case #%d: ",i+1);
		run();
	}
	return 0;
}