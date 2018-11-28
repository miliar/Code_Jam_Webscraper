#include <iostream>


using namespace std;

char lang[5001][16];
bool bad[5001];
char ltrs[1001];

int main()
{
    FILE* in = freopen("A-large.in", "r", stdin);
    FILE* out = freopen("A-large.out", "w+", stdout);

    int l,d,n,nw,lc,cc;
    cin>>l>>d>>n;
    for(int i=0;i<d;++i)
    {
        scanf("%s",lang[i]);
    }
    for(int q=0;q<n;++q)
    {
        nw = d;
        cc = 0;
        memset(bad, 0, sizeof(bad));
        do
        {
            lc = 0;
            do
            {
                scanf("%c", ltrs);
            }while('\n' == ltrs[0]);
            if('(' == ltrs[0])
            {
                do
                {
                    scanf("%c", ltrs+lc);

                }
                while(ltrs[lc++]!= ')');
                --lc;
                ltrs[lc] = 0;
            }
            else
            {
                ltrs[1] = 0;
                lc = 1;
            }

            for(int i=0;i<d;++i)
            {
                if(!bad[i])
                {
                    bool isbad = true;
                    for(int j=0;j<lc;++j)
                    {
                        if(ltrs[j] == lang[i][cc])
                        {
                            isbad = false;
                            break;
                        }
                    }
                    if(isbad)
                    {
                        bad[i] = true;
                        --nw;
                    }
                }
            }
            ++cc;
        }
        while(cc<l);
        cout<<"Case #"<<q+1<<": "<<nw<<"\n";
    }
}
