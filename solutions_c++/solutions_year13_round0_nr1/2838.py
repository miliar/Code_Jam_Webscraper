//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)
#define eps 1e-9

typedef long long ll;
typedef pair<int, int> pii;

char s[20][20];
char p[] = "0X";

int dx[] = {0,1,1, 1, 0,-1,-1,-1};
int dy[] = {1,1,0,-1,-1,-1, 0, 1};

int extra(){
    For(i,4) scanf("%s", s[i+8]+8);
    int full = 1;
    For(i,4) For(j,4) For(d,4) {
        int p1 = 1, p2 = 1;
        For(x,4){
            if (s[8+i+dx[d]*x][8+j+dy[d]*x] == '.')
                p1 = p2 = full = 0;
            if (s[8+i+dx[d]*x][8+j+dy[d]*x] < '.')
                p1 = p2 = 0;
            if (s[8+i+dx[d]*x][8+j+dy[d]*x] == 'O')
                p2 = 0;
            if (s[8+i+dx[d]*x][8+j+dy[d]*x] == 'X')
                p1 = 0;
        }
        if (p1){ 
            printf("O won\n");
            return 0;
        }
        if (p2) {
            printf("X won\n");
            return 0;
        }
    }
    if (full){
        printf("Draw\n");
    }else{
        printf("Game has not completed\n");
    }

}

int main(){
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
