#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>

using namespace std;

int n;
int p[2000];
int l[2000];
int L[2000];

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("a.out","w",stdout);
    int NCase,CCase=0;
    cin >> NCase;
    while (NCase)
    {
        NCase--;
        
        cin >> n;
        for (int i=0;i<n;i++) cin >> L[i];
        for (int i=0;i<n;i++) l[i]=i;
        for (int i=0;i<n;i++) cin >> p[i];
        
        for (int ii=0;ii<n;ii++) for (int jj=0;jj<n-1;jj++) if (p[jj]<p[jj+1])
        {
            int i=jj,j=jj+1;
            int tmp=p[i];p[i]=p[j];p[j]=tmp;
            tmp=l[i];l[i]=l[j];l[j]=tmp;
        }
            CCase++;
    printf("Case #%d:",CCase);
    for (int i=0;i<n;i++) printf(" %d",l[i]);
    printf("\n");
    }
    

}
    
    
