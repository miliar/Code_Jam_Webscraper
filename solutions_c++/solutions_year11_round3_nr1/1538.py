#include<iostream>

using namespace std;

FILE *fin = freopen("A-large.in","r",stdin);
FILE *fout = freopen("probA.out","w",stdout);

int no;
char mat[51][51];

void fill(int i,int j,int R,int C) {
    if(i+1>=R || j+1>=C) return;
    if(mat[i][j]=='#' && mat[i][j+1]=='#' && mat[i+1][j]=='#' && mat[i+1][j+1]=='#') {
        mat[i][j]='/';
        mat[i][j+1]='\\';
        mat[i+1][j]='\\';
        mat[i+1][j+1]='/';
        no-=4;
        fill(i,j+1,R,C);
        fill(i+1,j,R,C);
        fill(i+1,j+1,R,C);
    }
}

int main() {
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
        int R,C;
        cin>>R>>C;
        no = 0;
        int i,j;
        for(i=0;i<R;i++) {
            for(j=0;j<C;j++)
            {
                char c;
                cin>>c;
                if(c=='#') no++;
                mat[i][j]=c;
            }
            cin.get();
        }

        for(i=0;i<R;i++)
            for(j=0;j<C;j++)
                fill(i,j,R,C);
        cout<<"Case #"<<(t+1)<<":\n";
        if(!no) {
            for(i=0;i<R;i++) {
                for(j=0;j<C;j++)
                {
                    cout<<mat[i][j];
                }
                cout<<"\n";
            }
        }
        else {
            cout<<"Impossible\n";
        }

    }
    return 0;
}
