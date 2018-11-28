#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
using namespace std ;

int Myabs(int abs)
{
	if(abs < 0)
		return -abs;
	return abs;	
}


bool IsPossible(int tn, int tm, int ta)
{
	if( tn * tm < ta)
    {
        return false ;
    }
    int x1, x2, x3, y1, y2, y3, area;
    
    for(x1 = 0; x1 <= tn; x1 ++)
    	for(y1 = 0; y1 <= tm; y1 ++)
    		for(x2 = 0; x2 <= tn; x2 ++)
    			for(y2 = 0; y2 <= tm; y2 ++)
    				for(x3 = 0; x3 <= tn; x3 ++)
    					for(y3 = 0; y3 <= tm; y3 ++)
    					{
        					area = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1);
       					 	if( Myabs(area) == Myabs(ta))
        					{
            					printf("%d %d %d %d %d %d\n", x1, y1, x2, y2, x3, y3);
								return true ;
        					}
    					}
	
	return false;
}




int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out.txt", "w", stdout);
    int c, kase;
    int n, m, a;
    
    scanf("%d", &c);
    for(kase = 1; kase <= c; kase ++)
    {

        scanf("%d %d %d", &n, &m, &a);       
               
		printf("Case #%d: ", kase);

        if(!IsPossible(n, m, a)) 
			printf("IMPOSSIBLE\n");
    }
//    system("pause");
    return 0;   
}
