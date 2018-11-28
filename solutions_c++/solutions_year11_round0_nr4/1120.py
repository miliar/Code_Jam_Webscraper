#include <iostream>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>

#define pb push_back
#define foreach(it, c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef long long LL;

template<typename T> int size(const T &a) { return a.size(); }

double n[2000];
int data[2000];
bool visit[2000];

void process(void)
{
    int N;
    scanf("%d",&N);
    int gp = 0;
    for(int i=0;i<N;i++)
    {
        scanf("%d",&data[i]);
        if(data[i] == i+1)
        {
            gp++;
        }
    }

    printf("%d.000000\n", N-gp);
}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=0;i<T;i++)
    {
        printf("Case #%d: ",i+1);
        process();
    }
}
