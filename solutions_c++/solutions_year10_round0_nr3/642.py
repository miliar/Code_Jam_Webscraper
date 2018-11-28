#include <iostream>

using namespace std;
typedef long long LL;

LL R,K,N;
LL g[1100];
LL v[1100];
LL s[1100];
LL next[1100];

LL solve(){
    LL first,i,j,sum,tmp,start,len,ans;

    for( i=0;i<N;++i ){
        sum=0;
        for( j=0;j<N;++j ) {
            tmp=i+j;
            if( tmp>=N ) tmp-=N;
            if( sum+g[tmp] > K ) break;
            else sum+=g[tmp];
        }
        next[i]=tmp;
        s[i]=sum;
    }

    memset( v,0,sizeof(v));

    v[first=0]=1;
    for( i=2;;++i ){
        first=next[first];
        if( v[first] ){
            start=v[first];
            len=i-v[first];
            break;
        }else{
            v[first]=i;
        }
    }

    if( R<start ){
        ans=0;
        first=0;
        for( i=1;i<=R;++i ){
            ans+=s[first];
            first=next[first];
        }
        return ans;
    }else {
        ans=0;
        first=0;
        for( i=1;i<start;++i ){
            ans+=s[first];
            first=next[first];
        }

        sum=0;
        for( i=1;i<=len;++i ){
            sum+=s[first];
            first=next[first];
        }

        R-=start;
        ans+= R/len *sum;

        for( i=0;i<= R%len;++i ){
            ans+=s[first];
            first=next[first];
        }
        return ans;
    }
}



int main()
{
    freopen("c:\\C-small.in","r",stdin);
    freopen("c:\\out.txt","w",stdout);
    LL tn;
    cin>>tn;
    for(LL ts=1;ts<=tn;++ts ){
        cin>>R>>K>>N;
        for( LL i=0;i<N;++i ){
            cin>>g[i];
        }
        LL ans= solve();
        printf("Case #%I64d: %I64d\n",ts,ans);
    }
    return 0;
}
