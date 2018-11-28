#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;
#define PB push_back
#define PPB pop_back

int kasus,ganti,hapus,pas[30],pjg,cnt;
string awal,sem;
char ke,kata[150],blkg;
map <string,char> m;
bool masih;
vector <char> v;

int main()
{
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        memset(pas,-1,sizeof(pas));
        m.clear();
        v.clear();

        scanf("%d",&ganti);
        for (int i=1;i<=ganti;i++)
        {
            scanf("%s",kata);
            awal = kata[0];
            awal += kata[1];
            ke = kata[2];
            m[awal] = ke;
            awal = kata[1];
            awal += kata[0];
            m[awal] = ke;
        }
        scanf("%d",&hapus);
        for (int i=1;i<=hapus;i++)
        {
            scanf("%s",kata);
            pas[kata[0]-'A'] = kata[1]-'A';
            pas[kata[1]-'A'] = kata[0]-'A';
        }
        scanf("%d",&pjg);
        scanf("%s",kata);

        for (int i=0;i<pjg;i++)
        {
            if (v.size()==0) v.PB(kata[i]);
            else
            {
                masih = true;
                v.PB(kata[i]);
                while (masih && v.size()>1)
                {
                    masih = false;
                    sem = v[v.size()-2];
                    sem += v[v.size()-1];
//                    cout << sem << endl;
                    if (m.count(sem)!=0)
                    {
                        v.PPB();
                        v.PPB();
                        v.PB(m[sem]);
                        masih = true;
                    }
                }
                blkg = v[v.size()-1];
                for (int j=0;j<v.size()-1;j++)
                {
                    if (v[j]-'A'==pas[blkg-'A'])
                    {
                        v.clear();
                        break;
                    }
                }
            }
        }
        printf("Case #%d: [",z);
        for (int i=0;i<v.size();i++)
        {
            if (i>0) printf(", ");
            printf("%c",v[i]);
        }
        printf("]\n");
    }
//    system("PAUSE");
    return 0;
}
