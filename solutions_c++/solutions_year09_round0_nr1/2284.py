#include<iostream>
#define L_MAX 100
#define N_MAX 5000
#define D_MAX 5000
using namespace std;

char words[N_MAX + 3][L_MAX + 3];
bool dict[L_MAX + 3][30];
char buffor[5000];
int L, N, D;

int main() 
{
    scanf("%d %d %d", &L, &N, &D);
    for(int i = 1; i <= N; i++) {
        scanf("\n");
        for(int j = 1; j <= L; j++)
            scanf("%c", &words[i][j]);        
    }
    
    for(int i = 1; i <= D; i++) {
        scanf("\n");
        scanf("%s", &buffor);    
        
        int k = 1;
        bool add = true;
        for(int j = 0; buffor[j] != '\0'; j++) {
            if(buffor[j] == '(')
                add = false;
            else if(buffor[j] == ')')
                add = true;
            else if(buffor[j] >= 'a' && buffor[j] <= 'z')
                dict[k][buffor[j] - 'a'] = true;
                
            if(add) k++;
        }
        
        --k;
        int total = 0;
        
        for(int j = 1; j <= N; j++) {
            bool ok = true;
            for(int l = 1; l <= L; l++) {
                //cout<<words[j][l]<<" ("<<dict[l][words[j][l] - 'a']<<")     ";
                if(!dict[l][words[j][l] - 'a']) {
                    ok = false;
                    break;
                }
            }
            //cout<<endl;   
            if(ok) total++;
        }
        
        printf("Case #%d: %d\n", i, total);
            
        /*
        for(int j = 1; j <= k; j++) {
            cout<<j<<" : ";
            for(int l = 0; l < 30; l++)
                if(dict[j][l]) cout<<(char)(l+'a')<<" ";
            cout<<endl;
        }
        */
        
        for(int j = 0; j <= k+1; j++)
            for(int l = 0; l <= 30; l++)
                dict[j][l] = false;
    }
    
    int i;
    cin>>i;
    return 0;
}
