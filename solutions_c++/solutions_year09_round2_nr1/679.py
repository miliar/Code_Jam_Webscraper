#include <iostream>
#include <string>
#include <sstream>
using namespace std;
string s,fr[110][110];
char ch;
struct tree{
    string tr;
    double p;
    bool leaf;
}T[1000000];
void dfs(int pos){
    string s;
    scanf("%lf",&T[pos].p);
    while(scanf("%c",&ch) != EOF && (ch == ' ' || ch == '\n'));
    if(ch != ')'){
        s = ch;
        while(scanf("%c",&ch) != EOF && ch >= 'a' && ch <= 'z')
            s += ch;
        T[pos].tr = s;
        while(scanf("%c",&ch) != EOF && ch != '(' && ch != ')');
    }
    if(ch == '('){
        T[pos].leaf = 0;
        dfs(pos*2+1);
        while(scanf("%c",&ch) != EOF && ch != '(');
        dfs(pos*2+2);
        while(scanf("%c",&ch) != EOF && ch != ')');
    }
    else T[pos].leaf = 1;
}
double go(int pos,int k,int m,double p){
    p *= T[pos].p;
    if(T[pos].tr == ""){
        if(T[pos].leaf) return p;
        else return go(pos*2+2,k,m,p);
    }
    bool flag(0);
    for(int j = 0;j < m && !flag;++j)
        if(fr[k][j] == T[pos].tr) flag = 1;
    if(flag) return go(pos*2+1,k,m,p);
    else return go(pos*2+2,k,m,p);
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int N;
    cin >> N;
    for(int I = 1;I <= N;++I){
        for(int i = 0;i < 1000;++i) T[i].tr = "";
        printf("Case #%d:\n",I);
        int n,m;
        scanf("%d",&n);
        while(scanf("%c",&ch) != EOF && ch != '(');
        dfs(0);
        cin >> n;
        for(int i = 0;i < n;++i){
            cin >> s;
            cin >> m;
            for(int j = 0;j < m;++j)
                cin >> fr[i][j];
            printf("%.7lf\n",go(0,i,m,1.0));
        }
    }
}
