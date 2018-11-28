#include<cstdio>
#include<list>

using namespace std;


bool co[10][10];
char com[10][10];
bool op[10][10];
char s[10];
int moc[10];

inline int f(char C){
    for(int i=0;i<8;i++)
        if(s[i]==C) return i;

    return 8;
}

void czysc(){
    for(int i=0;i<9;i++)
        for(int j=0;j<9;j++)
            co[i][j]=op[i][j]=false;
}

void czysc2(){
    for(int i=0;i<8;i++) moc[i]=0;
}


int main(){
    sprintf(s,"QWERASDF");
    int z,Z;
    scanf("%d",&z);
    Z=z;
    while(z--){
        czysc();
        czysc2();
        int k; scanf("%d",&k);
        while(k--){
            char A,B,C;
            getchar();
            A=getchar(); B=getchar(); C=getchar();
            co[f(A)][f(B)]=co[f(B)][f(A)]=true;
            com[f(A)][f(B)]=com[f(B)][f(A)]=C;
        }
        scanf("%d",&k);
        while(k--){
            char A,B;
            getchar(); A=getchar(); B=getchar();
            op[f(A)][f(B)]=op[f(B)][f(A)]=true;
        }
        scanf("%d",&k);
        getchar();
        list<char> wynik;
        while(k--){
            char A=getchar();
            if(wynik.empty()){
                moc[f(A)]=1;
                wynik.push_back(A);
            }
            else{
                char B=wynik.back();
                if(co[f(A)][f(B)]){
                    moc[f(B)]--;
                    wynik.pop_back();
                    wynik.push_back(com[f(A)][f(B)]);
                }
                else{
                    bool usuwamy=false;
                    for(int i=0;i<8;i++)
                        if(op[f(A)][i] && moc[i]>0) usuwamy=true;
                    
                    if(usuwamy){
                        wynik.clear();
                        czysc2();
                    }
                    else{
                        wynik.push_back(A);
                        moc[f(A)]++;
                    }
                }
            }
        }
        printf("Case #%d: [",Z-z);
        if(wynik.empty()) printf("]\n");
        else{
            list<char>::iterator it=wynik.begin();
            printf("%c",*it);it++;
            while(it!=wynik.end()){
                printf(", %c",*it);
                it++;
            }
            printf("]\n");
        }
    }
}








