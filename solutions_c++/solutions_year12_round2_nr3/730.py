#include <cstdio>
#include <vector>
using namespace std;

int nb[20];

bool trouve;
vector<int> res1, res2;

void bourrin(vector<int> A, vector<int> B, int i, int s1, int s2, int s)
{
    if (trouve) return;
    if (i == 20)
    {
        if (s1 == s2 && s1 != 0)
        {
            res1 = A;
            res2 = B;
            trouve = true;
        }
        return;
    }
    
    if (s1 + s < s2) return;
    if (s2 + s < s1) return;
    
    A.push_back(nb[i]);
    s1 += nb[i];
    bourrin(A, B, i+1, s1, s2, s - nb[i]);
    s1 -= nb[i];
    A.pop_back();
    
    B.push_back(nb[i]);
    s2 += nb[i];
    bourrin(A, B, i+1, s1, s2, s - nb[i]);
    s2 -= nb[i];
    B.pop_back();
    
    bourrin(A, B, i+1, s1, s2, s - nb[i]);
}

void main2()
{
    int N;
    scanf("%d", &N);
    
    trouve = false;
    res1.clear();
    res2.clear();
    
    int somme = 0;
    for (int i=0; i<N; i++)
    {
        scanf("%d", &nb[i]);
        somme += nb[i];
    }
    
    bourrin(res1, res1, 0, 0, 0, somme);
    
    if (trouve)
    {
        for (int i=0; i<(int)res1.size(); i++)
            printf("%d ", res1[i]);
        printf("\n");
        for (int i=0; i<(int)res2.size(); i++)
            printf("%d ", res2[i]);
        printf("\n");
    }
    else
    printf("Impossible\n");
}

int main()
{
    int N;
    scanf("%d", &N);
    for (int i=0; i<N; i++)
    {
        printf("Case #%d:\n", i+1);
        main2();
    }
}
