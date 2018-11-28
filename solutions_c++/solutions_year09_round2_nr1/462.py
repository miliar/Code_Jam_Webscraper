#include<iostream>
using namespace std;
#define myfor(i,c,d) for(i = (c);i<=(d);++i)
struct treenode
{
    char s[20];
    double weight;
    treenode*ls,*rs;
}*root;
int nf,na;
char fs[120][20];
bool is_digit(char c)
{
    if(c>='0'&&c<='9') return true;
    return false;
}
double read_double(char *st)
{
    char *p = st;
    while(!is_digit(*p))++p;
    double t= 1;
    double sum = 0;
    while(is_digit(*p))
    {
        if(*p =='.'){++p; continue;}
        sum = sum + (*p-'0')*t;
        t = t/10;
        ++p;
        if(*p =='.')++p;
    }
    return sum;
}
bool isletter(char c)
{
    if(c>='a'&&c<='z'||c>='A'&&c<='Z') return true;
    return false;
}
void read_feature(char *s,char *&st)
{
while(!isletter(*st))++st;
while(isletter(*st))
{
    *s = *st;
    ++s;
    ++st;
}
*s = 0;
}

bool first_left(char *s)
{
    while(true)
    {
        if(*s=='(') return true;
        else if(*s==')') return false;
        ++s;
    }
    return false;
}
void build(treenode*&r,char *&s)
{
    double t;
    char ch;
    while(*s!='(')++s;
    ++s;
    if(r == NULL) r= new treenode();
    if(first_left(s))
    {
        t = read_double(s);
        r->weight = t;
        read_feature(r->s,s);
        build(r->ls,s);
        build(r->rs,s);
        while(*s!=')') ++s;
    }
    else 
    {
        r->weight = read_double(s);
        r->ls = r->rs = NULL;
    }
}
bool in_feature(char *s)
{
    int i;
    myfor(i,1,nf)
    {
        if(strcmp(s,fs[i])==0) return true;
    }
    return false;
}
double calc(treenode *r)
{
    if(r->rs == NULL) return r->weight;
    if(in_feature(r->s))
        return r->weight*calc(r->ls);
    else return r->weight*calc(r->rs);
}
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tt,tcase;
    double ans;
    int i,j,L,len;
    char st1[200],*p,st[19000];
    scanf("%d",&tcase);
    for(tt = 1;tt<=tcase;++tt)
    {
        scanf("%d\n",&L);
        len = 0;
        myfor(j,1,L)
        {
            gets(st1);
            p = st1;
            while(*p)
            {
                st[len++] = *p;
                ++p;
            }
        }
        st[len] = 0;
        printf("Case #%d:\n",tt);
        root = new treenode();
        p = st;
        build(root,p);
        scanf("%d",&na);
        myfor(i,1,na)
        {
            scanf("%s",st);
            scanf("%d",&nf);
            myfor(j,1,nf)
                scanf("%s",fs[j]);
            ans = calc(root);
            printf("%.7lf\n",ans);
        }
    }

}