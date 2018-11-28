#include<stdio.h>
#include<string.h>
#include<queue>

using namespace std;

int main() {
    freopen("D://test.txt","r",stdin);
    freopen("D://testout.txt","w",stdout);
    queue<char> eq;
    char oppose[40][4];
    char combine[40][5];
    char elements[102];
    int t,c,d,n,j,k;
    int tempA,tempB,curPos;
    bool tempC;
    scanf("%d",&t);
    for(int i=0;i<t;i++) {
        curPos=0;
        scanf("%d",&c);
        //printf("combine = ");//
        for(j=0;j<c;j++) {
            scanf("%s",combine[j]);
            //printf("%s ",combine[j]);//
        }
        //printf("\n");//
        scanf("%d",&d);
        //printf("oppose = ");//
        for(j=0;j<d;j++) {
            scanf("%s",oppose[j]);
            //printf("%s ",oppose[j]);//
        }
        //printf("\n");//

        scanf("%d",&n);
        scanf("%s",elements);
        //printf("%s\n",elements);//
        tempA=strlen(elements);
        for(j=0;j<tempA;j++) {
            eq.push(elements[j]);
        }
        strcpy(elements,"");
        if(!eq.empty()) {
            elements[curPos]=eq.front();
            ++curPos;
            eq.pop();
        }
        while(!eq.empty()) {
            tempC=false;
            for(j=0;j<c;j++) {
                    if((elements[curPos-1]==combine[j][0] &&
                    eq.front()==combine[j][1]) ||
                    (elements[curPos-1]==combine[j][1] &&
                    eq.front()==combine[j][0])) {
                        eq.pop();
                        elements[curPos-1]=combine[j][2];
                        tempC=true;
                        break;
                    }
            }

            if(!tempC) {
                for(j=0;j<d;j++) {
                    if(eq.front()==oppose[j][0]) {
                        for(k=0;k<curPos;k++) {
                            if(elements[k]==oppose[j][1]) {
                                curPos=0;
                                eq.pop();
                                tempC=true;
                                break;
                            }
                        }
                    }
                    else if(eq.front()==oppose[j][1]) {
                        for(k=0;k<curPos;k++) {
                            if(elements[k]==oppose[j][0]) {
                                curPos=0;
                                eq.pop();
                                tempC=true;
                                break;
                            }
                        }
                    }
                }
            }


            if(!tempC) {
                elements[curPos]=eq.front();
                ++curPos;
                eq.pop();
            }
        }
        elements[curPos]='\0';
        printf("Case #%d: [",i+1);
        tempA=strlen(elements);
        for(j=0;j<tempA;j++) {
            printf("%c",elements[j]);
            if(j<tempA-1)
                printf(", ");
        }
        printf("]\n");
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
