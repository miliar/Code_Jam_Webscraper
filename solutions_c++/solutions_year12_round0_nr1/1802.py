
#include <cstdlib>
#include <cstdio>



int main(int argc, const char * argv[])
{
    char ta[] = "yhesocvxduiglbkrztnwjpfmaq";
    char ia[120];
    int cn;
    int p;
    
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    
    scanf("%d\n", &cn);
    
    for (int ci = 1; ci <= cn; ci++) {
        p = 0;
        gets(ia);
        printf("Case #%d: ", ci);
        while(ia[p] != '\0') {
            if (ia[p] - 'a' >= 0 && ia[p] - 'a' < 26) {
                printf("%c", ta[ia[p] - 'a']);
            }
            else {
                printf("%c", ia[p]);
            }
            ++p;
        }
        printf("\n");
    }
    
    
    return 0;
}

