#include <cstdio>

#define Rep(i,l,r)			for(int i = (l) ; i <= (r) ; i++)

char a[10][10] ;

bool Ta,Comp ;

int Tx,Ty ;

int Check()
{
	Rep(i,1,4)
	{
		bool sigX = true , sigO = true ;
		Rep(j,1,4)
			sigX &= (a[i][j] == 'X') ,
			sigO &= (a[i][j] == 'O') ;
		if(sigX)	return 1 ;
		if(sigO)	return -1 ;
	}
	Rep(j,1,4)
	{
		bool sigX = true , sigO = true ;
		Rep(i,1,4)
			sigX &= (a[i][j] == 'X') ,
			sigO &= (a[i][j] == 'O') ;
		if(sigX)	return 1 ;
		if(sigO)	return -1 ;
	}
	bool sigX = true , sigO = true ;
	Rep(i,1,4)
		sigX &= (a[i][i] == 'X') ,
		sigO &= (a[i][i] == 'O') ;
	if(sigX)	return 1 ;
	if(sigO)	return -1 ;
	sigX = true , sigO = true ;
	Rep(i,1,4)
		sigX &= (a[i][4-i+1] == 'X') ,
		sigO &= (a[i][4-i+1] == 'O') ;
	if(sigX)	return 1 ;
	if(sigO)	return -1 ;
	return 0 ;
}

int main()
{
	freopen("in.txt","r",stdin) , freopen("out.txt","w",stdout) ;
	int T ; scanf("%d\n",&T) ; Rep(TT,1,T)
	{
		Ta = false ; Comp = true ; Rep(i,1,4)
		{
			Rep(j,1,4)
			{
				a[i][j] = getchar() ;
				if(a[i][j]=='T')	Tx = i , Ty = j , Ta = true ;
				if(a[i][j]=='.')	Comp = false ;
			}
			scanf("\n") ;
		}
		int u ;
		if(!Ta)
			u = Check() ;
		else
		{
			a[Tx][Ty] = 'X' ; u = Check() ;
			if(u==0)	a[Tx][Ty] = 'O' , u = Check() ;
		}
		switch (u)
		{
			case 1 : printf("Case #%d: X won\n",TT) ; break ;
			case 0 :
				if(Comp)	printf("Case #%d: Draw\n",TT) ;
				else		printf("Case #%d: Game has not completed\n",TT) ;
			break ;
			case -1 : printf("Case #%d: O won\n",TT) ; break ;
		}
	}
	return 0 ;
}
