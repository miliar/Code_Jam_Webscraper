#include <iostream>
#include <set>
#include <cstring>
using namespace std;

int cases;
int i,j,k;
int len;
string cur;
string lan[5005];
string str[5005];
int nstr;
int ans;
int L,D,N;

bool in(char a, string b)
{
        int i;
        int len=b.size();
        for(i=0;i<len;i++)
                if(a==b[i])
                        return 1;
        return 0;
}

bool ok(int k)
{
        for(int i=0;i<L;i++)
        {
                if(!in(lan[k][i],str[i]))
                        return 0;
        }
        return 1;
}
int main()
{
//        freopen("A-small-attempt0.in","r",stdin);
//        freopen("A-small-attempt0.out","w",stdout);

        freopen("A-large.in","r",stdin);
        freopen("A-large.out","w",stdout);

        scanf("%d %d %d",&L,&D,&N);

        for(i=0;i<D;i++)
        {
                cin>>lan[i];
        }

        for(cases=1; cases<=N;cases++)
        {
                ans=0;
                cin>>cur;
                len=cur.size();

                for(i=0;i<len;i++)
                        str[i]="";
                nstr=0;

                for(i=0;i<len;)
                {
                        if(cur[i]=='(')
                        {
                                i++;
                                while(cur[i]!=')')
                                        str[nstr]+=cur[i++];
                                i++;
                                nstr++;
                        }
                        else
                        {
                                str[nstr++]=cur[i++];
                        }
                }
//                for(i=0;i<nstr;i++)
//                        cout<<str[i]<<endl;
                if(nstr!=L)
                {
                        ans=0;
                        printf("Case #%d: ",cases);
                        cout<<ans<<endl;
                        continue;
                }
                for(i=0;i<D;i++)
                {
                        if(ok(i))
                                ans++;
                }
                printf("Case #%d: ",cases);
                cout<<ans<<endl;
        }

        return 0;
}
