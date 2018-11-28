#include<stdio.h>
#include<string>
#include<vector>
#include<utility>
#include<algorithm>
using namespace std;

int B[1005];
int E[1005];
int w[1005];

vector< pair <int, int> > aa;

int main(){
    int T, g, i;
    int X, S, R, t, N;
    scanf("%d ", &T);
    for(g=1; g<=T; g++){
        scanf("%d %d %d %d %d ", &X, &S, &R, &t, &N);
        for(i=0; i<N; i++)
            scanf("%d %d %d ", &B[i], &E[i], &w[i]);
        aa.clear();
        int soma=0;
        for(i=0; i<N; i++){
            pair <int, int> p;
            p.first = w[i];
            p.second = E[i]-B[i];
            aa.push_back(p);
            soma+=p.second;
        }
        pair <int, int> q;
        q.first=0;
        q.second = X-soma;
        aa.push_back(q);
        sort(aa.begin(), aa.end());
        double sobra=(double)t;
        double total=0;
        for(i=0; i<=N; i++){
            double temp;
            double yes;
            temp = ((double)aa[i].second)/((double)(aa[i].first+R));
            if(temp<=sobra){
                sobra=sobra-temp;
                total += temp;
            }
            else{
                yes = ((double)aa[i].second - sobra*(aa[i].first+R));
                yes =  yes/(double)(aa[i].first+S);
                total = total + sobra+ yes;
                sobra=0;
            }
        }
        printf("Case #%d: ", g);
        printf("%lf\n", total);
    }
    return 0;
}
