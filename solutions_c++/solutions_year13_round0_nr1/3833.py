#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int i, j, k, tCase;
    char arr[4][4];
    cin >> tCase;
    for(i=1; i<=tCase; i++)
    {
        int flag=0;
		int p, q;
		p = q = -1;
        for(j=0; j<4; j++)
            for(k=0; k<4; k++)
                {
                    cin >> arr[j][k];
					if(arr[j][k]=='T') p = j, q = k;
                    if(arr[j][k]=='.')
                        flag=1;
                }

            int win=0;

            for(j=0; j<4; j++)
            {
				if(p!=-1 && q!=-1) arr[p][q]='O';
                if(arr[j][0]=='O' && arr[j][1]=='O' && arr[j][2]=='O' && arr[j][3]=='O')
                {
                    win=1;
                    break;
                }
                else if(arr[0][j]=='O' && arr[1][j]=='O' && arr[2][j]=='O' && arr[3][j]=='O')
                {
                    win=1;
                    break;
                }
				if(p!=-1 && q!=-1) arr[p][q]='X';
                if(arr[j][0]=='X' && arr[j][1]=='X' && arr[j][2]=='X' && arr[j][3]=='X')
                {
                    win=2;
                    break;
                }
                else if(arr[0][j]=='X' && arr[1][j]=='X' && arr[2][j]=='X' && arr[3][j]=='X')
                {
                    win=2;
                    break;
                }
				if(p!=-1 && q!=-1) arr[p][q]='T';

            }
			if(p!=-1 && q!=-1) arr[p][q]='O';
            if(arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='O')
                win=1;
            if(arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='O')
                win=1;
			if(p!=-1 && q!=-1) arr[p][q]='X';
            if(arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='X')
                win=2;
            if(arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='X')
                win=2;
			if(p!=-1 && q!=-1) arr[p][q]='T';

            if(flag==1 && win==0)
                win=3;
            if(flag==0 && win==0)
                win=4;

        if(win==1) cout << "Case #" << i << ": O won" << endl;
        if(win==2) cout << "Case #" << i << ": X won" << endl;
        if(win==3) cout << "Case #" << i << ": Game has not completed" << endl;
        if(win==4) cout << "Case #" << i << ": Draw" << endl;

    }
    return 0;

}


