#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>

using namespace std;

bool ops[30][30];

int comb[30][30];

int list[105], len;

/*
void test()
{
    int i, j ;
	for(i = 0; i < 26; i ++)
	{
	    for(j = 0; j < 26; j ++)
		{
            if(ops[i][j])
		        printf("ops[%c][%c]\n", i + 'A', j + 'A'); 	  
        } 	  
    } 
	for(i = 0; i < 26; i ++)
	{
	    for(j = 0; j < 26; j ++)
		{
            if(comb[i][j] != -1)
		        printf("comb[%c][%c] = %c\n", i + 'A', j + 'A', comb[i][j] + 'A'); 	  
        } 	  
    } 	 
}
*/
int main()
{
 	freopen("B-large.in", "r", stdin);
 	freopen("B-large.out", "w", stdout);
    int T, C, D, N, i, j, t, no = 1 ;
    char temp[105];
    scanf("%d", &T);
    while(T--)
    {
	    memset(ops, 0, sizeof(ops));
	    memset(comb, -1, sizeof(comb));
        scanf("%d", &C);
        for(i = 0; i < C; i ++) 
        {
		    scanf("%s", temp);
			comb[temp[0]-'A'][temp[1]-'A'] = comb[temp[1]-'A'][temp[0]-'A'] = temp[2] - 'A' ;	  
	    }
	    scanf("%d", &D);
	    for(i = 0; i < D; i ++)
	    {
		    scanf("%s", temp);
			ops[temp[0]-'A'][temp[1]-'A'] = ops[temp[1]-'A'][temp[0]-'A'] = 1 ;	  
        }
        //test();
        scanf("%d", &N);
        scanf("%s", temp);
        len = -1 ;
        list[len] = temp[0] - 'A' ;
        for(i = 0; i < N; i ++)
        {
	        if(len == -1) {list[++len] = temp[i] - 'A'; continue;}
	        t = comb[list[len]][temp[i] - 'A'];
		 	if(t != -1) list[len] = t ;
			else list[++len] = temp[i]-'A' ;
			t = list[len] ;
			for(j = 0; j < len; j ++)
			{
			    if(ops[t][list[j]] == 1)
				{
				    len = -1 ;
					break ; 				   
				} 	  
            }  
        }
        printf("Case #%d: [", no ++);
        for(i = 0; i < len; i ++)
        {
		    printf("%c, ", list[i] + 'A'); 	  
	    }
	    if(len > -1) printf("%c", list[len] + 'A');
	    printf("]\n");
    }
    //system("pause");
    return 0 ;
}
