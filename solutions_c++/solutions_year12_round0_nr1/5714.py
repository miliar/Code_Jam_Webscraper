#include <cstdio>
#include <cstring>

using namespace std;

int main(){
    long t,i,j,k,l,cas=1;
    char temp[105];
    char o[] = "yhesocvxduiglbkrztnwjpfmaq";
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);

    scanf("%ld",&t);
    getchar();

    while(t--){
        gets(temp);
        printf("Case #%ld: ",cas++);
        for(i = 0; temp[i]; i++){
            if(temp[i] >= 'a' && temp[i] <= 'z' ){
                printf("%c",o[temp[i]-'a']);
            }
            else{
                printf("%c",temp[i]);
            }
        }
        printf("\n");
    }

    return 0;
}
