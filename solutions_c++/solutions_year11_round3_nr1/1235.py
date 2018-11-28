#include<cstdio>
#include<string>
#include<cstdlib>
#include<cstring>
#include<iostream>

#define MAX 100

using namespace std;

int main(){
    bool ok;
    int C,L,T;
    char str[MAX][MAX];

    char ch[] = "\\";

    scanf("%d\n",&T);
    for(int t = 1; t <= T; t++){
        scanf("%d %d\n",&L,&C);
        cout<<"Case #"<<t<<":"<<endl;

        ok = true;
        memset(str,'.',sizeof(str));
        for(int i = 0; i < L; i++){
            scanf("%s\n",str[i]);
        }
        for(int i = 0; i < L-1; i++){
            for(int j = 0; j < C-1; j++){
                if(str[i][j] == '#'){
                    if(str[i][j+1] != '#' || str[i+1][j] != '#' || str[i+1][j+1] != '#'){
                        ok = false;
                        cout<<"Impossible"<<endl;
                        goto VAZA;
                    }
                    str[i][j] = '/'; str[i][j+1] = char(92);
                    str[i+1][j] = char(92); str[i+1][j+1] = '/';
                }
            }
            if(str[i][C-1] == '#'){
                ok = false;
                cout<<"Impossible"<<endl;
                goto VAZA;
            }
        }
        for(int i = 0; i < C; i++)
            if(str[L-1][i] == '#'){
                ok = false;
                cout<<"Impossible"<<endl;
                break;
            }
VAZA:
        if(ok == true){
            for(int i = 0; i < L; i++){
                cout<<str[i]<<endl;
            }
        }
    }
	return 0;
}
