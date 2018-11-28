
#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<math.h>
#include<string.h>
#include<iostream>

using namespace std;

inline int max(int a,int b){
   return(a>b)?a:b;
}

inline int min(int a,int b){
   return(a<b)?a:b;
}

inline int abs(int a){
    return(a<0)?-a:a;
}
//qsort(array,arraysize,sizeof(int),compare);
int compare(const void*a,const void*b){
    return (*(int*)a-*(int*)b);
}
int comp(const void* p1, const void* p2) {
  int* arr1 = (int*)p1;
  int* arr2 = (int*)p2;
  int diff1 = arr1[0] - arr2[0];
  if (diff1) return diff1;
  return arr1[1] - arr2[1];
}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);

	int t;
	scanf("%d",&t);
    int R,C;
    char table[51][51];
    for(int z=1;z<=t;z++){
        scanf("%d%d",&R,&C);
        for(int i=0;i<R;i++){
            scanf("%s",&table[i]);
        }
        bool isOk=true;
        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(table[i][j]=='#'){
                    if(j==C-1||i==R-1){
                        isOk=false;
                        break;
                    }
                    if(table[i][j+1]=='#'&&table[i+1][j]=='#'&&table[i+1][j+1]=='#'){
                        table[i][j]='/';
                        table[i][j+1]='\\';
                        table[i+1][j]='\\';
                        table[i+1][j+1]='/';
                    }else{
                        isOk=false;
                        break;
                    }
                }
            }
        }


        printf("Case #%d:\n",z);
        if(isOk){
            for(int i=0;i<R;i++){
                printf("%s\n",table[i]);
            }
        }else printf("Impossible\n");
    }
	return 0;
}
