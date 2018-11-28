#include<cstdio>
#include<cstdlib>
#include<map>
#include<cstring>

using namespace std;

map<char, char> M;
char S[1000000];
char T[1000000];

int main(){
    freopen("A.out","w",stdout);
    int nS;
    scanf("%d",&nS);
    gets(S);

    bool hashS[26] = {false};
    bool hashT[26] = {false};

    for(int i=0;i<nS;i++){
        gets(S); //ori
        gets(T); //to
        int len = strlen(S);
        for(int j=0;j<len;j++){
            M[S[j]] = T[j];
            hashS[S[j]-'a'] = true;
            hashT[T[j]-'a'] = true;
        }
    }

    for(int i=0;i<26;i++){
        if(!hashS[i]) printf("S: %c\n",i+'a');
        if(!hashT[i]) printf("T: %c\n",i+'a');
    }

    scanf("%d",&nS);
    gets(S);
    for(int i=0;i<nS;i++){
        gets(S); //ori
        printf("Case #%d: ",i+1);
        int len = strlen(S);
        for(int j=0;j<len;j++){
            printf("%c",M[S[j]]);
        }
        printf("\n");
    }


}
