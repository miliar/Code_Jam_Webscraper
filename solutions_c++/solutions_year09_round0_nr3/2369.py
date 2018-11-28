#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <math.h>
#include <bitset>
#include <string.h>
#include <stack>
#include <queue>
#include <memory.h>

#define MAXH 102
#define MAXW 102
#define SET(a,b) memset(a,b,sizeof(a));
#define input(a) scanf("%d",&a);
#define FOR(b,a,w,e) for(int b=gp(pos[w][a],e);b<possize[e];++b)
using namespace std;

int pos[123][502],possize[123];
string str;

//============gp()=======================
int gp(int position,char e)
{
position++;
for(int g=0;g<possize[e];++g)
{if(pos[e][g]>=position){return g;}
}
return pos[e][possize[e]-1]+1;
}

//========== main =======================
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small.out","w",stdout);

    int t,z=1;
    input(t);
    getchar();

    while (t--)
    {
        SET(pos,0);
        SET(possize,0);
        getline(cin,str);
        int size=str.length(),count=0;
        for (int a=0;a<size;++a)
        {
            pos[str[a]][possize[str[a]]++]=a;
        }

for(int a=0;a<possize['w'];++a)
{//for(int b=gp(pos['w'][a]);b<possize['e'];++b)
FOR(b,a,'w','e')
FOR(c,b,'e','l')
FOR(d,c,'l','c')
FOR(e,d,'c','o')
FOR(f,e,'o','m')
FOR(g,f,'m','e')
FOR(h,g,'e',' ')
FOR(i,h,' ','t')
FOR(j,i,'t','o')
FOR(k,j,'o',' ')
FOR(l,k,' ','c')
FOR(m,l,'c','o')
FOR(n,m,'o','d')
FOR(o,n,'d','e')
{if(count>=10000){count=count%10000;}
FOR(p,o,'e',' ')
FOR(q,p,' ','j')
FOR(r,q,'j','a')
{count+=possize['m']-gp(pos['a'][r],'m');}
}
}
if(count>=10000){count=count%10000;}

printf("Case #%d: %04d\n",z,count);
z++;

}
return 0;
}



