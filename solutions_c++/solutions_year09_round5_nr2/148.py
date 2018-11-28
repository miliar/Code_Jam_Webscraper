#include<algorithm>
#include<cmath>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<sstream>
#include<stack>
#include<vector>

using namespace std;

#define forn(i,n) for(int i = 0; i < (n); i++)
#define dforn(i,n) for(int i = (int)(n-1); i >= 0; i--)
#define all(v) v.begin(), v.end()
#define pb push_back

int letras[26];

int calc2(string &st)
{
    int res = 1;
    forn(i,st.size())
    {
        res*=letras[st[i]-'a'];
        res%=10009;
    }
    return res;
}

int calc(string &st, string &dic)
{
    vector<int> vec;
    forn(i,st.size())
    {
        if(st[i] == '+')
            st[i] = ' ';
    }
    istringstream iss;
    string st2;
    iss.str(st);
    iss.clear();
    forn(i,26)
        letras[i] = 0;
    forn(i,dic.size())
        letras[dic[i]-'a']++;
    while(iss>>st2)
    {
        vec.push_back(calc2(st2));
    }
    int res = 0;
    forn(i,vec.size())
    {
        res+=vec[i];
        res%=10009;
    }
    return res;
}

int main()
{
    freopen("B-small.out","w",stderr);
	freopen("B-small.in","r",stdin);
	int casos;
	cin >> casos;
	forn(casito,casos)
	{
	    vector<int> res;
	    int n,k;
	    string st;
	    string pal;
	    vector<string> paltot;
	    cin >> st;
	    cin >> k;
	    cin >> n;
	    getline(cin,pal);
	    cerr << "Case #" << casito+1 << ": ";
	    forn(i,n)
	    {
	        getline(cin,pal);
	        paltot.push_back(pal);
	    }
        int sum = 0;
        forn(i1,paltot.size())
        {
            sum += calc(st,paltot[i1]);
            sum %= 10009;
        }
        cerr << sum;
        if(k>=2)
        {
            cerr << ' ';
            sum = 0;
            forn(i1,paltot.size())
            forn(i2,paltot.size())
            {
                pal = paltot[i1]+paltot[i2];
                sum += calc(st,pal);
                sum %= 10009;
            }
            cerr << sum;
        }
        if(k>=3)
        {
            cerr << ' ';
            sum = 0;
            forn(i1,paltot.size())
            forn(i2,paltot.size())
            forn(i3,paltot.size())
            {
                pal = paltot[i1]+paltot[i2]+paltot[i3];
                sum += calc(st,pal);
                sum %= 10009;
            }
            cerr << sum;
        }
        if(k>=4)
        {
            cerr << ' ';
            sum = 0;
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            forn(i4,i3)
            {
                pal = paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4];
                sum += 24*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i2]+paltot[i3];
                sum += 12*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i2]+paltot[i2]+paltot[i3];
                sum += 12*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i2]+paltot[i3]+paltot[i3];
                sum += 12*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i2]+paltot[i2];
                sum += 6*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i2];
                sum += 4*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i2]+paltot[i2]+paltot[i2];
                sum += 4*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i1];
                sum += calc(st,pal);
                sum %= 10009;
            }
            cerr << sum;
        }
        if(k>=5)
        {
            cerr << ' ';
            sum = 0;
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            forn(i4,i3)
            forn(i5,i4)
            {
                pal = paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4]+paltot[i5];
                sum += 120*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            forn(i4,i3)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4];
                sum += 60*calc(st,pal);
                sum %= 10009;
                pal = paltot[i2]+paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4];
                sum += 60*calc(st,pal);
                sum %= 10009;
                pal = paltot[i3]+paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4];
                sum += 60*calc(st,pal);
                sum %= 10009;
                pal = paltot[i4]+paltot[i1]+paltot[i2]+paltot[i3]+paltot[i4];
                sum += 60*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i2]+paltot[i2]+paltot[i3];
                sum += 30*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i3]+paltot[i2]+paltot[i2]+paltot[i3];
                sum += 30*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i1]+paltot[i3]+paltot[i2]+paltot[i3];
                sum += 30*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i2]+paltot[i2];
                sum += 10*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i1]+paltot[i2]+paltot[i2]+paltot[i2];
                sum += 10*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            forn(i3,i2)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i2]+paltot[i3];
                sum += 20*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i2]+paltot[i2]+paltot[i2]+paltot[i3];
                sum += 20*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i3]+paltot[i3]+paltot[i2]+paltot[i3];
                sum += 20*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            forn(i2,i1)
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i1]+paltot[i2];
                sum += 5*calc(st,pal);
                sum %= 10009;
                pal = paltot[i1]+paltot[i2]+paltot[i2]+paltot[i2]+paltot[i2];
                sum += 5*calc(st,pal);
                sum %= 10009;
            }
            forn(i1,paltot.size())
            {
                pal = paltot[i1]+paltot[i1]+paltot[i1]+paltot[i1]+paltot[i1];
                sum += calc(st,pal);
                sum %= 10009;
            }
            cerr << sum;
        }
        cerr << endl;
	}
}
