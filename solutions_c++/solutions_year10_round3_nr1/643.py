#include<cstdio>
int n,t;
struct pair{
    int a;
    int b;
};
int c;
pair w[1000];
int main (){
    scanf("%d", &t);
    for(int q=1; q<=t; q++){
        c=0;
        scanf("%d", &n);
        for(int i=0; i<n; i++)
            scanf("%d%d",&w[i].a,&w[i].b);
        for(int i=0; i<n; i++)
            for(int j=0; j<n; j++)
                if((i!=j)&&((w[i].a>w[j].a&&w[i].b<w[j].b)||(w[i].a<w[j].a&&w[i].b>w[j].b)))
                    c++;
        printf("Case #%d: %d\n",q,c/2);
	}
}
