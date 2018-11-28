//---------------------------------------------------------------------------
//-- Problem C. Candy Splitting
//-- @Carlos Mendoza
//--
//--
//---------------------------------------------------------------------------
#include<stdio.h>
#include<vector>
#include<algorithm>
#define MAX 1005

using namespace std;

int Vec[MAX],N,a,b,sa,sb;
vector<int> s;

void Calcula()
{
        a = -10;
        b = -10;

        for(int i=0;i<N;i++)
        {
                if(s[i] == 0)
                {
                        if(a==-10)
                        {
                                a = Vec[i];
                                sa = Vec[i];
                        }
                        else
                        {
                                a = a ^ Vec[i];
                                sa += Vec[i];
                        }
                }
                else if(s[i] == 1)
                {
                        if(b==-10)
                        {
                                b = Vec[i];
                                sb = Vec[i];
                        }
                        else
                        {
                                b = b ^ Vec[i];
                                sb += Vec[i];
                        }
                }
        }
}

int main()
{
        freopen("input.in","rt",stdin);
        freopen("output.out","wt",stdout);

        int T,ntest=1,max;
        scanf("%d\n",&T);
        while(T--)
        {
                scanf("%d\n",&N);
                for(int i=0;i<N;i++)
                        scanf("%d\n",&Vec[i]);

                max = -1;
                for(int i=1;i<N;i++)
                {
                        s.clear();
                        s.resize(N);
                        fill(s.begin(),s.begin()+i,1);
                        fill(s.begin()+i,s.end(),0);
                        sort(s.begin(),s.end());
                        do
                        {
                                Calcula();
                                if(a==b)
                                {
                                        if(sa > max)
                                                max = sa;
                                        if(sb > max)
                                                max = sb;
                                }
                        }while(next_permutation(s.begin(),s.end()));
                }
                if(max == -1)
                        printf("Case #%d: NO\n",ntest++);
                else
                        printf("Case #%d: %d\n",ntest++,max);
        }
        return 0;
}




 