#include<stdio.h>
#include<stdlib.h>
#include<string.h>
main(){
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out","w",stdout);

    int bsp[31] = {-1,-1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,-1,-1};
    int bns[31] = {0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
    
	int t;
	scanf("%d", &t);
	for(int a=0; a<t; a++){
        
    	int n,s,p;
        scanf("%d%d%d", &n, &s, &p);
        int ti[n];
        for(int i=0; i<n; i++) 
            scanf("%d", &ti[i]);
        int ans=0;
        int sp=0;
        for(int i=0; i<n; i++){
            if(bns[ti[i]]>=p) ans++;
            else if(bsp[ti[i]]>=p && sp<s) {
                 ans++; 
                 sp++;
            }
        }
    
    printf("Case #%d: %d\n", a+1, ans);
    }
//    system("pause");
}
