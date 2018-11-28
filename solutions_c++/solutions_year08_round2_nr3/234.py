#include <stdio.h>

int tab[1000000];
int s[1000000];
int run() {
    int n, size;

    scanf("%d %d", &size, &n);

    for(int i=0;i<n;i++)
        scanf("%d", &tab[i]);

    for(int i=0;i<size;i++)
        s[i] = 0;

    int pos = -1;

    for( int x=0;x<size;x++ ){
        int a = x+1;
        
        for(int y=0;y<a;y++) {
            pos = (pos+1) % size;
            while (s[pos])
                pos = (pos+1)%size;
        }
        s[pos] = a;
    }
    
    for( int i=0;i<n;i++)
       printf("%d ", s[tab[i]-1] );
    printf("\n");
    return 0;
}

int main(){
    int n;

    scanf("%d", &n );
    for( int i=0;i<n;i++){
        printf("Case #%d: ",i+1 );
        run();
    }

    return 0;
}
