
#include <stdio.h>
#include <stdlib.h>
#include <memory.h>

#define N 300

//using namespace std;
int mat[N][N],match1[N],match2[N];
int n;
int left,right;
int dep[N],arr[N];

int hungary(){
    
	int s[N],t[N],p,q,ret=0,i,j,k;
    memset(match1,-1,sizeof(match1));
	memset(match2,-1,sizeof(match2));
	
    for (i=0;i<n;ret+=(match1[i++]>=0)){
	   memset(t,-1,sizeof(t));	
       for (s[p=q=0]=i;p<=q&&match1[i]<0;p++)
			for (k=s[p],j=0;j<n&&match1[i]<0;j++)
				if (mat[k][j]&&t[j]<0){
					s[++q]=match2[j];t[j]=k;
					if (s[q]<0)
						for (p=j;p>=0;j=p){
							match2[j]=k=t[j];p=match1[k];match1[k]=j;
                        }    
                }
    }        
    return ret;
}


int main(){
    int z,kase;
    //int departure,arrival;
    int turntime;
    char buf0[20],buf1[20];
    int i,j;
    for(scanf("%d",&z),kase=1;kase<=z;kase++){
        scanf("%d",&turntime);
        int x,y;
        for(scanf("%d %d",&left,&right),i=0;i<left+right;i++){
            scanf("%s %s",buf0,buf1);
            sscanf(buf0,"%d:%d",&x,&y);
            dep[i]=x*60+y;
            sscanf(buf1,"%d:%d",&x,&y);
            arr[i]=x*60+y;
            //printf("%d %d\n",dep[i],arr[i]);
        }    
        memset(mat,0,sizeof(mat));
        for(i=0;i<left+right;i++){
            if(i<left){
                for(j=left;j<left+right;j++){
                    if(arr[i]+turntime <= dep[j]){
                        mat[i][j]=1;    
                    }    
                }    
            }else{
                for(j=0;j<left;j++){
                    if(arr[i]+turntime <= dep[j]){
                        mat[i][j]=1;
                    }    
                }    
            }        
        }    
        n=left+right;
        hungary();
        int ans0=left,ans1=right;
        for(i=0;i<left;i++){
            if(match2[i]>-1){
                ans0--;
            }    
        }    
        for(i=left;i<left+right;i++){
            if(match2[i]>-1){
                ans1--;
            }    
        }    
        printf("Case #%d: %d %d\n",kase,ans0,ans1);
    }    
    return 0;
}    
