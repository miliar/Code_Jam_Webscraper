#include<stdio.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;
vector<string> my;
map<string,bool> our;
double tt(int p,int q)
{
    p++;
    q--;
    double now;
    sscanf(my[p].c_str(),"%lf",&now);
    if(p==q)
        return now;
    int g=0,i;
    for(i=p+2;;i++)
    {
        if(my[i]=="(")
            g++;
        else if(my[i]==")")
            g--;
        if(!g)
            break;
    }
    if(our[my[p+1]])
        return now*tt(p+2,i);
    else
        return now*tt(i+1,q);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,o,g,t,len,i;
    string now;
    char str[1024];
    scanf("%d",&c);
    for(o=1;o<=c;o++)
    {
        printf("Case #%d:\n",o);
        my.clear();
        g=0;
        scanf("%d",&t);
        gets(str);
        while(t--)
        {
            gets(str);
            len=strlen(str);
            str[len]=' ';
            str[len+1]='\0';
            len++;
            now="";
            for(i=0;i<len;i++)
                if(str[i]=='('||str[i]==')')
                {   
                    if(now.size())
                    {
                        my.push_back(now);
                        now="";
                    }
                    now+=str[i];
                    my.push_back(now);
                    now="";
                }
                else if(str[i]>='a'&&str[i]<='z'||str[i]>='0'&&str[i]<='9'||str[i]=='.')
                    now+=str[i];
                else if(now.size())
                {
                    my.push_back(now);
                    now="";
                }
        }
        scanf("%d",&t);
        while(t--)
        {
            scanf("%s",str);
            our.clear();
            scanf("%d",&g);
            while(g--)
            {
                scanf("%s",str);
                our[str]=true;
            }
            printf("%.12lf\n",tt(0,my.size()-1));
        }
    }
    return 0;
}
