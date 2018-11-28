#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>



using namespace std;

struct point{
   double p;
   char s[100];
   point *left, *right;
}*root;

char s[10000];
char ss[1000][100];
char tt[100];
int t, k;
int l, qqqq = 0;


void read(point *p){
    p->p = 0;
    memset(p->s, 0, sizeof(100));
    p->left = p->right = 0;
    char c;
    cin >> c >> p->p >> p->s;
    int k = strlen(p->s);
    while(k > 0 && p->s[ k - 1] == ')'){
      p->s[k - 1] = '\0';
      --k;
      ++qqqq;
    }
    if (qqqq){
       --qqqq;
       return;
    }
    gets(s);
    k = strlen(s);
    for (int i = 0; i < k; ++i) if (s[i] == ')') ++qqqq;
    if (qqqq){ 
       --qqqq;
       return;
    }

    p->left = new point;
    read(p ->left);
    p->right = new point;
    read(p ->right);

    if (qqqq){
       --qqqq;
       return;
    }
    cin >> s;
    k = strlen(s);
    for (int i = 0; i < k; ++i) if (s[i] == ')') ++qqqq;
    --qqqq;
}

void print(point *p){
   cout << p -> p << " " << p -> s << " " << p -> left << " " << p -> right << endl;
   if (p -> left) print(p -> left);
   if (p -> right) print(p -> right);
}

void del(point *p){
   if (p -> left) del(p->left);
   if (p -> right) del(p -> right);
   delete p;
}

double check(point *p){
   if (p -> left == NULL) return p->p;
   int flag = false;
   for (int i = 0; i < k; ++i){
       if (strcmp(ss[i], p -> s) == 0){
          flag = true;
          break;
       }
   }
   if (flag) return p->p * check(p -> left);
   return p -> p * check(p -> right);

}
int a;

int main(){
cin >> t;
for (int _i = 0; _i < t; ++_i){

    root = new point;
    cin >> l;
    read(root);

    cin >> a;
    cout << "Case #" << _i + 1 << ":" << endl;
    for (int i = 0; i < a; ++i){
        cin >> s;
        cin >> k;
        for (int i = 0; i < k; ++i){
            cin >> ss[i];
        }
        printf("%.7lf\n", check(root));
    }
    del(root);
}
    return 0;
}