#include <iostream>
using namespace std;

void opens(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
}

void openb(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
}

int tes,cnt,mp[255],maxi;
char word[101];
string t;

void print(string a,int base){
    long long res=0LL;
    for (int i=0;i<a.length();i++){
        res*=(long long)base;
        res+=(long long)a[i];
    }
    cout<<res<<endl;
}

int main(){
    //opens();
    openb();
    scanf("%d",&tes);
    for (int i=1;i<=tes;i++){
        scanf("%s",word);
        memset(mp,-1,sizeof(mp));
        mp[word[0]]=1;
        maxi=1;
        t="";
        t+=(char)mp[word[0]];
        bool used=0;
        cnt=1;
        for (int j=1;j<strlen(word);j++){
            if (mp[word[j]]!=-1) t+=(char)mp[word[j]];
            else if (!used){
                mp[word[j]]=0;
                used=1;
                t+=(char)mp[word[j]];
            }
            else {
                mp[word[j]]=++cnt;
                t+=(char)mp[word[j]];
            }
            maxi=max(maxi,mp[word[j]]);
        }
        printf("Case #%d: ",i);
        /*for (int j=0;j<t.length();j++) cout<<(int)t[j];
        cout<<endl;*/
        print(t,++maxi);
    }
    //system("pause");
    return 0;
}
