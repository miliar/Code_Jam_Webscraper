#include<iostream>
using namespace std;

void Dfs( int ps, int *d, int h, int w, char *s, char c ){
    if( s[ps]!='$' ) return;
    s[ps] = c;
    if( d[ps] != -1 ) Dfs( d[ps], d, h, w, s, c );
    if( ps>=w && d[ps-w]==ps ) Dfs( ps-w, d, h, w, s, c );
    if( ps%w!=0 && d[ps-1]==ps ) Dfs( ps-1, d, h, w, s, c );
    if( ps%w!=w-1 && d[ps+1]==ps ) Dfs( ps+1, d, h, w, s, c );
    if( ps+w<h*w && d[ps+w]==ps ) Dfs( ps+w, d, h, w, s, c ); 
}

int main(){
    freopen("input.in","r",stdin);
    freopen("acm.out","w",stdout);
    int t, h, w, m[10008], d[10008];
    char s[10008];
    scanf("%d",&t);
    for(int r=1; r<=t; r++){
        scanf("%d%d",&h,&w);
        int k = h*w;
        for(int i=0; i<k; i++) scanf("%d",&m[i]);
        for(int i=0; i<k; i++){
            d[i] = -1;
            int lw = m[i];
            if( i>=w && lw>m[i-w] ){ lw = m[i-w]; d[i] = i-w; }
            if( i%w !=0 && lw>m[i-1] ){ lw = m[i-1]; d[i] = i-1; }
            if( i%w != w-1 && lw>m[i+1] ){ lw = m[i+1]; d[i] = i+1; }
            if( i+w<h*w && lw>m[i+w] ){ lw = m[i+w]; d[i] = i+w; }
            //printf("%d\n",d[i]);
        }
        for(int i=0; i<k; i++) s[i] = '$';
        char c = 'a';
        for(int i=0; i<k; i++){
            if( s[i]=='$' ){ Dfs( i, d, h,w, s, c ); c++; }
        }    
        printf("Case #%d:",r);
        for(int i=0; i<k; i++){
            if( i%w==0 ) printf("\n");
            else printf(" ");
            printf("%c",s[i]);
        }
        printf("\n");
    }
    return 0;
}
