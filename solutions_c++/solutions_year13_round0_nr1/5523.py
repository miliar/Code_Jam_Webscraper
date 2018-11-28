
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream cout ("A-small.out");
    ifstream cin ("A-small.in");
    char board[4][4];
    int t;
    while(cin>>t){
        for(int cnt=0;cnt<t;cnt++){
            int win=2;
            int flag=0;
            for(int i=0;i<4;i++)cin>>board[i];
            for(int i=0;i<4;i++){
                char cr0,cr1;
                int c0=0,c1=0;
                int fg0=1,fg1=1;
                for(int j=0;j<4;j++){
                    if(board[i][j]=='.')flag=1;
                    if(j==0){
                        c0++;
                        c1++;
                        cr0=board[i][j];
                        cr1=board[j][i];
                    }else if(board[i][j]!='.'){
                        if(board[i][j]==cr0){
                            c0++;
                        }else if(board[i][j]=='T'&&fg0){
							c0++;
							fg0=0;
						}else if(cr0=='T'){
                            c0++;
                            cr0=board[i][j];
                            fg0=0;
                        }
                        if(board[j][i]==cr1){
                            c1++;
                        }else if(board[j][i]=='T'&&fg1){
							c1++;
							fg1=0;
						}else if(cr1=='T'){
                            c1++;
                            cr1=board[j][i];
                            fg1=0;
                        }
                    }
                    if(j==i&&board[i][j]!='.'){
                        if(board[0][0]==board[1][1]==board[2][2]==board[3][3]&&board[0][0]!='T')
                            win=(board[0][0]=='O'?1:0);
                        else{
							int isit=1;
							int fg2=1;
							char n=board[0][0];
							for(int k=0;k<4;k++){
								if(board[k][k]!=n&&n!='T'&&board[k][k]!='T')isit=0;
								else if(n=='T'){fg2=0;n=board[k+1][k+1];}
								else if(board[k][k]=='T'&&fg2)fg2=0;
								else if(board[k][k]=='T'&&!fg2)isit=0;
							}
							if(isit)win=(n=='O'?1:0);
                        }
                    }
                    if(j==3-i&&board[i][j]!='.'){
						if(board[0][3]==board[1][2]==board[2][1]==board[3][0]&&board[0][3]!='T')
                            win=(board[0][3]=='O'?1:0);
                        else{
							int isit1=1;
							int fg3=1;
							char n2=board[0][3];
							for(int k=0;k<4;k++){
								if(board[k][3-k]!=n2&&n2!='T'&&board[k][3-k]!='T')isit1=0;
								else if(n2=='T'){fg3=0;n2=board[k+1][2-k];}
								else if(board[k][3-k]=='T'&&fg3)fg3=0;
								else if(board[k][3-k]=='T'&&!fg3)isit1=0;
							}
							if(isit1)win=(n2=='O'?1:0);
                        }
                    }
                }
                if(c0==4)win=(cr0=='O'&&cr0!='T'?1:0);
                if(c1==4)win=(cr1=='O'&&cr1!='T'?1:0);
                c0=0;
                c1=0;
            }
            if(win!=2)
            cout<<"Case #"<<cnt+1<<": "<<(win==0?'X':'O')<<" won"<<endl;
            else if(flag)
            cout<<"Case #"<<cnt+1<<": "<<"Game has not completed"<<endl;
            else
            cout<<"Case #"<<cnt+1<<": "<<"Draw"<<endl;
            win=2;
            flag=0;

        }
    }
    return 0;
}
