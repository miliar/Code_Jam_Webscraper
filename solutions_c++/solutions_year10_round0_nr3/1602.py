#include <iostream>
#include <vector>
#include <map>
using namespace std;
string getstr(int* ptr, int start, int n)
{
    char temp[1010];
    for(int i = start, times = 0; times < n; i = (i+1) % n, times++ )
    {
        temp[times] = ptr[i]%255 + 1;
    }
    temp[n] = 0;
    string newstr = temp;
    return newstr;
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int caseNum, i, j, r, k, n, start, group[1100], money[1500], ite, beg;
    long long ans;
    scanf("%d",&caseNum);
    for(i = 0; i < caseNum; ++i)
    {
        ans = 0;
        map<string, int> cycle;
        map<string, int>::iterator where;
        scanf("%d%d%d",&r,&k,&n);
        for(j = 0; j < n; ++j)
            scanf("%d",group+j);

        ite = start = 0;
        while(true)
        {
            //cout << "strat is  "<< start<<endl;
            string tmp = getstr(group, start, n);
            //cout <<"string is   "<< tmp<<endl;
            where = cycle.find(tmp);
            if(where == cycle.end() )
            {
                cycle[tmp] = ite;
                int tol = 0, tims = 0;
                while((tol + group[start]) <= k && tims < n)
                {
                    tol += group[start];
                    start = (start + 1) % n;
                    tims++;
                }
                money[ite++] = tol;
            }
            else
            {
                beg = cycle[tmp];
                break;
            }
        }
        for(j=0;j<beg;++j)
            ans += money[j];
        long long re = 0;
        for(j = beg; j < ite; ++j)
            re += money[j];
        int cy = ite - beg;
        long long times = (r-beg)/cy;
        int rest = (r-beg)%cy;
        ans += re*times;
        //cout << "cycle beg:"<< beg << "cycle ite:"<<ite<<endl;
        //cout << "money in cycle:" << re <<endl;
        for(j = beg, times = 0; times<rest; ++j, ++times)
        {
            ans += money[j];
        }
        cout << "Case #"<< i + 1 << ": "<<ans <<endl;
    }

    return 0;
}
