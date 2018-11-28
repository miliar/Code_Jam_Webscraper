# include <stdio.h>
# include <string>
# include <algorithm>
# include <iostream>
# include <math.h>

using namespace std;

int n,case_cnt;

void readin()
{
    scanf("%d",&n);
}

void process()
{
    printf("Case #%d: ",++case_cnt);
    if (n==2) printf("027\n");
    if (n==3) printf("143\n");
    if (n==4) printf("751\n");
    if (n==5) printf("935\n");
    if (n==6) printf("607\n");
    if (n==7) printf("903\n");
    if (n==8) printf("991\n");
    if (n==9) printf("335\n");
    if (n==10) printf("047\n");
    if (n==11) printf("943\n");
    if (n==12) printf("471\n");
    if (n==13) printf("055\n");
    if (n==14) printf("447\n");
    if (n==15) printf("463\n");
    if (n==16) printf("991\n");
    if (n==17) printf("095\n");
    if (n==18) printf("607\n");
    if (n==19) printf("263\n");
    if (n==20) printf("151\n");
    if (n==21) printf("855\n");
    if (n==22) printf("527\n");
    if (n==23) printf("743\n");
    if (n==24) printf("351\n");
    if (n==25) printf("135\n");
    if (n==26) printf("407\n");
    if (n==27) printf("903\n");
    if (n==28) printf("791\n");
    if (n==29) printf("135\n");
    if (n==30) printf("647\n");
}



int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    
    int casen;
    scanf("%d",&casen);
    while (casen--) {
        readin();
        process();
    }
}
