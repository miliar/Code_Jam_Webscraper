#include <cstdio>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

class Data
{
        public:
        int T;
        void Wczytaj()
        {
                int A,B;
                char C;
                scanf("%d%c%d",&A,&C,&B);
                T = A*60+B;
        }
};

class Tro
{
        public:
        int S,D,T;
        Tro(int S1,int D1,int T1):S(S1),D(D1),T(T1){}
        bool operator < (const Tro&X)const
        {
                if (S != X.S) return S < X.S;
                if (D != X.D) return D < X.D;
                return T < X.T;
        }
};

int main()
{
        int lw;
        scanf("%d",&lw);
        for (int L=1;L<=lw;L++)
        {
                int P;
                scanf("%d",&P);
                int A,B;
                scanf("%d%d",&A,&B);
                vector< Tro > Z;
                Data Temp1,Temp2;
                for (int i=0;i<A;i++)
                {
                        Temp1.Wczytaj();
                        Temp2.Wczytaj();
                        Z.push_back( Tro(Temp1.T,Temp2.T,0) );
                }
                for (int i=0;i<B;i++)
                {
                        Temp1.Wczytaj();
                        Temp2.Wczytaj();
                        Z.push_back( Tro(Temp1.T,Temp2.T,1) );
                }
                sort(Z.begin(),Z.end());
                int Left = 0;
                int Right = 0;

                for (int i=0;i<Z.size();i++)
                {
                    if (Z[i].T == -1) continue;
                    int Akt;
                    int TimeT;
                        if (Z[i].T == 0)
                        {
                            Left++;
                            Akt = 1;
                        }
                        else
                        {
                            Right++;
                            Akt = 0;
                        }
                    TimeT = Z[i].D + P;
                    for (int j=i+1;j<Z.size();j++)
                    {
                        if ((Z[j].S >= TimeT) && (Z[j].T == Akt))
                        {
                            TimeT = Z[j].D+P;
                            Akt = (Z[j].T+1)%2;
                            Z[j].T = -1;
                        }
                    }
                }
                printf("Case #%d: %d %d\n",L,Left,Right);
        }

        return 0;
}
