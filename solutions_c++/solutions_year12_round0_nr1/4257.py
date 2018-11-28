//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

#define For(i, n) for(int i = 0; i<(n); ++i)
#define ForEach(it, i) for(typeof i.begin() it = i.begin(); it!=i.end(); ++it)

typedef long long ll;
typedef pair<int, int> pii;

char key[] = "YHESOCVXDUIGLBKRZTNWJPFMAQ";
int N;
char ch;
int main(){
    scanf("%d ",&N);
    For(i,N){
        printf("Case #%d: ",i+1);
        while((scanf("%c",&ch)>0) && (ch!='\n')) {
            printf("%c",(ch==' ')?ch:key[ch-'a']+32);
        }
        printf("\n");
    }

}
