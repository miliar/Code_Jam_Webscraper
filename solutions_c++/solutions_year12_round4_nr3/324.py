#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<string>
#include<vector>

#define forn(i,n) for(int i=0;i<(int)n;i++)
#define dforn(i,n) for(int i=(int)n-1;i>=0;i--)
#define all(v) v.begin(),v.end()

using namespace std;

vector<int> vec,res;

int main()
{
	#ifdef ACMTUYO
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	#endif
	int casos;
	cin >> casos;
	forn(casito,casos)
	{
	    int n;
	    cin >> n;
	    vec.resize(n-1);
	    forn(i,n-1)
	    {
            cin >> vec[i];
            vec[i]--;
	    }
        res.resize(n);
        bool sepuede = true;
        forn(i,n)
        forn(j,i)
        if(vec[i]>vec[j]&&vec[j]>i)
        {
            sepuede = false;
        }
        if(sepuede==false)
        {
            cout <<"Case #"<<casito+1 <<": Impossible"<< endl;
            continue;
        }
        forn(i,n)
            res[i] = -1;
        int mucho = 1000000000;
        res[n-1] = mucho;
        int t = 0;
        while(t!=n-1)
        {
            res[t] = mucho;
            t = vec[t];
        }
        for(int i=n-2;i>=0;i--)
        {
            if(res[i] == -1)
            {
                if(res[vec[i]]==mucho)
                {
                    res[i] = mucho-1;
                }
                else
                {
                    int a = i, b = vec[i], c = vec[vec[i]];
                    int ra, rb = res[b], rc = res[c];
                    ra = rc - (c-a)*(rc-rb)/(c-b) - 1;
                    res[i] = ra;
                }
            }
        }
	    cout <<"Case #"<< casito+1 <<":";
	    forn(i,n)
            cout <<" "<< res[i];
        cout << endl;
	}
}
