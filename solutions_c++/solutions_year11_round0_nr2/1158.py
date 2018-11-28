#include<cstdio>
#include<vector>

using namespace std;

int t,c,d,n;
char seq[105],cb[26][26],count[26];
vector<int> op[26];

int main(){
    char str[105];

    scanf("%d",&t);
    for(int i=0;i<t;i++)
    {

        for(int j=0;j<26;j++)
        {
            for(int k=0;k<26;k++)
                cb[j][k]=0;
            op[j].clear();
            count[j]=0;
        }

        scanf("%d",&c);
        for(int j=0;j<c;j++)
        {
            scanf("%s",str);
            cb[str[0]-'A'][str[1]-'A']=(str[2]-'A');
            cb[str[1]-'A'][str[0]-'A']=(str[2]-'A');
        }

        scanf("%d",&d);
        for(int j=0;j<d;j++)
        {
            scanf("%s",str);
            op[str[0]-'A'].push_back(str[1]-'A');
            op[str[1]-'A'].push_back(str[0]-'A');
        }

        scanf("%d",&n);
        scanf("%s",str);

        int sol[105];
        int p=0;

        for(int j=0;j<n;j++)
        {
            sol[p++]=str[j]-'A';
            count[sol[p-1]]++;
            if(p>1&&cb[sol[p-2]][sol[p-1]])
            {
                count[sol[p-2]]--;
                count[sol[p-1]]--;
                sol[p-2]=cb[sol[p-2]][sol[p-1]];
                p--;
                count[sol[p-1]]++;
            }
            else
            {
                int si=op[sol[p-1]].size();
                for(int k=0;k<si;k++)
                {
                    if(count[op[sol[p-1]][k]]>0)
                    {
                        for(int l=0;l<26;l++)
                            count[l]=0;
                        p=0;
                    }
                }
            }

        }

        printf("Case #%d: [",i+1);
        for(int j=0;j<p;j++)
        {
            printf("%c",sol[j]+'A');
            if(j!=p-1)
                printf(", ");
        }
        printf("]\n");

    }
    return 0;
}
