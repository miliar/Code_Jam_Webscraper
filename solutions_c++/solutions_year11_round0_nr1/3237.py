#include<stdio.h>
#include<stdlib.h>
#include<queue>

using namespace std;

#define ORANGE 0
#define BLUE 1

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    queue<int> q[2];
    queue<char> tq;
    int t;
    int n;
    int p,pos[2];
    int curQ,opQ,des;
    int time;
    int tempA,sign;
    char temp[2];
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        scanf("%d",&n);
        pos[ORANGE]=1; pos[BLUE]=1;
        time=0;
        for(int j=0;j<n;j++) {
            scanf("%s",temp);
            scanf("%d",&p);
            //printf("%s %d ",temp,p);
            tq.push(temp[0]);
            if(temp[0]=='O')
                q[ORANGE].push(p);
            else if(temp[0]=='B')
                q[BLUE].push(p);
        }
        //printf("\n");
        while(!tq.empty()) {
            curQ=tq.front()=='O'? ORANGE:BLUE;
            opQ=curQ==ORANGE? BLUE:ORANGE;
            tq.pop();
            des=q[curQ].front();
            q[curQ].pop();
            tempA=abs(des-pos[curQ])+1; //steps
            time+=abs(tempA);
            pos[curQ]=des;
            if(!q[opQ].empty()) {
                sign=pos[opQ]>q[opQ].front()? -1:1;
                if(pos[opQ]==q[opQ].front())
                    sign=0;
                tempA*=sign;
                pos[opQ]+=tempA;
                if((sign==-1 && pos[opQ]<q[opQ].front()) ||
                   (sign==1 && pos[opQ]>q[opQ].front()))
                   pos[opQ]=q[opQ].front();
            }
            //printf("%d %d\n",pos[0],pos[1]);
        }
        printf("Case #%d: %d\n",i+1,time);
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
