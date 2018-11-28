#include<iostream>

using namespace std;

FILE *fin = freopen("A-large.in","r",stdin);
FILE *fout = freopen("probA.out","w",stdout);

int mat[101][101];
double WP[101];
double OWP[101];
double OOWP[101];
int games[101];
int wins[101];

void calcWP(int N) {
    for(int i=0;i<N;i++) {
        WP[i]=(double)wins[i]/games[i];
    }
}

void calcOWP(int N) {
    for(int i=0;i<N;i++) {
        OWP[i]=0;
        double l=0;
        for(int j=0;j<N;j++) {
            if(mat[i][j]!=2) {
                if(mat[j][i]==1)
                    l+=(double)(wins[j]-1)/(games[j]-1);
                else
                    l+=(double)(wins[j])/(games[j]-1);
            }
        }
        OWP[i]=l/games[i];
    }
}

void calcOOWP(int N) {
    for(int i=0;i<N;i++) {
        OOWP[i]=0;
        double l=0;
        for(int j=0;j<N;j++) {
            if(mat[i][j]!=2) {
                l+=OWP[j];
            }
        }
       OOWP[i]=l/games[i];
    }
}
int main() {
    int T;
    cin>>T;
    for(int t = 0;t<T;t++)
    {
        int N;
        cin>>N;
        int i,j;
        for(i=0;i<N;i++){
            wins[i]=games[i]=0;
            for(j=0;j<N;j++) {
                char c;
                cin>>c;
                if(c=='.')
                    mat[i][j]=2;
                else{
                    games[i]++;
                    if(c=='0')
                        mat[i][j]=0;
                    if(c=='1')
                        { mat[i][j]=1;wins[i]++;}
                }

            }
            cin.get();
        }

        calcWP(N);

        calcOWP(N);

        calcOOWP(N);

        cout<<"Case #"<<(t+1)<<":\n";
        for(i=0;i<N;i++) {
            double RPI = 0;
            RPI = 0.25*WP[i] + 0.5*OWP[i] + 0.25*OOWP[i];
            printf("%0.6f\n",RPI);
        }
    }
    return 0;
}
