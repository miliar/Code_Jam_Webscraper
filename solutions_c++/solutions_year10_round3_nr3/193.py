#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d\n",&t);
    for(int tc=1; tc<=t; tc++){
        int ans = 0;
        int n,m;
        scanf("%d %d\n",&n,&m);
        vector<vector<int> > a(n);
        vector<int> answer;
        for(int i=0; i<n; i++){
            char temp[1111];
            scanf("%s\n",temp);
            for(int j=0; j<m/4; j++){
                int num = 0;
                if(temp[j]<='9')
                    num = temp[j]-'0';
                else
                    num = temp[j]-'A'+10;
                for(int k=8; k>=1; k/=2){
                    if(num&k)
                        a[i].push_back(1);
                    else
                        a[i].push_back(0);
                }
            }
        }
        while(true){
            int x,y,l;
            l=0;
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    if(a[i][j]==-1)
                        continue;
                    bool ok = true;
                    int st = a[i][j];
                    for(int k=1;i+k<n && j+k<m && ok; k++){
                        st = a[i][j];
                        if(k%2==1)
                            st = 1-st;
                        for(int l1=0; l1<=k; l1++){
                            if(a[i+k][j+l1]!=st)
                                ok=false;
                            if(a[i+l1][k+j]!=st)
                                ok=false;
                            st=1-st;
                        }
                        if(ok){
                            if(l<k){
                                x=i;
                                y=j;
                                l=k;
                            }
                        }
                    }
                }
            }
            if(l==0)
                break;
            answer.push_back(l);
            for(int l1=0; l1<=l; l1++)
                for(int l2=0; l2<=l; l2++)
                    a[l1+x][l2+y]=-1;
        }

        int rest = n*m;
        for(int i=0; i<(int)answer.size(); i++)
            rest = rest - (answer[i]+1)*(answer[i]+1);
        vector<int> b(answer);
        b.erase(unique(b.begin(),b.end()),b.end());
        ans = b.size();
        if(rest!=0)
            ans++;
        printf("Case #%d: %d\n",tc,ans);
        for(int i=0; i<b.size(); i++)
            printf("%d %d\n",b[i]+1,count(answer.begin(),answer.end(),b[i]));
        if(rest!=0)
            printf("1 %d\n",rest);
    }
    return 0;
}

