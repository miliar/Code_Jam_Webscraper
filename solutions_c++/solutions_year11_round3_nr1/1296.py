#include<iostream>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int T,R,C;
    char board[60][60];
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cout<<"Case #"<<t+1<<":"<<endl;
        cin>>R>>C;
        int bcount=0;
        for (int i=0; i<R; i++) {
            cin>>board[i];
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (board[i][j]=='#') {
                    bcount++;
                }
            }
        }
        if (bcount!=0 && bcount%4!=0) {
            cout<<"Impossible"<<endl;
            continue;
        }
        if (bcount==0) {
            for (int i=0; i<R; i++) {
                cout<<board[i]<<endl;
            }
            continue;
        }
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (board[i][j]=='#' && board[i][j+1]=='#' && board[i+1][j]=='#' && board[i+1][j+1]=='#') {
                    board[i][j]=board[i+1][j+1]='/';
                    board[i+1][j]=board[i][j+1]='\\';
                 }
            }
        }
        bcount=0;
        for (int i=0; i<R; i++) {
            for (int j=0; j<C; j++) {
                if (board[i][j]=='#') {
                    bcount++;
                }
            }
        }
        if (bcount!=0) {
            cout<<"Impossible"<<endl;
        }
        else
        {
            for (int i=0; i<R; i++) {
                cout<<board[i]<<endl;
            }
        }
	}
	return 0;
}