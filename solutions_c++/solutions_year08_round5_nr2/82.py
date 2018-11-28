#include <cstdio>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

class Stan
{
public:
	int x,y,bx,by,yx,yy;
	Stan(){}
	Stan(int X,int Y,int BX,int BY,int YX,int YY)
		:x(X),y(Y),bx(BX),by(BY),yx(YX),yy(YY){};
	bool operator < (const Stan& T) const
	{
		if (x!=T.x) return x<T.x;
		if (y!=T.y) return y<T.y;
		if (bx!=T.bx) return bx<T.bx;
		if (by!=T.by) return by<T.by;
		if (yx!=T.yx) return yx<T.yx;
		if (yy!=T.yy) return yy<T.yy;
		return false;
	}
};

class Para
{
public:
	Stan S;
	int D;
	Para(){}
	Para (Stan s,int d){S = s; D = d;}
	bool operator < ( const Para&T) const
	{
		return D>T.D;
	}
};

int Pla[20][20];
pair<int,int> Gdz[20][20][4];
int Sx,Sy,Ex,Ey;

int Odw(int G)
{
	if (G == 0) return 2;
	if (G == 1) return 3;
	if (G == 2) return 0;
	if (G == 3) return 1;
}

void Strzel( Stan &T, int C, int G)
{
	if (C == 0)
	{
		T.bx = Gdz[T.x][T.y][G].first;
		T.by = Gdz[T.x][T.y][G].second;
	}
	else
	{
		T.yx = Gdz[T.x][T.y][G].first;
		T.yy = Gdz[T.x][T.y][G].second;
	}
}

bool Przejsc( Stan &T,int C )
{
	if( C == 0)
		return (T.x == T.bx) && (T.y == T.by) && (T.yx != -5);
	if( C == 1)
		return (T.x == T.yx) && (T.y == T.yy) && (T.bx != -5);
}

map< Stan, int > Zbior;

bool Check( Stan &T, int D)
{
	map<Stan,int>::iterator F = Zbior.find(T);
	if (F == Zbior.end())return true;
	if (F->second > D) return true;
	return false;
}

int main()
{
	int lw;
	scanf("%d",&lw);

	for (int L=1;L<=lw;L++)
	{
		int n,m;
		scanf("%d%d",&n,&m);
		for (int i=0;i<=n+1;i++)
			for (int j=0;j<=m+1;j++)
				Pla[i][j] = -1;
		for (int i=1;i<=n;i++)
		{
			char Tab[20];
			scanf("%s",Tab);
			for (int j=1;j<=m;j++)
			{
				if (Tab[j-1] == 'O') 
				{
					Pla[i][j] = 0;
					Sx = i;
					Sy = j;
				}
				if (Tab[j-1] == '#')
					Pla[i][j] = -1;
				if (Tab[j-1] == '.')
					Pla[i][j] = 0;
				if (Tab[j-1] == 'X')
				{
					Pla[i][j] = 0;
					Ex = i;
					Ey = j;
				}
			}
		}

		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				if (Pla[i][j] == 0)
				{
					for (int g=0;g<4;g++)
					{
						pair<int,int> x = make_pair(i,j);
						if (g == 0)
							while ( Pla[ x.first ][ x.second - 1 ] == 0 ) x.second--;
						if (g == 2)
							while ( Pla[ x.first ][ x.second + 1 ] == 0 ) x.second++;
						if (g == 1)
							while ( Pla[ x.first - 1][ x.second ] == 0) x.first--;
						if (g == 3)
							while ( Pla[ x.first + 1][ x.second ] == 0) x.first++;
						Gdz[i][j][g] = x;
					}
				}

		map< Stan, int > Zbior;
		priority_queue< Para > Kol;
		Kol.push( Para( Stan( Sx,Sy,-5,0,-5,0),0) );
		Stan Temp;
		int Best = -1;

		while (!Kol.empty() )
		{
			Para T = Kol.top(); Kol.pop(); 
			if ((Ex == T.S.x) &&( Ey == T.S.y))
			{
				Best = T.D;
				break;
			}
				
			map<Stan,int>::iterator F =  Zbior.find( T.S );
			if (F != Zbior.end() && F->second <= T.D ) continue;
			Zbior[ T.S ] = T.D;
			if (Pla[ T.S.x - 1 ][ T.S.y ] == 0 ) { Temp = T.S;
			                                       Temp.x--;
												   if ( Check( Temp, T.D+1 ) )
												   Kol.push( Para( Temp, T.D+1 ) );
			                                     }
			if (Pla[ T.S.x + 1 ][ T.S.y ] == 0 ) { Temp = T.S;
			                                       Temp.x++;
												   if ( Check( Temp, T.D+1 ) )
												   Kol.push( Para( Temp, T.D+1 ) );
			                                     }
			if (Pla[ T.S.x ][ T.S.y - 1 ] == 0 ) { Temp = T.S;
			                                       Temp.y--;
												   if ( Check( Temp, T.D+1 ) )
												   Kol.push( Para( Temp, T.D+1 ) );
			                                     }
			if (Pla[ T.S.x ][ T.S.y + 1 ] == 0 ) { Temp = T.S;
			                                       Temp.y++;
												   if ( Check( Temp, T.D+1 ) )
												   Kol.push( Para( Temp, T.D+1 ) );
			                                     }
		
			if ( Przejsc( T.S, 0 ) ) { Temp = T.S;
			                           Temp.x = T.S.yx;
									   Temp.y = T.S.yy;
									   if ( Check( Temp, T.D+1 ) )
	                                   Kol.push( Para( Temp, T.D+1 ) );
			                         }
			if ( Przejsc( T.S, 1 ) ) { Temp = T.S;
			                           Temp.x = T.S.bx;
									   Temp.y = T.S.by;
									   if ( Check( Temp, T.D+1 ) )
	                                   Kol.push( Para( Temp, T.D+1 ) );
			                         }
			Temp = T.S;
			for (int i=0;i<2;i++)
				for (int j=0;j<4;j++)
				{
					Strzel( Temp, i, j );
					if ( Check( Temp, T.D ) )
					Kol.push( Para( Temp, T.D ) );
				}
		}
		if (Best == -1)
			printf("Case #%d: THE CAKE IS A LIE\n",L);
		else
			printf("Case #%d: %d\n",L,Best);
	}

	return 0;
}
