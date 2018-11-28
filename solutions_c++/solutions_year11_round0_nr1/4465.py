#include<cstdio>
#include<queue>
#include<cstdlib>

using namespace std;

int T,N;


int main() {
    scanf("%d",&T);
    for(int t=0;t<T;t++) {
        queue<int> O,B,both;
        queue<bool> both2; // orange is true
        /* input */
        scanf("%d",&N);
        for(int i=0;i<N;i++) {
            char c[10];
            int num;
            scanf("%s %d",c,&num);
//            printf("%s : %d\n",c,num);
            both.push(num);
            if(c[0] == 'O') {
                both2.push(true);
                O.push(num);
            } else {
                both2.push(false);
                B.push(num);
            }
        }

        int steps=0;
        int Oloc=1,Bloc=1;
        while(!both.empty()) {
            if(both2.front() && !B.empty())
                if(Bloc != B.front())
                    Bloc += (B.front() > Bloc ? 1 : -1);
            if(!both2.front() && !O.empty())
                if(Oloc != O.front())
                    Oloc += (O.front() > Oloc ? 1 : -1);
            if(both2.front())
                if(Oloc == O.front()) {
                    O.pop();
                    both.pop();
                    both2.pop();
                } else
                    Oloc += (O.front() > Oloc ? 1 : -1);
            else
                if(Bloc == B.front()) {
                    B.pop();
                    both.pop();
                    both2.pop();
                } else
                    Bloc += (B.front() > Bloc ? 1 : -1);
            steps++;
        }
        printf("Case #%d: %d\n",t+1,steps);
    }
    return 0;
}
