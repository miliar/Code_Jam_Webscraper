#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<string>
#include<sstream>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int ans[t];
    for(int x=0;x<t;x++){
        ans[x]=0;
        int n=0;
        scanf("%d",&n);
        int posO=1,posB=1;
        char a[n];
        int b[n],size1=0,size2=0;
        for(int i=0;i<n;i++){
            a[i]=' ';
            b[i]=0;
            int temp;
            char tempo;
            scanf("%c",&tempo);
            scanf("%d",&temp);
            scanf("%c",&a[i]);
            scanf("%d",&b[i]);
            if(a[i]=='O')size1++;
            else size2++;
            //printf("a[%d]:%c , b[%d] %d , %d %d\n",i,a[i],i,b[i],size1,size2);
        }
        int orange[size1],blue[size2];
        orange[0]=1;
        blue[0]=1;
        for(int i=0,j=0,k=0;i<n;i++){
            if(a[i]=='O')orange[j++]=b[i];
            else if(a[i]=='B')blue[k++]=b[i];
        }
        for(int i=0,j=0,k=0;i<n;i++){
            if(j<size1)
            //printf("orange[%d]:%d\n",j,orange[j]);
            j++;
            if(k<size2)
            //printf("blue[%d]:%d\n",k,blue[k]);
            k++;

        }

        bool blueturn=a[0]=='B';
        //j=blue , k=orange
        for(int i=0,j=0,k=0;i<n;){
            while(blueturn&&i<n){
                //printf("-blue turn- i:%d,blue[%d]:%d,orange[%d]:%d,posB:%d,posO:%d,ans:%d\n",i,j,blue[j],k,orange[k],posB,posO,ans[x]);
                if(posB==blue[j]&&posO<orange[k]){
                    posO++;ans[x]++;j++;blueturn=(a[++i]=='B');
                }else if(posB==blue[j]&&posO>orange[k]){
                    posO--;ans[x]++;j++;blueturn=(a[++i]=='B');
                }else if(posB==blue[j]&&posO==orange[k]){
                    ans[x]++;j++;blueturn=(a[++i]=='B');
                }   //only walk
                else if(posB<blue[j]&&posO==orange[k]){
                    posB++;ans[x]++;
                }else if(posB>blue[j]&&posO==orange[k]){
                    posB--;ans[x]++;
                }else if(posB<blue[j]&&posO<orange[k]){
                    posB++;posO++;ans[x]++;
                }else if(posB<blue[j]&&posO>orange[k]){
                    posB++;posO--;ans[x]++;
                }else if(posB>blue[j]&&posO<orange[k]){
                    posB--;posO++;ans[x]++;
                }else if(posB>blue[j]&&posO>orange[k]){
                    posB--;posO--;ans[x]++;
                }
            }
            while(!blueturn&&i<n){
                //printf("orange turn i:%d,blue[%d]:%d,orange[%d]:%d,posB:%d,posO:%d,ans:%d\n",i,j,blue[j],k,orange[k],posB,posO,ans[x]);
                if(posB<blue[j]&&posO==orange[k]){
                    posB++;ans[x]++;k++;blueturn=(a[++i]=='B');
                }else if(posB>blue[j]&&posO==orange[k]){
                    posB--;ans[x]++;k++;blueturn=(a[++i]=='B');
                }else if(posB==blue[j]&&posO==orange[k]){
                    ans[x]++;k++;blueturn=(a[++i]=='B');
                }   //only walk
                else if(posB==blue[j]&&posO<orange[k]){
                    posO++;ans[x]++;
                }else if(posB==blue[j]&&posO>orange[k]){
                    posO--;ans[x]++;
                }else if(posB<blue[j]&&posO<orange[k]){
                    posB++;posO++;ans[x]++;
                }else if(posB<blue[j]&&posO>orange[k]){
                    posB++;posO--;ans[x]++;
                }else if(posB>blue[j]&&posO<orange[k]){
                    posB--;posO++;ans[x]++;
                }else if(posB>blue[j]&&posO>orange[k]){
                    posB--;posO--;ans[x]++;
                }
            }
        }

    }

    for(int i=0;i<t;i++){
        printf("Case #%d: %d\n",i+1,ans[i]);
    }
    return 0;
}
