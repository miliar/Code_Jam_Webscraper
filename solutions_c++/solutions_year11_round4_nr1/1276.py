#include <cstdio>
#include <set>
using namespace std;

struct box
{
    int start, end;
    int value;
    box()
    {
    }
    box(int a, int b, int c)
    {
        start = a;
        end = b;
        value = c;
    }
};

struct cmp{
    bool operator()(const box&a, const box&b)
    {
        return a.value<b.value;
    }
};

int main()
{
    int z;
    scanf("%d", &z);
    for(int q=1; q<=z; q++)
    {
        int x, s, r, t, n;
        long double wynik = 0.0;
        multiset<box, cmp> Set;
        scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
        long double time = (long double)t;

        int prevPoint = 0;

        for(int i=0; i<n; i++)
        {
            int a,b,c;
            scanf("%d%d%d", &a, &b, &c);
            if(prevPoint!=a){
                Set.insert(box(prevPoint, a, 0));
            }
            Set.insert(box(a,b,c));
            prevPoint = b;
        }
        if(prevPoint!=x){
            Set.insert(box(prevPoint, x, 0));
        }

        set<box>::iterator it;
        //printf("--\n");
        for(it = Set.begin(); it != Set.end(); it++)
        {
                int start = it->start;
                int end = it->end;
                int speed = it->value;
                //printf("%d %d %d\n", start, end, speed);
            if(time>0){
                long double tTime = ((long double)end-(long double)start)/(long double)(r+speed);
                //czas przebiegniecia
                if(tTime <= time)
                {
                    //printf("case 1 ");
                    //mamy czas na przebiegniecie
                    time -= tTime;
                    wynik += tTime;
                }else{
                    //printf("case 2 ");
                    //czesc biegniemy, czesc idziemy
                    wynik += time; //tyle biegniemy
                    //printf("time(1) %Lf", time);
                    //reszte idziemy
                    long double length = end-start;
                    length -= (long double)(r+speed)*time;
                    time = 0; 
                    wynik += length/(long double)(speed+s);
                }
            }else{
                //printf("case 3 ");
                wynik += ((long double)end-start)/((long double)speed+s);
            }
            //printf("%Lf\n", wynik);
        }
        printf("Case #%d: %.10Lf\n", q, wynik);
    }
    return 0;
}
