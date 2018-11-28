#include<iostream>
using namespace std;
int main()
{
    const int num[31]={0,5,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
    int casen;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    scanf("%d",&casen);
    int n;
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d",&n);
        printf("Case #%d: %03d\n",casei,num[n]);
    }
    return 0;
}
