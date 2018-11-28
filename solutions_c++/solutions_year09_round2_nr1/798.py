#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<string>
#include<set>
#include<stack>
#include<vector>
#include<algorithm>

using namespace std;

#define opn first
#define cls second

struct entry {
    double p;
    string s;     
};

entry T[10000];
double ans;
char Tree[2000000];
int I;

pair<int,int> brpos[500];
set<string> F;

void buildTree(int node)
{
    char *pr = Tree + brpos[I].opn + 1;
    
    double p;
    
    sscanf(pr,"%lf",&p);
    
    T[node].p = p;
    
    int i = 0;
    
    while( (pr[i]=='.') || (pr[i] >= '0' && pr[i] <= '9') )
    ++i;
    
    ++I;
    
    if(pr[i]==')')
    {
        T[node].s = "";
        return;
    }
    else
    {
        char str[100];
        pr += i;
        int j = 0;
        while(isalpha(pr[j])) { str[j] = pr[j]; ++j; }
        str[j] = '\0';
        T[node].s = string(str);   
    }
    
    buildTree(node*2);
    buildTree(node*2+1);
    
}

void dfs(int node)
{
    ans *= T[node].p; 
    if(T[node].s=="")
    return;
    if(F.find(T[node].s)!=F.end())
    {
        dfs(node*2);   
    }
    else
    {
        dfs(node*2+1);   
    }
}

char raw[102][100];

int main()
{
    freopen("A_easy.in","r",stdin);
    freopen("A_easy.out","w",stdout);
    
    int Test;
    
    scanf("%d",&Test);
    
    for(int t = 1; t <= Test; ++t)
    {
        int lines;
        
        scanf("%d",&lines);
        
        getchar();
        
        for(int i = 0; i < lines; ++i)
        {
            gets(raw[i]);   
        }
        
        int indx = 0, brindx = 0;
        
        Tree[0] = '#';

        stack<int> st;
                
        for(int i = 0; i < lines; ++i)
        {
            for(int len = strlen(raw[i]), j = 0; j < len; ++j)
            {
                if(raw[i][j]!=' ')
                {
                    Tree[indx++] = raw[i][j];
                    if(Tree[indx-1]=='(')
                    {
                        brpos[brindx].opn = indx-1;
                        st.push(brindx++);
                    }
                    else if(Tree[indx-1]==')')
                    {
                        int tmp = st.top();
                        st.pop();
                        brpos[tmp].cls = indx-1;
                    }
                }
            }   
        }
            
        Tree[indx] = '\0';
            
        I = 0;
        buildTree(1);
        
        int q;
        
        scanf("%d",&q);
        
        char name[100], feature[100];
        
        printf("Case #%d:\n",t);
        
        while(q--)
        {
            F.clear();
            int tot;
            scanf("%s%d",name,&tot);   
            for(int i = 0; i < tot; ++i)
            {
                scanf("%s",feature);   
                F.insert(string(feature));
            }
            
            ans = 1.0;
            
            dfs(1);
            
            printf("%.7lf\n",ans);
        }
        
    }
    
    //while(1);
    
    return 0;    
}
