#include<iostream>

using namespace std;

struct node0{
    char w[20];
    int len;
    int k;
    int lev;
    int p;
}dict[12000];

char let[30];
int n,m;

void deal(void)
{
    scanf("%d%d",&n,&m);
    for(int i=0;i<n;i++){
        scanf("%s",dict[i].w);
        dict[i].len=strlen(dict[i].w);
    }
    for(int i=0;i<m;i++){
        scanf("%s",let);
        for(int j=0;j<n;j++){
            int cc[300];
            for(int z=0;z<300;z++) cc[z]=0;
            dict[j].p=0;
            for(int ii=0;ii<n;ii++){
                dict[ii].k=0;
                if(dict[ii].len==dict[j].len){
                    dict[ii].lev=1;
                    for(int z=0;z<dict[ii].len;z++)
                        cc[dict[ii].w[z]]++;
                }
                else{
                    dict[ii].lev=0;
                }
            }
            //for(int z='a';z<='z';z++) cerr<<cc[z]<<" ";
            //cerr<<endl;
            for(int jj=0;jj<26;jj++){
                //cerr<<"let jj = "<<let[jj]<<" "<<cc[let[jj]]<<endl;
                if(cc[(int)let[jj]]<=0){
                    //cerr<<"continue "<<jj<<endl;
                    continue;
                }
                for(int ii=0;ii<n;ii++){
                    if(dict[ii].lev==0){
                        continue;
                    }
                    int kkk=0;
                    for(int kk=0;kk<dict[ii].len;kk++,kkk<<=1){
                        if(dict[ii].w[kk]==let[jj]){
                            kkk++;
                        }
                    }
                    dict[ii].k|=kkk;
                    //cerr<<j<<" "<<jj<<" "<<ii<<" "<<dict[ii].k<<endl;
                    if(ii==j && kkk==0){
                        dict[j].p++;
                        //cerr<<j<<" "<<jj<<" "<<let[jj]<<endl;
                    }
                }
                int z=0;
                for(int ii=0;ii<n;ii++){
                    if(dict[ii].lev==0){
                        continue;
                    }
                    if(dict[ii].k!=dict[j].k){
                        dict[ii].lev=0;
                        for(int kk=0;kk<dict[ii].len;kk++)
                            cc[dict[ii].w[kk]]--;
                    }
                    else{
                        z++;
                    }
                }
                if(z==1){
                    break;
                }
            }
        }
        int ma=-1;
        int ans=0;
        for(int j=0;j<n;j++){
            if(dict[j].p>ma){
                ans=j;
                ma=dict[j].p;
            }
            //cerr<<dict[j].p<<endl;
        }
        printf(" %s",dict[ans].w);
    }
    printf("\n");
}

int main(void)
{
    int num=0;
    scanf("%d",&num);
    for(int i=1;i<=num;i++){
        printf("Case #%d:",i);
        deal();
    }
    return 0;
}
/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
