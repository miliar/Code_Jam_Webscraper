#include <iostream>
using namespace std;
int L,d,n;
string a[5010];
bool kt[30][20];

void nhap(void) {
     scanf("%d%d%d\n",&L,&d,&n);
     int i,j;
     char ch;
     for (i=1;i<=d;i++) getline(cin,a[i]);
};

void khoitao(string s) {
     int i,j,dem,tam,k;
     i=0;
     dem=0;
     memset(kt,false,sizeof(kt));
     k=s.length();
     while (i<k) {
           dem++;
           if (s[i]=='(') {
              for (j=i+1;j<k;j++) {
                  if (s[j]==')') break;
                  tam=int(s[j])-96;
                  kt[tam][dem]=true;
              };
              i=j+1;
           }
           else {
                tam=int(s[i])-96;
                kt[tam][dem]=true;
                i++;
           };
     };
};

int count(string s) {
    int i,j,kq=0;
    for (i=1;i<=d;i++) {
        bool check;
        check=true;
        for (j=0;j<L;j++)
            if (kt[int(a[i][j])-96][j+1]==false) {check=false; break;};
        if (check==true) kq++;
    };
    return kq;
};

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i,t;
    string s;
    nhap();
    for (i=1;i<=n;i++) {
        printf("Case #%d: ",i);
        getline(cin,s);
        khoitao(s);
        printf("%d\n",count(s));
    };
    return 0;
};
