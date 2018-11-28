#include <iostream>
#include <vector>
using namespace std;

int n,m,k,ans,point;
char word[5001][15],dict[15];

int main(){
    freopen("hasil.txt","w",stdout);
    scanf("%d %d %d",&n,&m,&k);
    for (int i=0;i<m;i++){
        scanf("%s",&word[i]);
    }
    for (int i=0;i<k;i++){
        scanf("%s",&dict);
        bool can[n][26];
        memset(can,0,sizeof(can));
        point=0;ans=0;
        bool open=0;
        for (int j=0;j<n;j++){
            bool start=1;
            while (1){
                if (dict[point]=='(' && start){
                    open=1;
                    point++;
                }
                if (dict[point]==')'){
                    open=0;
                    point++;break;
                }
                can[j][dict[point++]-'a']=1;
                //cout<<j<<' '<<dict[point++]<<endl;
                start=0;
                if (point==strlen(dict)) break;
                if (!open && !start) break;
            }
        }
        for (int j=0;j<m;j++){
            bool found=1;
            for (int k=0;k<n;k++){
                if (!can[k][word[j][k]-'a']){
                    found=0;
                    break;
                }
            }
            if (found) ans++;
        }
        printf("Case #%d: %d\n",i+1,ans);
    }
    //system("pause");
    return 0;
}
