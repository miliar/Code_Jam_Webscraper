
#include<iostream>
#include<fstream>
#include<algorithm>
#include<iterator>
#include<vector>
#include<string>
#include<sstream>
#include<set>
#include<deque>
#include<cstring>
#include<cstdlib>


#define FOR(i,v,n) for(int i=v;i<n;++i)
#define PVector(arr,type) copy(arr.begin(),arr.end(),ostream_iterator<type>(cout," "));
#define swap(a,b) { a=a^b; b=a^b; a=a^b; }

using namespace std;
typedef long long ll;

vector<string> str(4);
bool xwin,owin,empty;
void who(char a)
{
    if(a=='X') xwin=true;
    else if(a=='O') owin=true;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;cin>>t;

    for(int i=1;i<=t;++i)
    {
        FOR(ii,0,4) cin>>str[ii];
        xwin=owin=empty=false;
        bool flag;

        for(int p=0;p<4;++p)
        {
            for(int q=0;q<4;++q)
            {
                if(str[p][q]=='.')
                {
                    empty=true;
                    continue;
                }

                char ch=str[p][q];
                if(ch=='T') flag=true;

                //right
                if(q+1<4 && flag) ch=str[p][q+1];
                if(q+3<4 && ( str[p][q+1]==ch || str[p][q+1]=='T') && ( str[p][q+2]==ch || str[p][q+2]=='T') && ( str[p][q+3]==ch || str[p][q+3]=='T')) who(ch);

                //down
                if(p+1<4 && flag) ch=str[p+1][q];
                if(p+3<4 && ( str[p+1][q]==ch || str[p+1][q]=='T') && ( str[p+2][q]==ch || str[p+2][q]=='T') && ( str[p+3][q]==ch || str[p+3][q]=='T') ) who(ch);

                // diag 1
                if(p+1<4 && q+1<4 && flag) ch=str[p+1][q+1];
                if(p+3<4 && q+3<4 && (str[p+1][q+1]==ch || str[p+1][q+1]=='T') && (str[p+2][q+2]==ch || str[p+2][q+2]=='T') && (str[p+3][q+3]==ch || str[p+3][q+3]=='T')) who(ch);

                // diag 2
                if(p+1<4 && q-1>=0 && flag) ch=str[p+1][q-1];
                if(p+3<4 && q-3>=0 && (str[p+1][q-1]==ch || str[p+1][q-1]=='T') && (str[p+2][q-2]==ch || str[p+2][q-2]=='T') && (str[p+3][q-3]==ch || str[p+3][q-3]=='T')) who(ch);

                flag=false;
                if(xwin || owin) goto my;
            }
        }

        my:
        cout<<"Case #"<<i<<": ";
        if(xwin)  cout<<"X won\n";
        else if(owin) cout<<"O won\n";
        else if(empty) cout<<"Game has not completed\n";
        else cout<<"Draw\n";
    }


    return 0;
}
