#include <iostream>
#include <stdio.h>

using namespace std;

int main(){

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int M[110][110];
    int memo[110][5];
    double WP[110],OWP[110], OOWP[110], RPI[110];

    //char in[110][110];
    int T;
    cin >> T;
    for(int ts=1;ts<=T;ts++){
        printf("Case #%d:\n",ts);

        int N;
        cin >> N;

        for(int i=1;i<=N;i++){
            memo[i][1]=0;
            memo[i][2]=0;
        }

        char c;
        for(int i=1;i<=N;i++)
        for(int j=1;j<=N;j++){
            cin >> c;
            if(c=='1') {M[i][j]=1;memo[i][1]++;}
            if(c=='0') {M[i][j]=-1;memo[i][2]++;}
            if(c=='.') M[i][j]=0;
        }

        for(int i=1;i<=N;i++){
            int temp = memo[i][1]+memo[i][2];
            if(temp==0) WP[i]=0;
            else
            WP[i]=(double)memo[i][1]/(double)temp;
        }

        for(int i=1;i<=N;i++){
            double temp=0;
            double counter = 0;
            for(int j=1;j<=N;j++){
                if(M[i][j]==0) continue;
                counter++;
                double var1=memo[j][1];
                double var2=memo[j][2];
                if(M[j][i]==-1) var2--;
                if(M[j][i]==1) var1--;
                if(var2+var1==0) continue;
                temp+=(var1/(var1+var2));
            }
            if(counter==0) OWP[i]=0;
            else{
            temp/=(double)counter;
            OWP[i]=temp;}

        }

        for(int i=1;i<=N;i++){
            double temp=0;
            double counter = 0;
            for(int j=1;j<=N;j++){
                if(M[i][j]==0) continue;
                counter++;
                temp+=OWP[j];
            }
            if(counter==0) OOWP[i]=0;
            else{
            temp/=(double)counter;
            OOWP[i]=temp;
            }
           // cout<<OOWP[i]<<endl;
        }

        for(int i=1;i<=N;i++){
            RPI[i]=0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
            //cout<<RPI[i]<<endl;
            printf("%.12lf\n",RPI[i]);
        }


    }

    return 0;
}
