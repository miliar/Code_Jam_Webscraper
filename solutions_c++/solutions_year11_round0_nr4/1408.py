#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t,g,i,j;
    vector<int> v1,v2;
    float count=0;
    freopen("D-large.in","r",stdin);
    freopen("D_Soluton","w",stdout);
    scanf("%d",&g);
    for(i=0;i<g;i++)
    {
                    scanf("%d",&t);
                    v1.resize(t);
                    for(j=0;j<t;j++)
                    scanf("%d",&v1[j]);
                    v2=v1;
                    sort(v1.begin(),v1.end());
                    count=0;
                    for(j=0;j<t;j++)
                    if(v1[j]!=v2[j])
                    count++;
                    printf("Case #%d: %f\n",(i+1),count);
                    }
                    }
    
