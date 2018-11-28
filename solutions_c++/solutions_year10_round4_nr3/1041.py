#include <iostream>
#define MAX 110

using namespace std;

bool T[MAX][MAX]={};
bool T2[MAX][MAX]={};

void kopiuj() { for (int i=0; i<MAX; ++i) for (int j=0; j<MAX; ++j) T[i][j]=T2[i][j]; }

int main()
{
    ios_base::sync_with_stdio(0);
    
    int C;
    cin>>C;
    
    for (int test=1; test<=C; ++test)
    {
        for (int i=0; i<MAX; ++i) for (int j=0; j<MAX; ++j) T[i][j]=0;
        
        int R;
        cin>>R;
        for (int i=1; i<=R; ++i)
        {
            int X1,Y1,X2,Y2;
            cin>>X1>>Y1>>X2>>Y2;
            
            if (X1>X2) swap(X1,X2);
            if (Y1>Y2) swap(Y1,Y2);
            
            for (int X=X1; X<=X2; ++X)
            {
                for (int Y=Y1; Y<=Y2; ++Y) T2[X][Y]=T[X][Y]=1;
            }
        }
        
        int licznik=0;
        
        while (1)
        {
            bool koniec=true;
            for (int i=1; i<MAX; ++i)
			{
				for (int j=1; j<MAX; ++j)
				{
					if (T[i][j]==1) koniec=false;
				}
			}
            if (koniec) break;
            
            ++licznik;
            
            for (int i=1; i<MAX; ++i)
			{
				for (int j=1; j<MAX; ++j)
				{
					if (T[i-1][j]==0 && T[i][j-1]==0) T2[i][j]=0;
					else if (T[i-1][j] && T[i][j-1]) T2[i][j]=1;
				}
			}
			kopiuj();
        }
        
        cout<<"Case #"<<test<<": "<<licznik<<endl;
    }

    return 0;
}
