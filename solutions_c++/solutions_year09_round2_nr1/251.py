#include<stdio.h>
#include<string.h>
#include<string>
#include<stdlib.h>
using namespace std;

struct node{
    double wg;
    string s;
    int ls, rs;
}tree[300000];

char ts[30000];
int cas, N, L, A, m, tn, sn;

void readdata()
{
     int i, j;
     char t[300];
     scanf("%d", &L);
     gets(t);
     for (i=sn=0;i<L;i++){
         memset(t, 0, sizeof(t));
         gets(t);
         //printf("t=%s\n", t);
         for (j=0;t[j];j++){
             if (t[j] == '('){
                ts[sn++] = '(';
                ts[sn++] = ' ';
             }
             if (t[j] >= '0' && t[j] <= '9' || t[j] == '.' 
              || t[j] >= 'a' && t[j] <= 'z' || t[j] == ' '){
                ts[sn++] = t[j];
             }
             if (t[j] == ')'){
                ts[sn++] = ' ';
                ts[sn++] = ')';
             }
         }
     }
     //printf("ts = %s\n", ts);
}

double getNextDouble(int &id)
{
    int i, len = 0;
    double ret = 0;
    char t[100];
    memset(t, 0, sizeof(t));
    for (i=id;i<sn;i++)
       if (ts[i]>='0' && ts[i]<='9') break;
    //printf("1i=%d ts[i]=%c\n", i, ts[i]);
    for (;;i++){
       if (ts[i]>='0' && ts[i]<='9' || ts[i]=='.') t[len++] = ts[i];
       else break;
    }
    //printf("1i=%d ts[i]=%c\n", i, ts[i]);
    id = i;
    sscanf(t, "%lf", &ret);
    //printf("ret = %lf\n", ret);
    return ret;
}

string getNextString(int &id)
{
    int i;
    string ret = "";
    for (i=id;i<sn;i++){
        if (ts[i] == '(' || ts[i] >='a' && ts[i] <= 'z') break;
    }
    //printf("i=%d ts[i]=%c\n", i, ts[i]);
    while (ts[i] >= 'a' && ts[i] <= 'z') ret += ts[i++];
    //printf("i=%d ts[i]=%c\n", i, ts[i]);
    //printf("ret = %s\n", ret.c_str());
    return ret;
}

void findNext(int &s, int &t)
{
    int i, c;
    for (i=s; ;i++)
        if (ts[i] == '(') break;
    c = 1;
    s = i;
    while (c){
        i++;
        if (ts[i] == '(') c++;
        if (ts[i] == ')') c--;
    }
    t = i;
}

void buildTree(int nd, int st, int ed)
{
    int i, s, t, bg = st;
    
    tree[nd].wg = getNextDouble(bg);
    tree[nd].ls = tree[nd].rs = -1;
    tree[nd].s = getNextString(bg);
    if (tree[nd].s != ""){
        s = bg;
        findNext(s, t);
        tn++;
        tree[nd].ls = tn;
        buildTree(tn, s, t);
        tn++;
        tree[nd].rs = tn;
        s = t + 1;
        findNext(s, t);
        buildTree(tn, s, t);
    }
}

void showTree()
{
    int i;
    for (i=0;i<=tn;i++)
       printf("i=%d, w=%lf, s=%s, ls=%d, rs=%d\n", i, 
       tree[i].wg, tree[i].s.c_str(), tree[i].ls, tree[i].rs);
}

void work()
{
    string s[300];
    char st[300];
    int nd, i, c, ok;
    scanf("%s", st);
    scanf("%d", &c);
    for (i=0; i<c;i++){
        memset(st, 0, sizeof(st));
        scanf("%s", st);
        s[i] = st;
    }
    nd = 0;
    double ans = 1.0;
    while (nd != -1){
        ans *= tree[nd].wg;
        for (ok=i=0;i<c;i++)
            if (tree[nd].s == s[i]) ok = 1;
        if (ok) nd = tree[nd].ls;
        else nd = tree[nd].rs;
    }
    printf("%.6lf\n", ans);
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &N);
    for (cas = 1; cas <= N; cas++){
        memset(ts, 0, sizeof(ts));
        readdata();
        buildTree(0, 0, sn);
       // showTree();
        scanf("%d", &A);
        printf("Case #%d:\n", cas);
        while (A--){
            work();
        }
    }
}
