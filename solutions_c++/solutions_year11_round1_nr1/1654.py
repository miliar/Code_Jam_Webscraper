#include<stdio.h>
#include<string.h>
int gcd(int a,int b)
{
	if(a>b)
	{
		int t=a;
		a=b;
		b=t;
	}

	if(a==0)return 0;
	if(a==1)return 1;
	int r;
	while(a)
	{
        r=b%a;
		b=a;
		a=r;
	}
	return b;
}
int main()
{
	freopen("A-small-attempt1 (3).in","r",stdin);
	freopen("A.small-ff.out","w",stdout);
	int T;
	while(scanf("%d",&T)!=EOF)
	{
		int N,Pd,Pg;
		int cases;
		for(cases=1;cases<=T;cases++)
		{
			scanf("%d%d%d",&N,&Pd,&Pg);
			if((Pg==0&&Pd!=0)||(Pd!=100&&Pg==100))
			{
				printf("Case #%d: Broken\n",cases);
				continue;
			}
            int comm = gcd(Pd,100);
			if(comm==0)
			{
				printf("Case #%d: Possible\n",cases);
				continue;
			}
			int left = 100/comm;
			if(left<=N)
			{
				printf("Case #%d: Possible\n",cases);
			}
			else
				printf("Case #%d: Broken\n",cases);
		}
	}
	return 0;
}

/*
100
10 91 46
2 50 41
6 42 65
6 60 28
7 10 89
1 80 15
8 90 27
10 18 79
1 66 88
5 11 86
1 50 58
7 99 9
1 50 32
4 60 73
8 49 22
10 89 57
2 50 91
8 8 41
7 28 6
8 33 68
10 54 76
10 95 71
10 87 58
2 22 7
9 98 39
8 92 87
10 82 47
9 17 7
1 99 35
1 78 4
8 21 96
8 19 63
10 96 89
3 26 62
10 35 29
1 50 59
2 44 52
10 52 41
4 50 0
8 60 27
5 59 88
5 15 74
3 25 31
3 24 20
10 8 70
1 53 30
10 100 100
8 14 86
7 96 78
10 90 61
3 25 89
9 50 100
7 6 17
10 77 100
10 10 66
10 44 4
3 39 99
2 50 36
10 97 51
5 25 8
5 60 96
7 91 3
5 35 87
1 2 0
1 46 54
7 92 24
1 31 92
9 65 25
2 79 92
5 25 75
1 21 39
4 20 7
3 80 33
10 55 61
5 86 92
3 75 17
6 100 0
10 10 17
5 75 27
8 26 99
4 77 98
4 0 0
7 66 70
3 16 69
10 17 69
7 91 8
3 20 9
1 27 100
7 0 100
4 40 5
10 84 60
7 12 11
8 45 31
9 57 4
3 76 8
5 10 48
10 81 8
8 2 92
3 32 15
4 23 84

*/