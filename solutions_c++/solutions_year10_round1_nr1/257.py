#include<stdio.h>

int n, k;
char board[100][100];

void input()
{
    int i;
    scanf("%d%d", &n, &k);
    for(i=0; i<n; i++) scanf("%s", board[i]);
    
//    for(int r=0; r<n; )
}

void move()
{
    int r, c, j;
    
    for(r=n-1; r>=0; r--){
        for(c=n-1; c>=0; c--)
            if(board[r][c]=='.'){
                j=c-1;
                while(j>=0 && board[r][j]=='.') j--;
                if(j<0) break;
                board[r][c]=board[r][j];
                board[r][j]='.';
            }
    }
}

int check()
{
    int redF=0, blueF=0, r, c, i, red, blue;
//    printf("\n");
/*    for(r=0; r<n; r++){
        for(c=0; c<n; c++) printf("%c", board[r][c]);
        printf("\n");
    }
    printf("ok\n");
*/    
    for(r=0; r<n; r++)
        for(c=0; c<n; c++)
            if(board[r][c]!='.'){
                red=blue=0;
                for(i=0; i<k && c+i<n; i++)
                    if(board[r][c+i]=='R') red++;
                    else if(board[r][c+i]=='B') blue++;
                if(red==k) redF=1;
                if(blue==k) blueF=1;
                
                red=blue=0;
                for(i=0; i<k && r+i<n; i++)
                    if(board[r+i][c]=='R') red++;
                    else if(board[r+i][c]=='B') blue++;
                if(red==k) redF=1;
                if(blue==k) blueF=1;
                
                red=blue=0;
                for(i=0; i<k && r+i<n && c-i>=0; i++)
                    if(board[r+i][c-i]=='R') red++;
                    else if(board[r+i][c-i]=='B') blue++;
                if(red==k) redF=1;
                if(blue==k) blueF=1;
                
                red=blue=0;
                for(i=0; i<k && r+i<n && c+i<n; i++)
                    if(board[r+i][c+i]=='R') red++;
                    if(board[r+i][c+i]=='B') blue++;
                if(red==k) redF=1;
                if(blue==k) blueF=1;
            }
            
     if(!redF && !blueF) return 0;
     if(redF && blueF) return 3;
     if(redF) return 1;
     if(blueF) return 2;   
                
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int T, tt, ans;
    
    scanf("%d", &T);
    for(tt=1; tt<=T; tt++){
        printf("Case #%d: ", tt);
        input();
        move();
        ans=check();
        if(ans==0) printf("Neither\n");
        else if(ans==1) printf("Red\n");
        else if(ans==2) printf("Blue\n");
        else printf("Both\n");
    }
    
    return 0;
}
