#include<cstdio>

int n;
char table[110][110];

double findWP(int r) {
    double wp=0.0,win=0.0,total=0.0;
    for(int i=0;i<n;i++) {
        if(table[r][i]!='.') {
            total++;
        }
        if(table[r][i]=='1') {
            ++win;
        }
    }
    wp=win/total;
    return wp;
}

double findWP(int r,int t) {
    double wp=0.0,win=0.0,total=0.0;
    for(int i=0;i<n;i++) {
        if(table[r][i]!='.' && i!=t) {
            total++;
        }
        if(table[r][i]=='1' && i!=t) {
            ++win;
        }
    }
    wp=win/total;
    return wp;
}

double findOWP(int r) {
    double count=0.0;
    double ans=0.0;
    for(int i=0;i<n;i++) {
        if(table[r][i]!='.') {
            ++count;
            ans+=findWP(i,r);
        }
    }
    return ans/count;
}

double findOOWP(int r) {
    double count=0.0;
    double ans=0.0;
    for(int i=0;i<n;i++) {
        if(table[r][i]!='.') {
            ++count;
            ans+=findOWP(i);
        }
    }
    return ans/count;
}

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    double rpi;
    int t;
    scanf("%d\n",&t);
    for(int i=0;i<t;i++) {
        scanf("%d\n",&n);
        for(int j=0;j<n;j++) {
            scanf("%s",table[j]);
            //printf("%s\n",table[j]);
        }
        printf("Case #%d:\n",i+1);
        for(int j=0;j<n;j++) {
            rpi=0.25*findWP(j)+0.5*findOWP(j)+0.25*findOOWP(j);
            printf("%.7lf\n",rpi);
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
