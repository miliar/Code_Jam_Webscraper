#include <iostream>
#include <stack>
using namespace std;
int Case,n,c,d,p;
char fc[40][5],fd[40][5],s[110];
stack<char> Q;
bool bomb()
{
     for (int i=1;i<=d;i++)
         if (s[p-1]==fd[i][0] || s[p-1]==fd[i][1]) {
            char ch=(s[p-1]==fd[i][0])?fd[i][1]:fd[i][0];
            for (int j=0;j<p-1;j++)
                if (ch==s[j]) return true;
            }
     return false;
}
bool change()
{
     for (int i=1;i<=c;i++)
         if ((s[p-1]==fc[i][0] && s[p-2]==fc[i][1])||
            (s[p-1]==fc[i][1] && s[p-2]==fc[i][0])) {
            p-=2;
            Q.push(fc[i][2]);
            return true;
            }
     return false;
}
void display()
{
     scanf("%d",&Case);
     for (int ca=1;ca<=Case;ca++) {
         scanf("%d",&c);
         for (int i=1;i<=c;i++)
             scanf("%s",fc[i]);
         scanf("%d",&d);
         for (int i=1;i<=d;i++)
             scanf("%s",fd[i]);
         scanf("%d%s",&n,s);
         while (!Q.empty()) Q.pop();
         for (int i=n-1;i>=0;i--) Q.push(s[i]);
         p=0;
         while (!Q.empty()) {
               s[p++]=Q.top();
               Q.pop();
               if (p==1) continue;
               if (change()) continue;
               if (bomb()) p=0;
               }
         printf("Case #%d: [",ca);
         if (p!=0) {
            printf("%c",s[0]);
            for (int i=1;i<p;i++)
                printf(", %c",s[i]);
            }
         printf("]\n");
     }
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    display();
    //while(1);
    return 0;
}
