#include<iostream>
const  int  a[40]  =  {0,  5,  27,  143,  751,  935,  607,  903,  991,  335,  47,  943,  471,  55,  447,  463,  991,95,  607,  263,  151,  855,  527,  743,  351,  135,  407,  903,  791,  135,  647};  
int main(){
    int cnt;
    freopen("c.out","w",stdout);
    scanf("%d", &cnt);
    for (int t = 1; t <= cnt; t++){
        int n;
        scanf("%d", &n);
        printf("Case #%d: %03d\n", t, a[n]);
    }
}
    
