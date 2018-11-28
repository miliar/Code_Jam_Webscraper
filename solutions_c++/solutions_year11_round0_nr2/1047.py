#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

map<pair<char,char> , char> C;
map<pair<char,char>, int> D;

void print_vector(vector<char> v)
{
    if(v.size()==0)
        printf("[]");
    else if(v.size()==1)
        printf("[%c]",v[0]);
    else
    {
        printf("[");
        for(int i=0;i<v.size()-1;i++)
            printf("%c, ",v[i]);
        printf("%c]",v[v.size()-1]);
    }
}
int main()
{
    int t,T,n,c,d,i,j;
    char s[111];
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        C.clear();
        D.clear();
        vector<char> out; 
        scanf("%d",&c);
        for(i=0;i<c;i++)
        {
            scanf("%s",s);
            C[make_pair(s[0],s[1])]=s[2];
            C[make_pair(s[1],s[0])]=s[2];
        }
        scanf("%d",&d);
        for(i=0;i<d;i++)
        {
            scanf("%s",s);
            D[make_pair(s[0],s[1])]=1;
            D[make_pair(s[1],s[0])]=1;
        }
        scanf("%d%s",&n,s);
        int m=0;
        for(i=0;i<n;i++)
        {
            m=out.size();
            if(!m)
            {
                out.push_back(s[i]);
                continue;
            }
            if(C[make_pair(s[i],out[m-1])])
            {
                out[m-1]=C[make_pair(s[i],out[m-1])];
                continue;
            }
            for(j=0;j<m;j++)
                if(D[make_pair(s[i],out[j])])
                {
                    out.clear();
                    break;
                }
            if(j==m)
                out.push_back(s[i]);
        }
        printf("Case #%d: ",t);
        print_vector(out);
        printf("\n");
    }
//system("pause");

    return 0;
}
