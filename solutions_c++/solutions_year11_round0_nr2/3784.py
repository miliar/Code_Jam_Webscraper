#include <cstdio>
#include <stack>
#include <cstring>

using namespace std;

char com[50][4], opp[50][4];

int main(){
    int t;
    scanf("%d",&t);
    for(int test = 0; test < t; ++test){
        int c,d;
        scanf("%d",&c);
        stack< char > elements;
        for(int i = 0; i < c; ++i){
            scanf("%s",com[i]);
           // printf("%s\n", com[i]);
        }
        scanf("%d",&d);
        for(int i = 0; i < d; ++i){
            scanf("%s",opp[i]);
        }

        int n;
        scanf("%d",&n);
        char in[110];
        scanf("%s",in);

        int postoji[300] = {0};

        for(int i = 0;i < n; ++i){
            char a,b;
            elements.push( in[i] );
            postoji[in[i]]++;
            while(elements.size() > 1){
                a = elements.top();
                elements.pop();
                postoji[a]--;
                b = elements.top();
                elements.pop();
                postoji[b]--;
                bool cnt = false;
                for(int j = 0; j < c; ++j){
                    if( (com[j][0] == a && com[j][1] == b) || (com[j][0] == b && com[j][1] == a )){
                        elements.push(com[j][2]);
                        postoji[com[j][2]]++;
                        cnt = true;
                        break;
                    }
                }

                if(cnt) continue;
                postoji[b]++;
                for(int j = 0; j < d; ++j){
                    if( (opp[j][0] == a && postoji[opp[j][1]] > 0) || (opp[j][1] == a && postoji[opp[j][0]] > 0)){
                        while(!elements.empty()) elements.pop();
                        cnt = true;
                        memset(postoji, 0, sizeof(postoji));
                        break;
                    }
                }
                if(cnt){
                 break;
                }else{
                    elements.push(b);
                    elements.push(a);
                    postoji[a]++;
                     break;
                }
            }
        }

        stack<char> pom;
        while(!elements.empty()){

            pom.push(elements.top());
            elements.pop();
        }
        printf("Case #%d: [", test+1);
        while( !pom.empty() ){
            if( pom.size() > 1)
                printf("%c, ", pom.top());
            else
                printf("%c", pom.top());
            pom.pop();
        }
        printf("]\n");

    }
    return 0;
}
