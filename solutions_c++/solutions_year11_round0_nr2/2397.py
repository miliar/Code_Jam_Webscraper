#include <stdio.h>
#include <stack>

using namespace std;

int c,d;
int oppose[27][27];
int convert[27][27];
int n;
char word[105];
stack<int> stk;
int isGet[27];
int ans[105];

void clear(){
    int i,j;
    for(i=0;i<27;i++){
    	for(j=0;j<27;j++){
    		oppose[i][j]=0;
    		convert[i][j]=-1;
    	}
    	isGet[i]=0;
    }
}

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
        clear();
        scanf("%d",&c);
        char str[105];
        for(i=1;i<=c;i++){
            scanf("%s",&str[1]);
            for(j=1;j<=3;j++){
            	str[j]-='A';
            }
            convert[str[1]][str[2]]=str[3];
            convert[str[2]][str[1]]=str[3];
        }
        scanf("%d",&d);
        for(i=1;i<=d;i++){
            scanf("%s",&str[1]);
            for(j=1;j<=2;j++){
            	str[j]-='A';
            }
            oppose[str[1]][str[2]]=1;
            oppose[str[2]][str[1]]=1;
        }
        scanf("%d",&n);
        scanf("%s",&str[1]);
        int temp;
        for(i=1;i<=n;i++){
            str[i]-='A';
            if(stk.empty()){
            	stk.push(str[i]);
                isGet[str[i]]++;
            }else{
                temp=stk.top();
                if(convert[temp][str[i]]!=-1){
                    isGet[temp]--;
                    stk.pop();
                    stk.push(convert[temp][str[i]]);
                    isGet[convert[temp][str[i]]]=1;
                }else{
                    stk.push(str[i]);
                    isGet[str[i]]++;
                }
                temp=stk.top();
                int k;
                for(k=0;k<27;k++){
                    if(isGet[k]>0){
                    	if(oppose[k][temp]==1){
                    	    while(!stk.empty()){
                    	    	stk.pop();
                    	    }
                    	    for(j=0;j<27;j++){
                    	    	isGet[j]=0;
                    	    }
                            break;
                    	}
                    }
                }
            }
        }
        i=stk.size();
        int size=i;
        while(!stk.empty()){
            ans[i--]=stk.top();
            stk.pop();
        }
        printf("Case #%d: [",xx);
        for(i=1;i<size;i++){
            printf("%c, ",ans[i]+'A');
        }
        if(size!=0){
        	printf("%c",ans[size]+'A');
        }
        printf("]\n",ans[size]+'A');
    }
	return 0;
}
/*
1
1 QFT 1 QF 7 FAQFDFQ

5
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 0 2 EA
1 QRI 0 4 RRQR
0 1 QW 2 QW

5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
*/
