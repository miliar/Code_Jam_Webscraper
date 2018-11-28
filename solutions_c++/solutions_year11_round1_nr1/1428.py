#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>

using namespace std;

//bool hash[105];

int special(int a, int b, int c)
{
 	int i;
 	if(b < 100 && c == 100) return 0 ;
 	if(c == 0 && b > 0) return 0 ;
    if(b == 100) return 1 ;
    if(a == 1)
	{
	    if(b == 0)
		{
		    if(c == 100) return 0 ;
			else return 1 ; 	 
        } 	 
        else if(b == 100) return 1 ;
        else return 0 ;
    } 
	else 
	{
        for(i = 1; i <= a; i ++)
        {
		    if((i * b)%100 == 0) break ; 		
        }
        if(i > a) return 0 ;
        else return 1 ;
    }	 
}

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    int T, N, pd, pg, i, j, no = 1 ;
    scanf("%d", &T);
    while(T --)
    {
	    scanf("%d%d%d", &N, &pd, &pg);
	    printf("Case #%d: %s\n", no ++, special(N, pd, pg)?"Possible":"Broken");
    }
    //system("pause");
    return 0 ;
}
/*
100
1 50 32
9 52 95
1 100 100
4 54 47
5 50 77
4 57 1
8 86 9
6 10 93
10 72 27
8 61 61
5 60 73
6 29 67
10 71 99
6 34 94
8 65 3
3 45 99
10 10 89
9 0 100
1 87 100
10 45 62
9 72 15
10 98 41
10 71 98
10 58 16
4 25 45
3 75 14
3 1 89
10 12 3
4 42 80
10 66 0
10 14 14
8 0 0
9 24 14
3 8 78
10 90 85
2 50 72
1 34 29
8 90 62
10 62 56
7 63 50
10 70 95
8 97 87
1 46 97
4 62 71
5 26 75
9 71 21
7 13 50
10 12 16
3 1 63
2 7 31
2 60 80
10 55 61
1 50 2
2 50 0
4 82 55
4 41 67
8 29 93
2 42 46
6 73 25
5 60 49
10 59 18
4 59 83
2 31 91
5 80 19
3 20 58
1 26 95
10 100 0
8 29 87
10 71 60
4 80 69
5 62 47
10 74 91
5 70 93
7 48 52
1 12 29
10 69 99
10 55 78
2 25 22
4 1 32
2 50 61
9 50 100
4 1 62
10 65 71
10 96 17
3 84 26
5 10 21
2 75 63
5 13 59
3 29 42
5 40 48
4 75 74
5 97 34
10 12 99
2 50 78
10 11 6
1 50 65
1 44 0
10 28 13
9 80 62
5 75 80
*/
