#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

struct type{
    char name[3];
    int place;
    type(){
        strcpy(name,"");
        place = -1;
    }
};

int abs(int n)
{
	return n>0?n:(-n);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
    int T , tcase = 0;
	scanf("%d",&T);
    while(T--)
    {
        int i , n ;
        scanf("%d",&n);
        int ot = 0 , bt = 0 ,opos = 1 , bpos = 1 ;
        int complete = 0 , ans = 0;
        for(i = 0 ; i < n ; i++){
            type t ;
            scanf("%s%d",t.name,&t.place);
            if(t.name[0] == 'O') 
			{
				if(ot >= abs(t.place - opos))
				{
					bt++;
					ot = 0;
					opos = t.place;
					ans++;
				}	
				else 
				{
					ans += abs(t.place - opos) - ot + 1;
					bt += abs(t.place - opos) - ot + 1 ;
					ot = 0 ;
					opos = t.place;
				}
			}
			if(t.name[0] == 'B') 
			{
				if(bt >= abs(t.place-bpos))
				{
					ot++;
					bt = 0 ;
					bpos = t.place;
					ans++;
				}
				else
				{
					ans += abs(t.place - bpos) - bt + 1 ;
					ot += abs(t.place - bpos) - bt + 1 ;
					bt = 0 ;
					bpos = t.place ;
				}
			}
        }
		
		printf("Case #%d: %d\n",++tcase,ans);
    }
    return 0;
}
