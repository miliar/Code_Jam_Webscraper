#include <iostream>
#include <utility>

#define MAX 1100

using namespace std;
typedef pair<long long,int> stan;

int main()
{
    ios_base::sync_with_stdio(0);
    
    int Testow;
    cin>>Testow;
    
    for (int nr=1; nr<=Testow; ++nr)
    {
        int R,k,N;
        cin>>R>>k>>N;
        int T[MAX]={};
        stan W[MAX]={};
        
        for (int i=0; i<N; ++i) cin>>T[i];
        
        for (int i=0; i<N; ++i) //O(N^2)
        {
            long long& ile=W[i].first=0;
            int& j=W[i].second=i;
            int licznik=0;
        
            while (ile+T[j]<=k && ++licznik<=N)
            {
                ile+=T[j];
                j=(j+1)%N;
            }
        }
        
        int poz=0;
        
        bool Visited[MAX]={};
        while (!Visited[poz]) //O(N); Wyznaczam cykl
        {
            Visited[poz]=true;
            poz=W[poz].second;  
        }
        
        long long wynik1=0,wynik2=0;
        int j=0;
        int licznik1=0,licznik2=0;
        
        while (j!=poz)
        {
            ++licznik1;
            wynik1+=W[j].first;
            j=W[j].second;
        }
        
        while (j!=poz || licznik2==0)
        {
            ++licznik2;
            wynik2+=W[j].first;
            j=W[j].second;
        }
        
        long long wynik=0;
        
        if (R>=licznik1+licznik2)
        {
            wynik=wynik1+wynik2*((R-licznik1)/licznik2);
            R-=licznik1;
            R%=licznik2;
        }
        else poz=0;
        
        for (int i=1; i<=R; ++i) //O(R)
        {
            wynik+=W[poz].first;
            poz=W[poz].second;
        }
    
        cout<<"Case #"<<nr<<": "<<wynik<<endl;
    }
    return 0;
}
