#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
using namespace std;
#define PB push_back

int kasus,jml,o,b,po,pb,jawab,lama,angka;
vector <int> vo,vb;
vector <string> v;
char k[2];
string kata;

int abs(int a,int b) {return (a>=b) ? a-b : b-a;}

int main()
{
    scanf("%d",&kasus);
    for (int z=1;z<=kasus;z++)
    {
        vo.clear(); vb.clear();
        v.clear();
        scanf("%d",&jml);
        for (int i=1;i<=jml;i++)
        {
            scanf("%s %d",k,&angka);
            kata = k;
            v.PB(kata);
            if (kata=="O") vo.PB(angka);
            else vb.PB(angka);
        }
        po = pb = jawab = 0;
        o = b = 1;
        for (int i=0;i<v.size();i++)
        {
            if (v[i]=="O")
            {
                lama = abs(vo[po]-o)+1;
                jawab += lama;
                if (pb<vb.size())
                {
                    if (abs(vb[pb]-b)<=lama) b = vb[pb];
                    else {(b<vb[pb]) ? b += lama : b -= lama;}
                }
                o = vo[po];
                po++;
            }
            else
            {
                lama = abs(vb[pb]-b)+1;
                jawab += lama;
                if (po<vo.size())
                {
                    if (abs(vo[po]-o)<=lama) o = vo[po];
                    else {(o<vo[po]) ? o += lama : o -= lama;}
                }
                b = vb[pb];
                pb++;
            }
        }
        printf("Case #%d: %d\n",z,jawab);
    }
//    system("PAUSE");
    return 0;
}
