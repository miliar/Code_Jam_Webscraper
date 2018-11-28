#include<cstdio>


int t ;
char a[5][5] ;
bool fin = true,xwin,owin;
int main(){

    freopen ("A-large.in","r",stdin);
    freopen("2.sol","w",stdout);
    scanf("%d",&t);

    for(int tt = 1 ;tt <= t; tt++){
        fin = true ,xwin = false ,owin = false ;

        for(int i = 0 ; i < 4 ; i ++)
            scanf("%s",a[i]);

        for(int i = 0 ; i < 4 ; i ++){
            int cx = 0 , co = 0 ;
            for(int j = 0 ; j < 4 ; j ++){
                if(a[i][j] == 'X') cx++;
                else if(a[i][j] == 'O') co ++;
                else if(a[i][j] == 'T') cx ++ , co ++ ;
                else fin = false ;
            }
            if(cx == 4) xwin = true ;
            if(co == 4) owin = true ;
        }

        for(int j = 0 ; j < 4 ; j ++){
            int cx = 0 , co = 0 ;
            for(int i = 0 ; i < 4 ; i ++){
                if(a[i][j] == 'X') cx++;
                else if(a[i][j] == 'O') co ++;
                else if(a[i][j] == 'T') cx ++ , co ++ ;
                else fin = false ;
            }
            if(cx == 4) xwin = true ;
            if(co == 4) owin = true ;
        }

        for(int j = 0 ; j < 1 ; j ++){
            int cx = 0 , co = 0 ;
            for(int i = 0 ; i < 4 ; i ++){
                if(a[i][i] == 'X') cx++;
                else if(a[i][i] == 'O') co ++;
                else if(a[i][i] == 'T') cx ++ , co ++ ;
                else fin = false ;
            }
            if(cx == 4) xwin = true ;
            if(co == 4) owin = true ;
        }

        for(int j = 0 ; j < 1 ; j ++){
            int cx = 0 , co = 0 ;
            for(int i = 0 ; i < 4 ; i ++){
                if(a[i][3-i] == 'X') cx++;
                else if(a[i][3-i] == 'O') co ++;
                else if(a[i][3-i] == 'T') cx ++ , co ++ ;
                else fin = false ;
            }
            if(cx == 4) xwin = true ;
            if(co == 4) owin = true ;
        }




        if(xwin and not owin) printf("Case #%d: X won\n",tt);
        else if(owin and not xwin) printf("Case #%d: O won\n",tt);
        else if(not xwin and not owin and not fin) printf("Case #%d: Game has not completed\n",tt);
        else printf("Case #%d: Draw\n",tt);
    }
}
